#Testes de Importação de Bibliotecas
# Este script verifica se as bibliotecas necessárias estão instaladas e prontas para uso.
def test_imports():
    try:
        import openai
    except ImportError:
        print("OpenAI library is not installed.")   
        print("Please install it using: pip install openai")

    try:
        from langchain_openai import ChatOpenAI
    except ImportError:
        print("LangChain OpenAI library is not installed.")
        print("Please install it using: pip install langchain-openai")

    try:
        from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
    except ImportError:
        print("LangChain SQL Toolkit is not installed.")
        print("Please install it using: pip install langchain-community")

    try:
        from langchain_community.agent_toolkits.sql.base import create_sql_agent
    except ImportError:
        print("LangChain SQL Agent is not installed.")
        print("Please install it using: pip install langchain-community")

    try:
        import numpy

    except ImportError:
        print("NumPy is not installed.")
        print("Please install it using: pip install numpy")

if __name__ == "__main__":
    test_imports()
    print("All libraries are installed correctly.")