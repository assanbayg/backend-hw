from fastapi import Depends, Response

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service

from . import router


class UpdateShanyrakRequest(AppModel):
    type: str
    price: int
    description: str
    address: str
    area: int
    rooms_count: int


@router.patch("/{id:str}")
def update_shanyrak(
    id: str,
    data: UpdateShanyrakRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    user_id = jwt_data.user_id
    result = svc.repository.update_shanyrak(id, user_id, data.dict())
    return Response(status_code=200)
