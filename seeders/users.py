# seeders/users.py
from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.security import hash_password



def seed_users(db: Session):
    if db.query(User).count() == 0:
        users = [
            User(name="Admin User", email="admin@example.com", password=hash_password("admin123")),
            User(name="Normal User", email="user@example.com", password=hash_password("user123")),
        ]
        db.add_all(users)
        db.commit()
        print("✅ Seeded users.")
    else:
        print("ℹ️ Users already seeded.")
