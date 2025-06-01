from app.models.role import Role
from app.config.database import Base
from sqlalchemy.orm import Session

def seed_roles(db: Session): 
    if db.query(Role).count() == 0:
        roles = [
            Role(name="Admin"),
            Role(name="User"),
            Role(name="Member"), 
        ] 
        db.add_all(roles)
        db.commit()
        print("✅ Seeded roles.")
    else:
        print("ℹ️ Roles already seeded.")
