from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from app.constants.enums import InputTypeEnum, StatusEnum


class EngineRequestBase(BaseModel): 
    input_type: InputTypeEnum  # Use enum instead of Literal
    input_url: str 


class EngineRequestCreate(EngineRequestBase):
    pass


class EngineRequestUpdate(BaseModel):
    result_json: Optional[dict] = None
    status: Optional[StatusEnum] = None  # Reuse the StatusEnum


class EngineRequestRead(EngineRequestBase):
    id: int
    user_id: int
    result_json: Optional[dict]
    status: StatusEnum  # Keep as enum, no need to convert to str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
