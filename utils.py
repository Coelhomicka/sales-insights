import os
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carrega variáveis do .env
load_dotenv()

# Conecta ao banco SQLite local
engine = create_engine("sqlite:///./sales.db")
db = SQLDatabase(engine)

# Inicializa o modelo LLM da OpenAI
llm = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Cria agente LangChain com acesso ao banco SQL
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    verbose=True
)

# Lista de palavras-chave que definem o escopo da aplicação
ALLOWED_KEYWORDS = ["venda", "produto", "cliente", "categoria", "quantidade", "valor", "data", "faturamento", "sku", "email"]

def is_question_in_scope(question: str) -> bool:
    """Verifica se a pergunta está dentro do escopo permitido para evitar alucinações do LLM."""
    return any(keyword in question.lower() for keyword in ALLOWED_KEYWORDS)

def ask_sales_question(question: str) -> str:
    """
    Recebe uma pergunta, verifica se está dentro do escopo permitido e 
    executa via LangChain e SQLAgent.
    
    Esta abordagem previne alucinações forçando uso de RAG em um contexto controlado.
    """
    if not is_question_in_scope(question):
        return " Pergunta fora do escopo permitido. Reformule usando termos relacionados a vendas, produtos ou clientes."

    try:
        return agent_executor.run(question)
    except Exception as e:
        return f"Erro ao processar a pergunta: {str(e)}"
