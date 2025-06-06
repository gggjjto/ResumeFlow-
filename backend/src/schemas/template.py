from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class TemplateBase(BaseModel):
    name: str
    content: str
    template_id: Optional[UUID] = None
    tags: Optional[str] = None
    ai_vector: Optional[str] = None


class TemplateCreate(TemplateBase):
    pass


class TemplateUpdate(BaseModel):
    name: Optional[str] = None
    content: Optional[str] = None
    template_id: Optional[UUID] = None
    tags: Optional[str] = None
    ai_vector: Optional[str] = None


class TemplateResponse(TemplateBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True

    class Config:
        from_attributes = True
