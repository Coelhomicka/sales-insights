from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from models import Product, Sale

def get_top_products_last_month(db: Session, limit: int = 5):
    results = (
        db.query(
            Product.name,
            func.sum(Sale.quantity).label("total_sold")
        )
        .join(Sale, Product.id == Sale.product_id)
        # .filter(Sale.sale_date >= one_month_ago)  ← REMOVIDO TEMPORARIAMENTE
        .group_by(Product.name)
        .order_by(func.sum(Sale.quantity).desc())
        .limit(limit)
        .all()
    )
    return results
