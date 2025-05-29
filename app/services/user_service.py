from sqlalchemy.orm import Session
from schemas.user_schema import UserCreate
from models.user import User
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def create_user(self, db: Session, user_data: UserCreate) -> User:
        existing = self.user_repo.get_user_by_email(db, user_data.email)
        if existing:
            raise ValueError("User with this email already exists.")
        return self.user_repo.create_user(db, user_data)
