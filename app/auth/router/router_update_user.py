from fastapi import Depends, Response
from pydantic import BaseModel

from app.utils import AppModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class UpdateUserRequest(BaseModel):
    phone: str
    name: str
    city: str


class UpdateUserResponse(AppModel):
    phone: str
    name: str
    city: str


@router.patch("/users/me")
def update_user_by_id(
    input: UpdateUserRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    user_id = jwt_data.user_id

    svc.repository.update_user_by_id(user_id, input.dict())

    return Response(status_code=200)
