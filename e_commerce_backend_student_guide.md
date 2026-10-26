# 🎓 Student Guide: E-Commerce Backend System API

Welcome to the **E-Commerce Backend System** project! This repository is designed as a learning resource to help students understand how real-world backend APIs are constructed using **Python**, **FastAPI**, and modular architecture patterns.

---

## 📌 1. Project Objective: What Does This Project Do?

When you shop online on websites like Amazon or Flipkart, a few core actions happen behind the scenes:
1. **Catalog Browsing:** Browsing products, prices, and stock.
2. **User Profiles:** Managing user information.
3. **Shopping Cart:** Adding products to a temporary cart before checkout.
4. **Order Processing:** Converting items in a cart into a placed order.
5. **Payment Processing:** Tracking whether an order is paid or pending.

This project builds the **Backend Engine** for all those operations using RESTful APIs. It provides endpoints for creating and viewing products, managing users, adding items to a cart, creating orders, and recording payments.

---

## ⚡ 2. What is FastAPI and How Does It Work?

**FastAPI** is a modern, high-performance web framework for building APIs with Python based on standard Python type hints.

### Key Concepts:
* **Asynchronous Capabilities:** FastAPI is built on top of `Starlette` and `Pydantic`, allowing it to handle many requests concurrently with high performance.
* **Automatic Data Validation:** Using `Pydantic`, FastAPI automatically validates incoming request payloads (JSON data) against defined schemas. If a client sends string data for an integer field, FastAPI catches it and returns a clear error message.
* **Automatic Interactive Documentation:** FastAPI automatically generates interactive OpenAPI documentation (Swagger UI and ReDoc) directly from your code metadata and type annotations.

---

## 📁 3. Why is Folder Structure Important?

In small projects, putting all code in a single `main.py` file might seem easier. However, in production systems, this creates massive, unmaintainable files.

We use **Modular Project Architecture**:

```text
ecommerce_backend/
│
├── app/
│   ├── __init__.py          # Marks 'app' as a Python package
│   ├── main.py              # Application entry point & router registration
│   ├── schemas.py           # Data validation models (Pydantic)
│   ├── routers/             # API route handlers organized by feature
│   │   ├── __init__.py
│   │   ├── products.py      # Endpoints for /products
│   │   ├── users.py         # Endpoints for /users
│   │   ├── orders.py        # Endpoints for /orders
│   │   ├── cart.py          # Endpoints for /cart
│   │   └── payments.py      # Endpoints for /payments
│   └── models/              # Database models & database session setup
│       ├── __init__.py
│       └── database.py      # Database connection & mock database storage
│
└── requirements.txt         # Project dependencies list
```

### Benefits of this structure:
* **Separation of Concerns:** Each file has one specific job (e.g., schemas define structure, routers handle requests).
* **Scalability:** New features (e.g., reviews or wishlists) can be added as new files in `routers/` without touching existing routes.
* **Teamwork:** Multiple developers can work on different routers at the same time without code conflicts.

---

## 📄 4. Detailed File-by-File & Code Line Breakdown

---

### A. `app/main.py`
This is the **entry point** of the application. It instantiates the FastAPI instance and registers all feature routers.

#### Line Explanations:
* `from fastapi import FastAPI`: Imports the central `FastAPI` class.
* `from app.routers import products, users, orders, cart, payments`: Imports all modular router modules.
* `app = FastAPI(title="E-commerce Backend API")`: Creates the main application instance. The `title` argument sets the header display in the Swagger UI.
* `app.include_router(products.router)`: Mounts the products endpoints onto the main application.
* `@app.get("/")`: A route decorator defining a GET request at the root path (`/`).

---

### B. `app/schemas.py`
This file defines **Pydantic Models** that enforce incoming data structure (requests) and outgoing data structure (responses).

#### Code Example & Explanation:
```python
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int
    category: str

class ProductResponse(ProductCreate):
    id: int
```

