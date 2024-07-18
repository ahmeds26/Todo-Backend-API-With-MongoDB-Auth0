from pydantic import BaseModel, Field
from pydantic import EmailStr
from typing import Optional, Annotated, Union
from uuid import UUID, uuid4


class UserModel(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "username": "username",
                "email": "user@example.com",
                "password": "password"
            }
        }


