from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Optional

from . import models, schemas, crud
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Products
@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.get("/products/", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@app.get("/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Categories
@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@app.get("/categories/", response_model=list[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_categories(db, skip=skip, limit=limit)

# Inventory
@app.get("/inventory/", response_model=list[schemas.Inventory])
def read_inventory(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_inventory(db, skip=skip, limit=limit)

@app.get("/inventory/low-stock", response_model=list[schemas.LowStockAlert])
def get_low_stock_items(threshold: int = 5, db: Session = Depends(get_db)):
    items = crud.get_low_stock_items(db, threshold)
    return [
        {
            "product_id": item.product_id,
            "product_name": crud.get_product(db, item.product_id).name,
            "current_quantity": item.quantity,
            "threshold": item.low_stock_threshold
        }
        for item in items
    ]

# Sales
@app.post("/sales/", response_model=schemas.Sale)
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    return crud.create_sale(db, sale)

@app.get("/sales/", response_model=list[schemas.Sale])
def read_sales(
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    product_id: Optional[int] = Query(None),
    category_id: Optional[int] = Query(None),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_sales(
        db,
        start_date=start_date,
        end_date=end_date,
        product_id=product_id,
        category_id=category_id,
        skip=skip,
        limit=limit
    )

@app.get("/sales/summary", response_model=schemas.SalesSummary)
def get_sales_summary(db: Session = Depends(get_db)):
    return crud.get_sales_summary(db)

@app.get("/sales/revenue/{period}", response_model=list[schemas.RevenueAnalysis])
def get_revenue_by_period(period: str, db: Session = Depends(get_db)):
    if period not in ["daily", "weekly", "monthly", "yearly"]:
        raise HTTPException(status_code=400, detail="Invalid period")
    data = crud.get_revenue_by_period(db, period)
    return [{"period": str(r.period), "total_revenue": r.total_revenue} for r in data]
