from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.database import Base
from app.models.user_role import UserRole  # <-- required for direct relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    
    user_roles = relationship(UserRole, back_populates="user")
    roles = relationship("Role", secondary="user_roles", viewonly=True)
