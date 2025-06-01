from sqlalchemy.orm import Session
from app.schemas.role_schema import RoleCreate,RoleRead
from app.models.role import Role
from app.repositories.role_repository import RoleRepository

class RoleService:
    def __init__(self):
        self.role_repo = RoleRepository()

    def create_role(self, db: Session, role_data: RoleCreate) -> Role:
        existing = self.role_repo.get_role_by_name(db, role_data.name)
        if existing:
            raise Exception("Role with this name already exists.")
        return self.role_repo.create_role(db, role_data)

    def get_role_by_id(self, db: Session, id: RoleRead) -> Role:
        return  self.role_repo.get_role_by_id(db, id)
    
    def get_all_roles(self, db: Session) -> Role:
        return  self.role_repo.get_all_roles(db)
        