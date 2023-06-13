from fastapi import Depends
from typing import Optional

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router


class CreateShanyrakRequest(AppModel):
    type: str
    price: int
    description: str
    address: str
    area: int
    rooms_count: int
    description: str


class CreateShanyrakResponse(AppModel):
    id: Optional[str]


@router.post("/")
def create_shanyrak(
    input: CreateShanyrakRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> CreateShanyrakResponse:
    user_id = jwt_data.user_id
    created_shanyrak_id = svc.repository.create_shanyrak(
        {
            "user_id": user_id,
            "type": input.type,
            "price": input.price,
            "address": input.address,
            "area": input.area,
            "description": input.description,
            "rooms_count": input.rooms_count,
        }
    )

    return CreateShanyrakResponse(id=created_shanyrak_id)
