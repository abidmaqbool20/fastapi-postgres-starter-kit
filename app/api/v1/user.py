from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.schemas.user_schema import UserCreate, UserRead
from app.config.database import get_db
from app.controllers.user_controller import UserController
from app.auth.index import get_current_user

from app.utils.rate_limiter import limiter


router = APIRouter()


@router.post("/", response_model=UserRead)
@limiter.limit("5/minute")
def create_user(request: Request,
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return UserController().create_user(user, db)


@router.get("/{user_id}", response_model=UserRead)
@limiter.limit("2/minute")
def get_user_by_id(request: Request,
    user_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    user = UserController().get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=List[UserRead])
@limiter.limit("5/minute")
def get_all_users(request: Request,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return UserController().get_all_users(db)
