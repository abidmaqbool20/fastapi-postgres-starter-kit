from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.role_schema import RoleCreate, RoleRead, RoleBase  
from app.services.role_service import RoleService 
from app.models.role import Role  

class RoleController:
    def __init__(self):
        self.service = RoleService()

    def create_role(self, role_data: RoleCreate, db: Session):
        try:
            return self.service.create_role(db, role_data)
        except ValueError as e:
            raise Exception(str(e))
    
    def get_role_by_id(self, role_id: int, db: Session):
        try:
            return self.service.get_role_by_id(db, role_id)
        except ValueError as e:
            raise Exception(str(e)) 

    def get_all_roles(self, db: Session):
        try:
            return self.service.get_all_roles(db)
        except ValueError as e:
            raise Exception(str(e)) 