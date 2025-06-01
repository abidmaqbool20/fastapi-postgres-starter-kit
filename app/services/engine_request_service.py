# app/services/engine_request_service.py

from sqlalchemy.orm import Session
from app.schemas.engine_request_schema import EngineRequestCreate
from app.repositories.engine_request_repository import EngineRequestRepository
from app.models.engine_request import EngineRequest

class EngineRequestService:
    def __init__(self):
        self.repository = EngineRequestRepository()

    def create_engine_request(self, db: Session, data: EngineRequestCreate, current_user: dict) -> EngineRequest:
        return self.repository.create(db, data, current_user["id"])

    def get_engine_request_by_id(self, db: Session, request_id: int) -> EngineRequest:
        result = self.repository.get_by_id(db, request_id)
        if not result:
            raise ValueError("EngineRequest not found")
        return result

    def get_all_engine_requests(self, db: Session, current_user: dict):
        return self.repository.get_all(db)
    
    def get_engine_requests_by_user(self, db: Session, current_user: dict):
        return self.repository.get_by_user(db, current_user["id"])
