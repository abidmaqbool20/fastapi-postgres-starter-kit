from sqlalchemy.orm import Session
from schemas.user_schema import UserCreate
from services.user_service import UserService

class UserController:
    def __init__(self):
        self.service = UserService()

    def create_user(self, user_data: UserCreate, db: Session):
        try:
            return self.service.create_user(db, user_data)
        except ValueError as e:
            raise Exception(str(e))
