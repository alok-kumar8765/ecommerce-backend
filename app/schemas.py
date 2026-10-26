from pydantic import BaseModel
from typing import Optional

# --- Product Schemas ---
class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int
    category: str

class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True


# --- User Schemas ---
class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True


# --- Cart Schemas ---
class CartItemAdd(BaseModel):
    product_id: int
    quantity: int


# --- Order Schemas ---
class OrderCreate(BaseModel):
    user_id: int
    total_amount: float


# --- Payment Schemas ---
class PaymentCreate(BaseModel):
    order_id: int
    amount: float
    status: str  # e.g., "Pending", "Completed", "Failed"