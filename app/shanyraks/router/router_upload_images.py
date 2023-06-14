from typing import List
from fastapi import Depends, UploadFile

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

from ..service import Service, get_service
from . import router


@router.post("/{id}/media")
def upload_images(
    id: str,
    files: List[UploadFile],
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    result = []
    for file in files:
        result.append(svc.upload_image(file=file.file, filename=file.name))

    return {"message": result}
