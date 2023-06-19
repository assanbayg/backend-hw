from fastapi import Depends, Response, status
from fastapi.responses import JSONResponse

from pydantic import Field
from typing import Any
from app.utils import AppModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class UserShanyraksFavorites(AppModel):
    id: Any = Field(alias="_id")
    address: str


class Favorites(AppModel):
    shanyraks: list[UserShanyraksFavorites]


@router.post(
    "/auth/users/favorites/shanyraks/{shanyrak_id:str}",
    status_code=status.HTTP_200_OK,
)
def make_favorite(
    shanyrak_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> Response:
    svc.repository.make_favorite(jwt_data.user_id, shanyrak_id)
    return Response(status_code=status.HTTP_200_OK)


@router.delete(
    "/auth/users/favorites/shanyraks/{shanyrak_id:str}",
    status_code=status.HTTP_200_OK,
)
def delete_user_likes(
    shanyrak_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> Response:
    svc.repository.delete_user_like(jwt_data.user_id, shanyrak_id)
    return Response(status_code=status.HTTP_200_OK)


@router.get(
    "/auth/users/favorites/shanyraks",
    status_code=status.HTTP_200_OK,
    response_model=Favorites,
)
def get_user_likes(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> Response:
    result = svc.repository.get_shanyraks_by_id(jwt_data.user_id)
    return Favorites(shanyraks=result)
