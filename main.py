from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db 
import models, schemas
from routes import livros, usuarios, emprestimos

app = FastAPI()

Base.metadata.create_all(bind=engine)



@app.get("/")
def home():
    return {"mensagem": "Biblioteca API funcionando!"}

app.include_router(livros.router)
app.include_router(usuarios.router)
app.include_router(emprestimos.router)