from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.curso import Curso
from app.schemas import CursoCreate, CursoResponse

# Roteador com o prefixo e a tag para organizar o Swagger
router = APIRouter(
    prefix="/cursos",
    tags=["Cursos"]
)

# --- 1. CRIAR CURSO (POST /cursos) ---
@router.post("", response_model=CursoResponse, status_code=status.HTTP_201_CREATED)
def criar_curso(curso_dados: CursoCreate, db: Session = Depends(get_db)):
    novo_curso = Curso(nome=curso_dados.nome, duracao=curso_dados.duracao)
    db.add(novo_curso)
    db.commit()
    db.refresh(novo_curso)
    return novo_curso

# --- 2. LISTAR TODOS OS CURSOS (GET /cursos) ---
@router.get("", response_model=List[CursoResponse])
def listar_cursos(db: Session = Depends(get_db)):
    return db.query(Curso).all()

# --- 3. BUSCAR UM CURSO POR ID (GET /cursos/{curso_id}) ---
@router.get("/{curso_id}", response_model=CursoResponse)
def buscar_curso(curso_id: int, db: Session = Depends(get_db)):
    curso = db.query(Curso).filter(Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return curso

# --- 4. ATUALIZAR UM CURSO (PUT /cursos/{curso_id}) ---
@router.put("/{curso_id}", response_model=CursoResponse)
def atualizar_curso(curso_id: int, curso_dados: CursoCreate, db: Session = Depends(get_db)):
    curso = db.query(Curso).filter(Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    
    curso.nome = curso_dados.nome
    curso.duracao = curso_dados.duracao
    db.commit()
    db.refresh(curso)
    return curso

# --- 5. DELETAR UM CURSO (DELETE /cursos/{curso_id}) ---
@router.delete("/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_curso(curso_id: int, db: Session = Depends(get_db)):
    curso = db.query(Curso).filter(Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    
    db.delete(curso)
    db.commit()
    return None
