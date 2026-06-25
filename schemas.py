from pydantic import BaseModel

class LivroCreate(BaseModel):
    titulo: str
    autor: str
    quantidade_total: int

class LivroResponse(BaseModel):
    id: int
    titulo: str
    autor: str
    quantidade_total: int
    quantidade_disponivel: int

    class Config:
        from_attributes = True

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    
class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True

class EmprestimoCreate(BaseModel):
    usuario_id: int
    livro_id: int

class EmprestimoResponse(BaseModel):
    id: int
    usuario_id: int
    livro_id: int
    status: str

    class Config:
        from_attributes = True
