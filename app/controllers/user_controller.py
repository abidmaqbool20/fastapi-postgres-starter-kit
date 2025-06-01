from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user_schema import UserCreate 
from app.schemas.auth_schema import UserLogin, Token
from app.services.user_service import UserService
from app.utils.security import verify_password
from app.auth.index import create_access_token 
from app.models.user import User  

class UserController:
    def __init__(self):
        self.service = UserService()

    def create_user(self, user_data: UserCreate, db: Session):
        try:
            return self.service.create_user(db, user_data)
        except ValueError as e:
            raise Exception(str(e))

    def login(self, user_login: UserLogin, db: Session):
        user = db.query(User).filter(User.email == user_login.username).first()
        if not user or not verify_password(user_login.password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        access_token = create_access_token(data={
            "sub": str(user.id),
            "id": user.id,
            "name": user.name,
            "email": user.email,
            # "role": user.role.name if user.role else "user"  # adjust as needed
        })

        return {"access_token": access_token, "token_type": "bearer"}
    
    
    def get_user_by_id(self, user_id: int, db: Session):
        return db.query(User).filter(User.id == user_id).first()
    

    def get_all_users(self, db: Session):
        return db.query(User).all()