import uuid

from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from src.database import Base


class Template(Base):
    __tablename__ = "templates"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    template_id = Column(UUID(as_uuid=True), nullable=True)
    tags = Column(String(255), nullable=True)
    ai_vector = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    tags = Column(String(255), nullable=True)
    ai_vector = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
