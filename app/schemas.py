from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# --- Category ---
class Category(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True

class CategoryCreate(BaseModel):
    name: str
    description: Optional[str] = None


# --- Product ---
class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    category_id: int

    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: int


# --- Inventory ---
class Inventory(BaseModel):
    product_id: int
    quantity: int
    low_stock_threshold: int = 5
    last_updated: datetime

    class Config:
        from_attributes = True


# --- Sales ---
class SaleItem(BaseModel):
    product_id: int
    quantity: int
    unit_price: float
    total_price: float

class Sale(BaseModel):
    id: int
    total_amount: float
    payment_method: Optional[str] = None
    customer_email: Optional[str] = None
    sale_date: datetime
    items: List[SaleItem] = []

    class Config:
        from_attributes = True

class SaleCreate(BaseModel):
    total_amount: float
    payment_method: Optional[str] = None
    customer_email: Optional[str] = None
    items: List[SaleItem]


# --- Reports ---
class RevenueAnalysis(BaseModel):
    period: str
    total_revenue: float
    comparison_percentage: Optional[float] = None

class SalesSummary(BaseModel):
    total_sales: int
    total_revenue: float
    average_order_value: float
    products_sold: int

class LowStockAlert(BaseModel):
    product_id: int
    product_name: str
    current_quantity: int
    threshold: int
