from typing import List, Optional

from fastapi import Depends

from app.utils import AppModel

from ..service import Service, get_service
from . import router


class Post(AppModel):
    id: str
    type: str
    price: float
    address: str
    area: float
    rooms_count: int
    location: dict


class GetPostsResponse(AppModel):
    total: int
    objects: List[Post]


@router.get(
    "?limit={limit}&offset={offset}&rooms_count={rooms_count}",
    response_model=GetPostsResponse,
)
def get_posts(
    limit: int,
    offset: int,
    type: Optional[str] = None,
    rooms_count: Optional[int] = None,
    price_from: Optional[float] = None,
    price_until: Optional[float] = None,
    svc: Service = Depends(get_service),
):
    result = svc.repository.get_posts(
        limit,
        offset,
        type,
        rooms_count,
        price_from,
        price_until,
    )
    return result
