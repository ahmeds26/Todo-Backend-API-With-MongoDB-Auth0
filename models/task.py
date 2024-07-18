from pydantic import BaseModel, Field
from pydantic import EmailStr
from datetime import date
from typing import Optional
from uuid import UUID, uuid4

class TaskModel(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    title: str = Field(...)
    description: str = Field(...)
    status: str = Field(...)
    due_date: date = Field(...)  # ISO 8601 format

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "title": "Building API endpoints",
                "description": "Creating register and login endpoints",
                "status": "complete",
                "due_date": "2024-07-14"
            }
        }

class UpdateTaskModel(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
    due_date: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Building API endpoints",
                "description": "Creating tasks endpoints",
                "status": "pending",
                "due_date": "2024-07-14"
            }
        }