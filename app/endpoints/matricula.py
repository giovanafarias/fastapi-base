from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.matricula import Matricula
from app.schemas import MatriculaCreate, MatriculaResponse

router = APIRouter(
    prefix="/matriculas",
    tags=["Matrículas"]
)

# 1. CRIAR MATRÍCULA
@router.post("", response_model=MatriculaResponse, status_code=status.HTTP_201_CREATED)
def criar_matricula(
    matricula_dados: MatriculaCreate,
    db: Session = Depends(get_db)
):
    nova_matricula = Matricula(
        aluno_id=matricula_dados.aluno_id,
        disciplina_id=matricula_dados.disciplina_id
    )

    db.add(nova_matricula)
    db.commit()
    db.refresh(nova_matricula)

    return nova_matricula


# 2. LISTAR TODAS AS MATRÍCULAS
@router.get("", response_model=List[MatriculaResponse])
def listar_matriculas(db: Session = Depends(get_db)):
    return db.query(Matricula).all()


# 3. BUSCAR MATRÍCULA
@router.get("/{aluno_id}/{disciplina_id}", response_model=MatriculaResponse)
def buscar_matricula(
    aluno_id: int,
    disciplina_id: int,
    db: Session = Depends(get_db)
):
    matricula = db.query(Matricula).filter(
        Matricula.aluno_id == aluno_id,
        Matricula.disciplina_id == disciplina_id
    ).first()

    if not matricula:
        raise HTTPException(
            status_code=404,
            detail="Matrícula não encontrada"
        )

    return matricula


# 4. REMOVER MATRÍCULA
@router.delete(
    "/{aluno_id}/{disciplina_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def deletar_matricula(
    aluno_id: int,
    disciplina_id: int,
    db: Session = Depends(get_db)
):
    matricula = db.query(Matricula).filter(
        Matricula.aluno_id == aluno_id,
        Matricula.disciplina_id == disciplina_id
    ).first()

    if not matricula:
        raise HTTPException(
            status_code=404,
            detail="Matrícula não encontrada"
        )

    db.delete(matricula)
    db.commit()

    return None