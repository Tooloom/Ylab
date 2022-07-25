from __future__ import annotations  # чтобы не ругался, что не объявлен класс, который ниже
from datetime import datetime
from typing import Optional, List  # пишут, что в новых версиях python есть list "из коробки"

from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Column, String

__all__ = ("Post", "User")


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(nullable=False)
    description: str = Field(nullable=False)
    views: int = Field(default=0)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    author_id: Optional[str] = Field(foreign_key="user.uuid", nullable=False)
    user: Optional[User] = Relationship(back_populates="posts")  # для поиска автора поста


class User(SQLModel, table=True):
    uuid: str = Field(default=None, primary_key=True)
    username: str = Field(sa_column=Column("username", String, unique=True, nullable=False, index=True))
    email: str = Field(nullable=False)
    hashed_password: str = Field(nullable=False)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    is_superuser: bool = Field(default=False)
    is_totp_enabled: bool = Field(default=False)
    is_active: bool = Field(default=True)
    posts: List[Post] = Relationship(back_populates="user")  # для поиска постов пользователя
