from fastapi import FastAPI

app = FastAPI(title='API do Gustavo e do Ronald lindao')

@app.get("/")
def hello():
    return{"mensage": "Hello World!"}
