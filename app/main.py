from fastapi import FastAPI
from app.endpoints import curso_router
from app.endpoints import disciplina_router # Linha Adicionada
from app.endpoints import aluno_router
from app.endpoints import matricula_router

# Criando uma instância do FastAPI
app = FastAPI(
    title="Sistema Acadêmico - Modular",
    description="API para gerenciamento de cursos e disciplinas",
    version="1.0.0"
)

# Incluindo as rotas do recurso de Cursos
app.include_router(curso_router)

# Incluindo as rotas do recurso de Disciplinas
app.include_router(disciplina_router) # Linha Adicionada

app.include_router(aluno_router) 

app.include_router(matricula_router) 

# Definindo a rota principal "/"
@app.get("/")
def raiz():
    return {"mensagem": "Bem-vindo à API do Sistema Acadêmico!"}
