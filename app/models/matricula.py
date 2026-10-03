from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Matricula(Base):
    __tablename__ = "matriculas"

    aluno_id = Column(Integer, ForeignKey("alunos.id", ondelete="CASCADE"), primary_key=True)
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id", ondelete="CASCADE"), primary_key=True)

    aluno = relationship("Aluno", back_populates="matriculas")
    disciplina = relationship("Disciplina", back_populates="matriculas")