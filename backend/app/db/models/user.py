from .base import Base
from sqlalchemy import Column, Integer, String, Sequence, DateTime
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=True)
    profile_image = Column(String(255), nullable=True)
    last_online = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
