import json
from functools import lru_cache
from typing import Optional

from fastapi import Depends
from sqlmodel import Session

from src.api.v1.schemas import UserCreate, UserModel, UserLogin, UserUpdate
from src.db import AbstractCache, get_cache, get_session
from src.models import User
from src.services import UserMixin

__all__ = ("UserService", )


class UserService(UserMixin):
    def create_user(self, user: UserCreate):
        new_user = User(username=user.username, password=user.password, email=user.email)
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user.dict()

    def login_user(self, user: UserLogin):
        pass