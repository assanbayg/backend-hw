from fastapi import Depends
from typing import Optional

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router


class CreateShanyrakRequest(AppModel):
    type: str
    price: int
    description: str
    address: str
    area: int
    rooms_count: int


class CreateShanyrakResponse(AppModel):
    id: Optional[str]


@router.post("/")
def create_shanyrak(
    data: CreateShanyrakRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> CreateShanyrakResponse:
    coordinates = svc.here_service.get_coordinates(data.address)
    location = {
        "latitude": coordinates.lat,
        "longitude": coordinates.lng,
    }
    created_shanyrak_id = svc.repository.create_shanyrak(
        {
            "user_id": jwt_data.user_id,
            "type": data.type,
            "price": data.price,
            "address": data.address,
            "area": data.area,
            "description": data.description,
            "rooms_count": data.rooms_count,
            "location": location,
        }
    )

    return CreateShanyrakResponse(id=created_shanyrak_id)


# {
#     "items": [
#         {
#             "title": "Алматы, Қазақстан",
#             "id": "here:cm:namedplace:23799358",
#             "resultType": "locality",
#             "localityType": "city",
#             "address": {
#                 "label": "Алматы, Қазақстан",
#                 "countryCode": "KAZ",
#                 "countryName": "Қазақстан",
#                 "county": "Алматы",
#                 "city": "Алматы",
#                 "postalCode": "050009",
#             },
#             "position": {"lat": 43.25066, "lng": 76.88814},
#             "mapView": {
#                 "west": 76.73774,
#                 "south": 43.03399,
#                 "east": 77.17164,
#                 "north": 43.40304,
#             },
#             "scoring": {"queryScore": 1.0, "fieldScore": {"city": 1.0}},
#         }
#     ]
# }
