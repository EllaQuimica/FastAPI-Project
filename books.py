from fastapi import FastAPI


app = FastAPI()


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'},

]

@app.get("/")
def first_api():
    return {"message": "Hello SheCodifies!"}


# Obtenemos todos los libros
@app.get("/api-endpoint") #ruta estatica
def first_api():
    return BOOKS

@app.get("/books/mybook") #ruta estatica
def read_all_book():
    return {'book_title': 'My favorite book!'}

# Parametros dinamicos
@app.get("/books/{dynamic_param}") #ruta dinamica
def read_all_book(dynamic_param: str):
    return {'dynamic_param': dynamic_param}

#solicitud por titulo
@app.get("/books/{book_title}")
def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        

#Query Parameters -> esto es cuando el request URL:127.0.0.1:8000/books/?category=science

@app.get("/books")
def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


#Query Parameters -> esto es cuando el request URL:127.0.0.1:8000/books/author%20four/?category=science
@app.get("/books/{boook_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return
