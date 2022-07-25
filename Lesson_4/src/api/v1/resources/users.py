from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

from src.api.v1.schemas import UserModel, UserCreate, UserLogin, UserUpdate
from src.services import PostService, get_post_service

router = APIRouter()


@router.get(path="/users", summary="Registration", tags=["registration"])
def user_registration(user: UserModel):
    pass



