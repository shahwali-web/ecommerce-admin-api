# app/populate_db.py
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .models import Category, Product, Inventory, Sale, SaleItem
import random
from datetime import datetime, timedelta

def create_tables():
    """Create all database tables"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

def create_demo_data():
    create_tables()
    
    db = SessionLocal()
    
    try:
        print("Creating demo data...")
        
        if db.query(Category).count() == 0:
            categories = [
                Category(name="Electronics", description="Electronic devices"),
                Category(name="Clothing", description="Apparel and fashion"),
                Category(name="Home & Kitchen", description="Home appliances"),
                Category(name="Books", description="Books and stationery"),
                Category(name="Toys", description="Toys and games")
            ]
            db.add_all(categories)
            db.commit()
            print("Categories created")

        if db.query(Product).count() == 0:
            categories = db.query(Category).all()
            products = []
            for i in range(1, 21):
                category = random.choice(categories)
                products.append(Product(
                    name=f"Product {i}",
                    description=f"Description for Product {i}",
                    price=round(random.uniform(10, 500), 2),
                    category_id=category.id
                ))
            db.add_all(products)
            db.commit()
            print("Products created")

            for product in products:
                db.add(Inventory(
                    product_id=product.id,
                    quantity=random.randint(0, 50),
                    low_stock_threshold=5
                ))
            db.commit()
            print("Inventory created")


        if db.query(Sale).count() == 0:
            products = db.query(Product).all()
            for i in range(1, 101):
                sale_date = datetime.now() - timedelta(days=random.randint(0, 90))
                num_items = random.randint(1, 5)
                items = random.sample(products, num_items)
                
                total_amount = 0
                sale = Sale(
                    sale_date=sale_date,
                    total_amount=0,  # Will be updated
                    payment_method=random.choice(["Credit Card", "PayPal", "Cash"]),
                    customer_email=f"customer{i}@example.com"
                )
                db.add(sale)
                db.commit()
                
                for item in items:
                    quantity = random.randint(1, 3)
                    unit_price = item.price * (1 - random.uniform(0, 0.2))
                    total_price = round(unit_price * quantity, 2)
                    total_amount += total_price
                    
                    db.add(SaleItem(
                        sale_id=sale.id,
                        product_id=item.id,
                        quantity=quantity,
                        unit_price=unit_price,
                        total_price=total_price
                    ))
                
                sale.total_amount = round(total_amount, 2)
                db.commit()
            print("Sales created")

        print("Demo data population completed successfully!")
        
    except Exception as e:
        print(f"Error creating demo data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_demo_data()