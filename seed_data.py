from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal, engine
from models import Base

SQL_SCRIPT_PATH = "script_dump_banco.txt"

def execute_sql_file(db: Session, file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        sql_commands = f.read()

        for command in sql_commands.split(";"):
            cmd = command.strip()

            # Ignora comentários e linhas vazias
            if not cmd or cmd.startswith("--"):
                continue

            try:
                db.execute(text(cmd))
            except Exception as e:
                print(f"\n❌ Erro ao executar:\n{cmd}\nErro: {e}")

def main():
    print("⏳ Criando tabelas e carregando dados...")

    # Cria as tabelas se não existirem
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        execute_sql_file(db, SQL_SCRIPT_PATH)
        db.commit()
        print("✅ Dados carregados com sucesso no banco!")
    except Exception as e:
        print("❌ Erro ao carregar dados:", e)
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()
