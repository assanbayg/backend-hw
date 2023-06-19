from fastapi import Depends, Response, status
from typing import Any, List

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service

from . import router


class UpdateCommentRequest(AppModel):
    content: str


@router.patch("/{id:str}/comments/{comment_id:str}")
def update_comment(
    comment_id: str,
    content: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    svc.comment_repository.update_comment(
        comment_id=comment_id,
        new_content=content,
        user_id=jwt_data.user_id,
    )
    return status.HTTP_200_OK
