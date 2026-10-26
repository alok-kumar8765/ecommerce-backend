from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import UserCreate, UserResponse
from app.models.database import fake_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[UserResponse])
def get_users():
    return fake_db["users"]

@router.post("/", response_model=UserResponse)
def create_user(data: UserCreate):
    new_id = len(fake_db["users"]) + 1
    new_user = {"id": new_id, **data.model_dump()}
    fake_db["users"].append(new_user)
    return new_user