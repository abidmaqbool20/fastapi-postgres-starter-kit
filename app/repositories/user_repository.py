from sqlalchemy.orm import Session, joinedload
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.utils.security import hash_password

class UserRepository:
    def create_user(self, db: Session, user_data: UserCreate) -> User:
        user = User(
            name=user_data.name,
            email=user_data.email,
            password=hash_password(user_data.password)
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_user_by_email(self, db: Session, email: str):
        return (
            db.query(User)
            .options(joinedload(User.roles))  # Eagerly load roles
            .filter(User.email == email)
            .first()
        )
