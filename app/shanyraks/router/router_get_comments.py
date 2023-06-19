from typing import Any, List

from fastapi import Depends, HTTPException, status
from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router


class GetCommentsResponse(AppModel):
    id: Any = Field(alias="_id")
    content: str = ""
    created_at: str = ""
    author_id: str = ""


@router.get("/{id:str}/comments")
def get_commnets(
    shanyrak_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    comments = svc.comment_repository.get_comments(shanyrak_id)
    if comments:
        return [GetCommentsResponse(**comment) for comment in comments]
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comments are not found",
        )
