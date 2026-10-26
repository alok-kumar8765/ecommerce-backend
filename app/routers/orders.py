from fastapi import APIRouter
from app.schemas import OrderCreate
from app.models.database import fake_db

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/")
def get_orders():
    return fake_db["orders"]

@router.post("/")
def create_order(order: OrderCreate):
    new_id = len(fake_db["orders"]) + 1
    new_order = {"id": new_id, **order.model_dump(), "status": "Pending"}
    fake_db["orders"].append(new_order)
    return new_order