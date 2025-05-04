"""User management routes for registration, login, and profile management."""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.models.user import User

router = APIRouter()


class UserCreate(BaseModel):
    """Model for user registration and login."""

    username: str
    password: str
    email: str


class UserUpdate(BaseModel):
    """Model for updating user profile."""

    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None


@router.post("/register")
async def register(user: UserCreate):
    """Register a new user."""
    existing_user = await User.get_or_none(username=user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = await User.create(**user.dict())
    return {"id": new_user.id, "username": new_user.username}


@router.post("/login")
async def login(user: UserCreate):
    """Login an existing user."""
    existing_user = await User.get_or_none(username=user.username)
    if not existing_user or existing_user.password != user.password:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return {"message": "Login successful"}


@router.put("/update/{user_id}")
async def update_user(user_id: int, user: UserUpdate):
    """Update user profile."""
    existing_user = await User.get_or_none(id=user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    existing_user.username = user.username or existing_user.username
    existing_user.password = user.password or existing_user.password
    existing_user.email = user.email or existing_user.email
    await existing_user.save()
    return {"message": "User updated successfully"}


@router.get("/profile/{user_id}")
async def get_user_profile(user_id: int):
    """Get user profile by ID."""
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"username": user.username, "email": user.email, "profile": user.profile}
