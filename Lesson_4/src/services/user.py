import json
from functools import lru_cache
from typing import Optional

from fastapi import Depends
from sqlmodel import Session

from src.api.v1.schemas import PostCreate, PostModel
from src.db import AbstractCache, get_cache, get_session
from src.models import Post
from src.services import UserMixin

__all__ = ("UserService", )


class UserService(UserMixin):
    pass
