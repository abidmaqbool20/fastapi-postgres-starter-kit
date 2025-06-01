from sqlalchemy.orm import Session
from app.models.role import Role
from app.schemas.role_schema import RoleCreate,RoleRead 

class RoleRepository:
    def create_role(self, db: Session, role_data: RoleCreate) -> Role:
        role = Role(
            name=role_data.name 
        )
        db.add(role)
        db.commit()
        db.refresh(role)
        return role

    def get_role_by_id(self, db: Session, id: int):
        return db.query(Role).filter(Role.id == id).first()
    
    def get_role_by_name(self, db: Session, name: str):
        return db.query(Role).filter(Role.name == name).first()
    
    def get_all_roles(self, db: Session):
        return db.query(Role).all()
