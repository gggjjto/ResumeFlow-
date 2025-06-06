from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class ResumeBase(BaseModel):
    content: Any
    template_id: Optional[UUID] = None
    status: Optional[str] = "draft"


class ResumeCreate(ResumeBase):
    pass


class ResumeUpdate(BaseModel):
    content: Optional[Any] = None
    template_id: Optional[UUID] = None
    status: Optional[str] = None


class ResumeResponse(ResumeBase):
    id: UUID
    user_id: UUID
    last_modified: datetime

    class Config:
        from_attributes = True
