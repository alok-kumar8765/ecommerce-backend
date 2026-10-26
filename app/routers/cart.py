from fastapi import APIRouter
from app.schemas import CartItemAdd
from app.models.database import fake_db

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.get("/")
def get_cart():
    return fake_db["cart"]

@router.post("/")
def add_to_cart(item: CartItemAdd):
    fake_db["cart"].append(item.model_dump())
    return {"message": "Item added to cart successfully", "item": item}