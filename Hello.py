from fastapi import FastAPI

app = FastAPI()
app.title = "Mi aplicación con  FastAPI"  # Personalizar titulo Documentacion 
app.version = "0.0.1" # Personalizar titulo Documentacion 

@app.get('/')
def message():
    return "Hello From FastAPI! "