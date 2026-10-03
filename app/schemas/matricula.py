from pydantic import BaseModel

class MatriculaCreate(BaseModel):
    aluno_id: int
    disciplina_id: int

class MatriculaResponse(BaseModel):
    aluno_id: int
    disciplina_id: int

    class Config:
        from_attributes = True