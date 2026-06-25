# Biblioteca API

Este projeto é uma API REST desenvolvida com FastAPI para gerenciamento de uma biblioteca simples, permitindo o controle de livros, usuários e empréstimos.

A aplicação simula um sistema real de biblioteca, com regras como controle de estoque de livros e validação de empréstimos ativos.

---

## Tecnologias

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

---

## Funcionalidades

### Livros
- Criar livro
- Listar livros
- Buscar livro
- Atualizar livro
- Deletar livro

### Usuários
- Criar usuário
- Listar usuários
- Buscar usuário
- Atualizar usuário
- Deletar usuário

### Empréstimos
- Criar empréstimo
- Listar empréstimos
- Devolver livro
- Ver empréstimos por usuário

---

## Estrutura do projeto

- main.py
- models.py
- database.py
- schemas.py
- routes/
- services/

---

## Como rodar

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Acesse: http://127.0.0.1:8000/docs
