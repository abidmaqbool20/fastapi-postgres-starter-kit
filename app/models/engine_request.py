from sqlalchemy import Column, Integer, String, Enum, JSON, DateTime, ForeignKey
from datetime import datetime

from app.config.database import Base
from app.constants.enums import InputTypeEnum, StatusEnum  
  

class EngineRequest(Base):
    __tablename__ = "engine_requests"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    input_type = Column(Enum(InputTypeEnum, name="input_type_enum"), nullable=False)
    input_url = Column(String, nullable=False)
    result_json = Column(JSON, nullable=True)
    status = Column(Enum(StatusEnum, name="status_enum"), default=StatusEnum.pending)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
