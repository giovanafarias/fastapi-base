from pydantic import BaseModel

class AlunoCreate(BaseModel):
    nome: str
    curso_id: int

class AlunoResponse(BaseModel):
    id: int
    nome: str
    curso_id: int

    class Config:
        from_attributes = True