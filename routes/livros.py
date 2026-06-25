from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter()



@router.post("/livros", response_model=schemas.LivroResponse)
def criar_livro(livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    novo_livro = models.Livro(
        titulo=livro.titulo,
        autor=livro.autor,
        quantidade_total=livro.quantidade_total,
        quantidade_disponivel=livro.quantidade_total
    )

    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)

    return novo_livro



@router.get("/livros", response_model=list[schemas.LivroResponse])
def listar_livros(db: Session = Depends(get_db)):
    return db.query(models.Livro).all()



@router.get("/livros/{livro_id}", response_model=schemas.LivroResponse)
def buscar_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()

    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro



@router.put("/livros/{livro_id}", response_model=schemas.LivroResponse)
def atualizar_livro(livro_id: int, dados: schemas.LivroCreate, db: Session = Depends(get_db)):
    livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()

    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    livro.titulo = dados.titulo
    livro.autor = dados.autor
    livro.quantidade_total = dados.quantidade_total

    db.commit()
    db.refresh(livro)

    return livro



@router.delete("/livros/{livro_id}")
def deletar_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()

    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    db.delete(livro)
    db.commit()

    return {"mensagem": "Livro removido com sucesso!"}
