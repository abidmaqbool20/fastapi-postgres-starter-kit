from sqlalchemy.orm import Session
from app.models.user import User
from app.models.role import Role
from app.models.user_role import UserRole

def seed_user_roles(db: Session):
    # Fetch users by email (adjust as needed)
    user1 = db.query(User).filter(User.email == "admin@demo.com").first()
    user2 = db.query(User).filter(User.email == "user@demo.com").first()
    user3 = db.query(User).filter(User.email == "member@demo.com").first()
    
    # Fetch roles by name
    admin_role = db.query(Role).filter(Role.name == "Admin").first()
    user_role = db.query(Role).filter(Role.name == "User").first()
    member_role = db.query(Role).filter(Role.name == "Member").first()

    if not all([user1, user2, user3, admin_role, user_role, member_role]):
        print("Make sure users and roles exist before seeding user_roles.")
        return

    # Check if roles are already assigned to avoid duplicates
    existing_ur_admin = db.query(UserRole).filter_by(user_id=user1.id, role_id=admin_role.id).first()
    existing_ur_user = db.query(UserRole).filter_by(user_id=user2.id, role_id=user_role.id).first()
    existing_ur_member = db.query(UserRole).filter_by(user_id=user3.id, role_id=member_role.id).first()

    if not existing_ur_admin:
        user_role1 = UserRole(user_id=user1.id, role_id=admin_role.id)
        db.add(user_role1)

    if not existing_ur_user:
        user_role2 = UserRole(user_id=user2.id, role_id=user_role.id)
        db.add(user_role2)

    if not existing_ur_member:
        user_role3 = UserRole(user_id=user3.id, role_id=member_role.id)
        db.add(user_role3)

    db.commit()
    print("Seeded user_roles successfully.")

# Usage example, make sure you pass a db session to seed_user_roles
# from somewhere, like a script or a FastAPI dependency

if __name__ == "__main__":
    from app.config.database import SessionLocal
    db = SessionLocal()
    seed_user_roles(db)
    db.close()