* `class ProductCreate(BaseModel)`: Inheriting from `BaseModel` marks this as a Pydantic schema. Whenever a user submits JSON to create a product, FastAPI checks that `price` is a valid floating-point number, `stock` is an integer, etc.
* `class ProductResponse(ProductCreate)`: Inherits all fields from `ProductCreate` (`name`, `price`, `stock`, `category`) and adds `id: int` because the ID is generated server-side after creation.

---

### C. `app/models/database.py`
This file handles data storage setups. In full production, this contains SQLAlchemy engine definitions for MySQL/PostgreSQL. In our current setup, it contains mock database structures so the application runs without external database installation.

#### Key Code Components:
* `fake_db`: A Python dictionary simulating database tables using in-memory lists.
* `get_db()`: A generator function used for dependency injection (`Depends(get_db)`), ensuring each HTTP request gets its own database session context.

---

### D. `app/routers/products.py` (And Router Files)
Router files define the actual HTTP endpoints for each domain feature.

#### Deep Dive Code Line Explanations:

#### 1. Router Instantiation Line:
```python
router = APIRouter(prefix="/products", tags=["Products"])
```
* `router = APIRouter(...)`: Creates an isolated router instance to group related routes together instead of attaching them directly to `app`.
* `prefix="/products"`: prepends `/products` to all routes inside this file. So `@router.get("/")` automatically becomes accessible at `http://127.0.0.1:8000/products/`.
* `tags=["Products"]`: Groups all these endpoints under a clean, collapsible heading titled **"Products"** inside the Swagger UI (`/docs`).

---

#### 2. Route Handler Decorator Line:
```python
@router.post("/", response_model=ProductResponse)
def create_product(data: ProductCreate):
```
* `@router.post("/")`: A decorator defining that this function handles incoming **HTTP POST** requests to the root path of this router (`/products/`).
* `response_model=ProductResponse`: 
  * Specifies the Pydantic schema used to format and validate the **outgoing response payload**.
  * Filters out any extra sensitive internal variables not present in `ProductResponse`.
  * Ensures response data matches the documented structure in Swagger UI.
* `data: ProductCreate`: Tells FastAPI to read the incoming JSON request body, validate it against the `ProductCreate` schema, and pass it to the function as the `data` variable.

---

## 🧪 5. How to Test Your API

### Option A: Using Interactive Swagger UI (Browser)

1. Run your Uvicorn server in terminal:
   ```bash
   uvicorn app.main:app --reload
   ```
2. Open your web browser and navigate to:
   ```text
   http://127.0.0.1:8000/docs
   ```
3. Expand any section (e.g., **Products** -> **POST /products/**).
4. Click **"Try it out"**.
5. Fill in the JSON request body:
   ```json
   {
     "name": "Gaming Headphones",
     "price": 2999.0,
     "stock": 30,
     "category": "Electronics"
   }
   ```
6. Click **"Execute"**. Scroll down to see the **200 OK** response and the generated `id`.

---

### Option B: Using Postman

1. Download and launch [Postman](https://www.postman.com/downloads/).
2. Create a **New Request**.

#### Testing `GET /products/`:
* **Method:** `GET`
* **URL:** `http://127.0.0.1:8000/products/`
* Click **Send**. You should receive a `200 OK` status with a list of initial products.

#### Testing `POST /products/`:
* **Method:** `POST`
* **URL:** `http://127.0.0.1:8000/products/`
* Go to the **Headers** tab and set:
  * Key: `Content-Type` | Value: `application/json`
* Go to the **Body** tab, select **raw**, and set format to **JSON**.
* Paste payload:
  ```json
  {
    "name": "Mechanical Keyboard",
    "price": 4500.0,
    "stock": 12,
    "category": "Electronics"
  }
  ```
* Click **Send**. View the JSON response returning the created product with its `id`.

---

## 🚀 Summary Checklist for Students
* `main.py` combines everything.
* `schemas.py` validates incoming and outgoing JSON data.
* `routers/` handle distinct feature paths (`/products`, `/users`, `/cart`).
* `APIRouter(prefix=..., tags=...)` organizes endpoints into tidy URL groups.
* `response_model=...` enforces structured API output formatting.