#from fastapi import AProuter, HTTPException, Depends
from typing import List
from app.schemas import ProductCreate, ProductResponse
from app.models.database import fake_db
from fastapi import APIRouter, HTTPException, Depends

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[ProductResponse])
def get_products():
    return fake_db["products"]

@router.post("/", response_model=ProductResponse)
def create_product(data: ProductCreate):
    new_id = len(fake_db["products"]) + 1
    new_product = {"id": new_id, **data.model_dump()}
    fake_db["products"].append(new_product)
    return new_product

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    prod = next((p for p in fake_db["products"] if p["id"] == product_id), None)
    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    return prod