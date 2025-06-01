from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from datetime import datetime

class UserRole(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    assigned_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="user_roles")
    role = relationship("Role", back_populates="user_roles")
