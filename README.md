# E-commerce Admin API

## Project Description
A complete backend API for an e-commerce management system with product catalog, inventory tracking, and sales analytics. Built with **FastAPI** and **PostgreSQL** for high performance and scalability.

## Key Features
- 🛒 **Product Management**: Full CRUD operations for products and categories
- 📦 **Inventory Control**: Real-time stock tracking with configurable low-stock alerts
- 💰 **Sales Processing**: Record transactions with automatic inventory updates
- 📊 **Revenue Analytics**: Daily, weekly, and monthly sales reporting
- 📈 **Data Visualization**: Built-in endpoints for generating business reports

## Technology Stack
- **Backend**: Python 3.9+ with FastAPI
- **Database**: PostgreSQL 14+ using SQLAlchemy ORM
- **Validation**: Pydantic
- **API Documentation**: Swagger UI & ReDoc (auto-generated)

## System Requirements
- Python 3.9+
- PostgreSQL 14+ (with admin access)
- pip (Python package installer)
- Git (optional)

---

## 🔧 Installation Guide

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/ecommerce-admin-api.git
cd ecommerce-admin-api
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create the Database
```bash
createdb ecommerce_admin
```

### 5. Environment Configuration
Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://postgres:PASSWORD@localhost/ecommerce_admin
```

### 6. Initialize Database with Seed Data
```bash
python -m app.populate_db
```

---

## ▶️ Running the Application
```bash
uvicorn app.main:app --reload
```

### API Documentation
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📌 Available Endpoints

### 🛍️ Products
- `GET /products/` – List all products (paginated)
- `POST /products/` – Create a new product
- `GET /products/{id}` – Get product details
- `PUT /products/{id}` – Update product
- `DELETE /products/{id}` – Delete product

### 📦 Inventory
- `GET /inventory/` – View current inventory
- `PATCH /inventory/{product_id}` – Update stock levels
- `GET /inventory/low-stock` – Low-stock warnings

### 💸 Sales
- `POST /sales/` – Record a new sale
- `GET /sales/` – List sales with optional date filters
- `GET /sales/revenue/daily` – Daily revenue
- `GET /sales/revenue/weekly` – Weekly trends

### 🗂️ Categories
- `GET /categories/` – List all categories
- `POST /categories/` – Create a new category

---

## 🗃️ Database Schema

### `products`
- `id`, `name`, `description`, `price`, `category_id`

### `categories`
- `id`, `name`, `description`

### `inventory`
- `product_id`, `quantity`, `low_stock_threshold`

### `sales`
- `id`, `sale_date`, `total_amount`, `payment_method`

### `sale_items`
- `id`, `sale_id`, `product_id`, `quantity`, `unit_price`
