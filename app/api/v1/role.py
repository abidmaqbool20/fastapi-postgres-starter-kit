from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.schemas.role_schema import RoleCreate, RoleRead
from app.config.database import get_db
from app.controllers.role_controller import RoleController
from app.auth.index import get_current_user

from app.utils.rate_limiter import limiter


router = APIRouter()


@router.post("/", response_model=RoleRead)
@limiter.limit("5/minute")
def create_role(request: Request,
    role: RoleCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return RoleController().create_role(role, db)


@router.get("/{role_id}", response_model=RoleRead)
@limiter.limit("5/minute")
def get_role_by_id(request: Request,
    role_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    role = RoleController().get_role_by_id(role_id, db)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.get("/", response_model=List[RoleRead])
@limiter.limit("5/minute")
def get_all_roles(request: Request,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return RoleController().get_all_roles(db)
