from fastapi import APIRouter
from app.schemas import PaymentCreate
from app.models.database import fake_db

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.get("/")
def get_payments():
    return fake_db["payments"]

@router.post("/")
def process_payment(payment: PaymentCreate):
    new_id = len(fake_db["payments"]) + 1
    new_payment = {"id": new_id, **payment.model_dump()}
    fake_db["payments"].append(new_payment)
    return {"message": "Payment processed successfully", "payment": new_payment}