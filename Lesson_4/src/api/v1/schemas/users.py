from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field

__all__ = (
    "UserModel",
    "UserCreate",
    "UserLogin",
    "UserUpdate"
)


class UserName(BaseModel):
    username: str


class UserPassword(BaseModel):
    password: str = Field(min_length=5)


class UserEmail(BaseModel):
    email: EmailStr


# ----------------------------------------------
class UserLogin(UserName, UserPassword):
    ...


class UserCreate(UserLogin, UserEmail):
    ...


class UserModel(UserName, UserEmail):
    uuid: str
    created_at: datetime
    is_superuser: bool
    is_totp_enabled: bool
    is_active: bool


class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
