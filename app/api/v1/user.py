from fastapi import APIRouter, Depends
from app.schemas.user_schema import UserCreate, UserRead
from config.database import get_db
from app.controllers.user_controller import UserController
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserController().create_user(user, db)
