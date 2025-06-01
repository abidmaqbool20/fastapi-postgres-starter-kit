# seeders/users.py
from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.security import hash_password



def seed_users(db: Session):
    if db.query(User).count() == 0:
        users = [
            User(name="Admin", email="admin@demo.com", password=hash_password("12345")),
            User(name="User", email="user@demo.com", password=hash_password("12345")),
            User(name="Member", email="member@demo.com", password=hash_password("12345")),
        ]
        db.add_all(users)
        db.commit()
        print("✅ Seeded users.")
    else:
        print("ℹ️ Users already seeded.")
