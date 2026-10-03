from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.aluno import Aluno
from app.schemas import AlunoCreate, AlunoResponse

router = APIRouter(
    prefix="/alunos",
    tags=["Alunos"]
)

# 1. CRIAR ALUNO
@router.post("", response_model=AlunoResponse, status_code=status.HTTP_201_CREATED)
def criar_aluno(aluno_dados: AlunoCreate, db: Session = Depends(get_db)):
    novo_aluno = Aluno(
        nome=aluno_dados.nome,
        curso_id=aluno_dados.curso_id
    )

    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)

    return novo_aluno


# 2. LISTAR TODOS OS ALUNOS
@router.get("", response_model=List[AlunoResponse])
def listar_alunos(db: Session = Depends(get_db)):
    return db.query(Aluno).all()


# 3. BUSCAR ALUNO POR ID
@router.get("/{aluno_id}", response_model=AlunoResponse)
def buscar_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()

    if not aluno:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    return aluno


# 4. ATUALIZAR ALUNO
@router.put("/{aluno_id}", response_model=AlunoResponse)
def atualizar_aluno(
    aluno_id: int,
    aluno_dados: AlunoCreate,
    db: Session = Depends(get_db)
):
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()

    if not aluno:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    aluno.nome = aluno_dados.nome
    aluno.curso_id = aluno_dados.curso_id

    db.commit()
    db.refresh(aluno)

    return aluno


# 5. DELETAR ALUNO
@router.delete("/{aluno_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()

    if not aluno:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    db.delete(aluno)
    db.commit()

    return None