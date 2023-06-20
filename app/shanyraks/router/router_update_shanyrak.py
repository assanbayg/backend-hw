from fastapi import Depends, Response

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service

from . import router


class UpdateShanyrakRequest(AppModel):
    type: str
    price: float
    description: str
    address: str
    area: float
    rooms_count: int


@router.patch("/{id:str}")
def update_shanyrak(
    id: str,
    data: UpdateShanyrakRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    user_id = jwt_data.user_id
    result = svc.repository.update_shanyrak(id, user_id, data.dict())
    return Response(status_code=200)


# @router.post("/{id:str}/media")
# def update_shanyrak(
#     id: str,
#     files: List[UploadFile],
#     jwt_data: JWTData = Depends(parse_jwt_user_data),
#     svc: Service = Depends(get_service),
# ) -> Any:
#     media_urls = []
#     for file in files:
#         url = svc.repository.upload(file.file, file.filename)
#         media_urls.append(url)
#     update_result = svc.repository.update_shanyrak(id=id, user_id=jwt_data.user_id, data={"media": media_urls})
#     if update_result.acknowledged:
#         return media_urls
#     raise HTTPException(status_code=404, detail=f"Error occured while updating shanyrak {id}")
