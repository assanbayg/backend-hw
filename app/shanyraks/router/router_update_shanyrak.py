from fastapi import Depends, Response
from pydantic import BaseModel
from app.utils import AppModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class UpdateShanyrakRequest(BaseModel):
    type: str
    price: int
    description: str
    address: str
    area: int
    rooms_count: int


@router.patch("/{id:str}")
def update_shanyrak_by_id(
    id: str,
    data: UpdateShanyrakRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict:
    user_id = jwt_data.user_id
    result = svc.repository.update_shanyrak_by_id(id, user_id, data.dict())
    if result.modified_count == 1:
        return Response(status_code=200)

    return Response(status_code=404)
