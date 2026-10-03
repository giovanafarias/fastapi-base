from pydantic import BaseModel

class MatriculaCreate(BaseModel):
    aluno_id: int
    disciplina_id: int

class MatriculaResponse(BaseModel):
    id: int
    aluno_id: int
    disciplina_id: int

    class Config:
        from_attributes = True