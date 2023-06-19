from fastapi import Depends, status

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

from ..service import Service, get_service

from . import router


@router.delete("/{id:str}/comments/{comment_id:str}")
def delete_comment(
    comment_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    user_id = jwt_data.user_id
    result = svc.comment_repository.delete_comment(
        comment_id=comment_id, user_id=user_id
    )
    return status.HTTP_200_OK
