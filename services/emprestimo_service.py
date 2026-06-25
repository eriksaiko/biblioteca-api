from fastapi import HTTPException
import models



def criar_emprestimo(db, dados):

    livro = db.query(models.Livro).filter(models.Livro.id == dados.livro_id).first()

    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    usuario = db.query(models.Usuario).filter(models.Usuario.id == dados.usuario_id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    emprestimo_existente = db.query(models.Emprestimo).filter(
        models.Emprestimo.usuario_id == dados.usuario_id,
        models.Emprestimo.livro_id == dados.livro_id,
        models.Emprestimo.status == "emprestado"
    ).first()

    if emprestimo_existente:
        raise HTTPException(status_code=400, detail="Já possui empréstimo ativo")

    if livro.quantidade_disponivel <= 0:
        raise HTTPException(status_code=400, detail="Sem estoque")

    novo_emprestimo = models.Emprestimo(
        usuario_id=dados.usuario_id,
        livro_id=dados.livro_id,
        status="emprestado"
    )

    livro.quantidade_disponivel -= 1

    db.add(novo_emprestimo)
    db.commit()
    db.refresh(novo_emprestimo)

    return novo_emprestimo
