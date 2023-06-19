from fastapi import Depends, status

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

from ..service import Service, get_service
from . import router


@router.post("/{id}/comments")
def create_comment(
    shanyrak_id: str,
    content: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    svc.comment_repository.create_comment(
        shanyrak_id=shanyrak_id,
        payload={
            "content": content,
            "author_id": jwt_data.user_id,
        },
    )
    return status.HTTP_200_OK
