from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session 
from app.schemas.auth_schema import UserLogin, Token

from app.config.database import get_db
from app.controllers.user_controller import UserController

from app.utils.rate_limiter import limiter

router = APIRouter()


@router.post("/login", response_model=Token)
@limiter.limit("3/minute")
def login(request: Request, user_login: UserLogin, db: Session = Depends(get_db)):
    return UserController().login(user_login, db)
   
