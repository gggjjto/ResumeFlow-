"""用户相关的 Pydantic 模型定义"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """用户基本信息"""

    email: EmailStr
    username: str


class UserCreate(UserBase):
    """用户注册信息"""

    password: str


class UserLogin(BaseModel):
    """用户登录信息"""

    login: str  # 可以是邮箱或用户名
    password: str


class PasswordReset(BaseModel):
    """密码重置信息"""

    email: EmailStr
    old_password: str
    new_password: str


class UserResponse(UserBase):
    """用户响应信息"""

    id: int
    created_at: datetime

    class Config:
        """配置类"""

        from_attributes = True


class UserUpdate(BaseModel):
    username: Optional[str] = None
    phone: Optional[str] = None
    avatar: Optional[str] = None


class UserDetail(UserResponse):
    phone: Optional[str] = None
    avatar: Optional[str] = None
    role: str
    is_active: bool
