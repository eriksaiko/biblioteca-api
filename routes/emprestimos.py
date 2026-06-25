from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from fastapi import HTTPException
import models
import schemas
from services.emprestimo_service import criar_emprestimo

router = APIRouter()



@router.post("/emprestimos")
def emprestar_livro(dados: schemas.EmprestimoCreate, db: Session = Depends(get_db)):
    return criar_emprestimo(db, dados)



@router.get("/emprestimos", response_model=list[schemas.EmprestimoResponse])
def listar_emprestimos(db: Session = Depends(get_db)):
    return db.query(models.Emprestimo).all()



@router.get("/emprestimos/{emprestimo_id}", response_model=schemas.EmprestimoResponse)
def buscar_emprestimo(emprestimo_id: int, db: Session = Depends(get_db)):

    emprestimo = db.query(models.Emprestimo).filter(
        models.Emprestimo.id == emprestimo_id
    ).first()

    if not emprestimo:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")

    return emprestimo



@router.get("/usuarios/{usuario_id}/emprestimos", response_model=list[schemas.EmprestimoResponse])
def listar_por_usuario(usuario_id: int, db: Session = Depends(get_db)):

    return db.query(models.Emprestimo).filter(
        models.Emprestimo.usuario_id == usuario_id
    ).all()


@router.put("/emprestimos/{emprestimo_id}/devolver", response_model=schemas.EmprestimoResponse)
def devolver_emprestimo(emprestimo_id: int, db: Session = Depends(get_db)):

    emprestimo = db.query(models.Emprestimo).filter(
        models.Emprestimo.id == emprestimo_id
    ).first()

    if not emprestimo:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")

    if emprestimo.status == "devolvido":
        raise HTTPException(status_code=400, detail="Empréstimo já foi devolvido")

    livro = db.query(models.Livro).filter(
        models.Livro.id == emprestimo.livro_id
    ).first()

    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    emprestimo.status = "devolvido"
    livro.quantidade_disponivel += 1

    db.commit()
    db.refresh(emprestimo)

    return emprestimo
