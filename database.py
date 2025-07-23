from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Caminho do banco SQLite (arquivo local na mesma pasta)
DATABASE_URL = "sqlite:///./sales.db"

# Criação da engine de conexão
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria sessão de acesso ao banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()
