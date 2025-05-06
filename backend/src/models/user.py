""" "定义用户模型类"""

import enum

from sqlalchemy import Boolean, Column, DateTime, Enum, Integer, String
from sqlalchemy.sql import func

from src.database import Base


class UserRole(enum.Enum):
    """用户角色枚举类"""
    NORMAL = "normal"
    PREMIUM = "premium"
    ADMIN = "admin"


class User(Base):
    """用户类"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    username = Column(String(50))
    hashed_password = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    role = Column(Enum(UserRole), default=UserRole.NORMAL)
    phone = Column(String(20))
    avatar = Column(String(200))
    is_active = Column(Boolean, default=True)
