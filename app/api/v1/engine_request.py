from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from app.schemas.engine_request_schema import (
    EngineRequestCreate,
    EngineRequestRead
)
from app.config.database import get_db
from app.controllers.engine_request_controller import EngineRequestController
from app.auth.index import get_current_user
from app.utils.rate_limiter import limiter

router = APIRouter()


@router.post("/", response_model=EngineRequestRead)
@limiter.limit("5/minute")
def create_engine_request(
    request: Request,
    engine_request: EngineRequestCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return EngineRequestController().create_engine_request(engine_request, db, current_user)


@router.get("/{request_id}", response_model=EngineRequestRead)
@limiter.limit("5/minute")
def get_engine_request_by_id(
    request: Request,
    request_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    result = EngineRequestController().get_engine_request_by_id(request_id, db)
    if not result:
        raise HTTPException(status_code=404, detail="EngineRequest not found")
    return result


@router.get("/", response_model=List[EngineRequestRead])
@limiter.limit("5/minute")
def get_all_engine_requests(
    request: Request,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return EngineRequestController().get_all_engine_requests(db, current_user)
