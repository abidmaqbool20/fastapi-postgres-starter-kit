# app/repositories/engine_request_repository.py

from sqlalchemy.orm import Session
from app.models.engine_request import EngineRequest
from app.schemas.engine_request_schema import EngineRequestCreate
from app.constants.enums import StatusEnum

class EngineRequestRepository:
    def create(self, db: Session, data: EngineRequestCreate, user_id: int) -> EngineRequest:
        new_request = EngineRequest(
            user_id=user_id,
            input_type=data.input_type,
            input_url=data.input_url,
            status=StatusEnum.pending
        )
        db.add(new_request)
        db.commit()
        db.refresh(new_request)
        return new_request

    def get_by_id(self, db: Session, request_id: int) -> EngineRequest:
        return db.query(EngineRequest).filter(EngineRequest.id == request_id).first()

    def get_all(self, db: Session): 
        return db.query(EngineRequest).all()
    
    def get_by_user(self, db: Session, user_id: int):
        return db.query(EngineRequest).filter(EngineRequest.user_id == user_id).all() 
