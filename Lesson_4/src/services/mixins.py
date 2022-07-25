from sqlmodel import Session

from src.db import AbstractCache


class PostMixin:
    def __init__(self, cache: AbstractCache, session: Session):
        self.cache: AbstractCache = cache
        self.session: Session = session


class UserMixin:
    def __init__(self, cache: AbstractCache, session: Session):
        self.cache: AbstractCache = cache
        self.session: Session = session
