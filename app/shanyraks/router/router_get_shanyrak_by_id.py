from typing import Any

from fastapi import Depends, HTTPException, status
from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router


class GetShanyrakResponse(AppModel):
    id: Any = Field(alias="_id")
    type: str
    price: int
    description: str
    address: str
    area: int
    rooms_count: int
    description: str


class GetShanyraksRequest(AppModel):
    id: str


@router.get("/{id:str}", response_model=GetShanyrakResponse)
def get_shanyrak_by_id(
    id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict:
    shanyrak = svc.repository.get_shanyrak_by_id(id)

    return shanyrak
