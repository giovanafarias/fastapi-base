import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Obtém a URL de conexão das variáveis de ambiente. 
# Caso a variável "DATABASE_URL" não exista, utiliza o valor padrão.  
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://post_user:post_pass@db:5432/fastapi_db")

# Referência do SQLAlchemy, para gerenciar a conexão com o banco. 
engine = create_engine(DATABASE_URL)

# Cria (cada) instância será uma sessão independente com o banco. 
# autocommit=False: db.commit() manualmente para salvar alterações.   
# autoflush=False: impede envio automático de alterações pendentes antes de cada consulta.   
# bind=engine: Associa a sessão ao motor de conexão criado acima.  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Referêcnia para as modelos ORM - irão herdar essa classe "Base".
Base = declarative_base()

# Função utilitária para obter a sessão do banco nas rotas do FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
