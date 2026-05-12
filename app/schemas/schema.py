


from typing import Required
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator


class Todo(BaseModel):
    todo_id: UUID = Field(default_factory=uuid4)
    content: str =  Field(
        min_length=3,
        max_length=200,
        description="Todo content"
    )
    completed: bool = False
    
    
    @field_validator("content")
    @classmethod
    def validate_content(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Content cannot be empty")

        banned_words = ["spam", "fake"]

        if any(word in value.lower() for word in banned_words):
            raise ValueError("Content contains banned words")

        return value