from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import get_top_products_last_month
from utils import ask_sales_question  # << aqui

app = FastAPI(title="Sales Insights API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/top-products")
def top_products(db: Session = Depends(get_db)):
    products = get_top_products_last_month(db)
    return {"top_products": [{"product": name, "quantity_sold": qty} for name, qty in products]}

@app.get("/sales-insights")
def sales_insights(question: str = Query(..., description="Sua pergunta sobre vendas.")):
    response = ask_sales_question(question)
    return {"answer": response}
