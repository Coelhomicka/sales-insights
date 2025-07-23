#  Sales Insights - FastAPI + LangChain + OpenAI

Este projeto é uma API que permite consultar insights de vendas a partir de uma base de dados relacional, utilizando linguagem natural. Foi desenvolvido como parte do processo seletivo para a vaga de Desenvolvedor Python com IA Generativa — The Garage.

---

##  Tecnologias utilizadas

- **FastAPI** – para a construção da API REST
- **SQLite** – banco de dados relacional
- **SQLAlchemy** – ORM para interagir com o banco
- **LangChain + OpenAI** – geração de respostas em linguagem natural baseadas em SQL
- **Uvicorn** – servidor de desenvolvimento
- **python-dotenv** – para gerenciamento de variáveis de ambiente

---

##  Estrutura do projeto

sales_insights/
│
├── main.py # Inicialização da API e rotas
├── crud.py # Lógica de extração do banco
├── database.py # Conexão com SQLite
├── utils.py # Integração com LangChain + OpenAI
├── sales.db # Base de dados SQLite com dados de exemplo
├── .env # Chave da OpenAI (não versionar)
└── requirements.txt # Dependências do projeto


---

##  Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com:

OPENAI_API_KEY=sua_chave_aqui


---

##  Como rodar o projeto localmente

```bash
# 1. Clone o repositório
git clone <url-do-repo>
cd sales_insights

# 2. Crie e ative um ambiente virtual
python -m venv env
source env/bin/activate  # Linux/macOS
.\env\Scripts\activate   # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Inicie o servidor
uvicorn main:app --reload

Acesse: http://127.0.0.1:8000/docs


🔍 Exemplos de uso
1. Top produtos

GET /top-products

2. Perguntas com linguagem natural

GET /sales-insights?question=Qual foi o produto mais vendido no último mês?


⚠️ Restrições e validações
Perguntas fora do escopo (como “quanto custa um macaco?”) são bloqueadas e recebem mensagem explicativa.

Apenas perguntas relacionadas a vendas, produtos ou clientes são permitidas.


👨‍💻 Desenvolvido por
Mickael Coelho 