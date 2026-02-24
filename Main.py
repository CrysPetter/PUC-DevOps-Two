from fastapi import FastAPI
from pygments.lexer import default

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste1")
async def funcaoteste():
    return {"message": "Deu certo o teste nº 02"}