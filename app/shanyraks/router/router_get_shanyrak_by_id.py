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
    type: str = ""
    price: int = 0
    description: str = ""
    address: str = ""
    area: int = 0
    rooms_count: int = 0  # REMINDER: GET requeres data ((( it took me 1 hour to fix


@router.get("/{id:str}", response_model=GetShanyrakResponse)
def get_shanyrak_by_id(
    id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    return svc.repository.get_shanyrak_by_id(id)
