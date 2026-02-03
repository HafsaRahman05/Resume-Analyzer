from fastapi import APIRouter
from app.models.user import User
from app.database import users_collection

router = APIRouter()


@router.post("/register")
def register_user(user: User):
    users_collection.insert_one(user.dict())
    return {"message": "User registered successfully"}
