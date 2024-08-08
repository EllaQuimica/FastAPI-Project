from fastapi import FastAPI
<<<<<<< HEAD
from pydantic import BaseModel
=======

>>>>>>> master

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: str

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


<<<<<<< HEAD
# Created a new object for data validation in BOOK using PyDantic
class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: str

=======
>>>>>>> master

BOOKS= [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

<<<<<<< HEAD
@app.post("/create_book")
#async def create_book(book_request = Body()):
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)
=======
>>>>>>> master


