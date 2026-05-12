from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import Boolean, Column, DateTime, String

from app.repositories.db import Base


class TodoSchema(Base):
    __tablename__ = "todos"
    todo_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, index=True)
    
    content = Column(String, nullable=False)

    is_completed = Column(Boolean, default=False)
    
    created_at = Column(DateTime, default=datetime.now(timezone.utc))