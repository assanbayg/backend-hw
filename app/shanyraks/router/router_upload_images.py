from fastapi import Depends, UploadFile, status
from typing import List

from ..service import Service, get_service
from . import router


@router.post("/{id:str}/media")
def upload_files(
    id: str,
    files: List[UploadFile],
    svc: Service = Depends(get_service),
):
    result = []
    for file in files:
        url = svc.s3_service.upload_file(file=file.file, filename=file.filename)
        result.append(url)

    return status.HTTP_200_OK
