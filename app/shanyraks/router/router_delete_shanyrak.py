from fastapi import Depends, Response

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

from ..service import Service, get_service

from . import router


@router.delete("/{id:str}")
def delete_shanyrak(
    id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    user_id = jwt_data.user_id
    result = svc.repository.delete_shanyrak(id, user_id)
    return Response(status_code=200)
