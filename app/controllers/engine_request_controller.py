# app/controllers/engine_request_controller.py

from sqlalchemy.orm import Session
from app.schemas.engine_request_schema import EngineRequestCreate
from app.services.engine_request_service import EngineRequestService

class EngineRequestController:
    def __init__(self):
        self.service = EngineRequestService()

    def create_engine_request(self, data: EngineRequestCreate, db: Session, current_user: dict):
        try:
            print(current_user)
            return self.service.create_engine_request(db, data, current_user)
        except ValueError as e:
            raise Exception(str(e))

    def get_engine_request_by_id(self, request_id: int, db: Session):
        try:
            return self.service.get_engine_request_by_id(db, request_id)
        except ValueError as e:
            raise Exception(str(e))

    def get_all_engine_requests(self, db: Session, current_user: dict):
        try:
            return self.service.get_all_engine_requests(db, current_user)
        except ValueError as e:
            raise Exception(str(e))
        
    def get_engine_requests_by_user(self, db: Session, current_user: dict):
        try:
            return self.service.get_engine_requests_by_user(db, current_user)
        except ValueError as e:
            raise Exception(str(e))
