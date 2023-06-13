from datetime import datetime

from bson.objectid import ObjectId
from pymongo.database import Database


class ShanyrakRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_shanyrak(self, input: dict):
        payload = {
            "user_id": ObjectId(input["user_id"]),
            "type": input["type"],
            "price": input["price"],
            "address": input["address"],
            "area": input["area"],
            "rooms_count": input["rooms_count"],
            "description": input["description"],
            "created_at": datetime.utcnow(),
        }

        result = self.database["shanyraks"].insert_one(payload)
        created_shanyrak_id = str(result.inserted_id)
        return created_shanyrak_id

    def get_shanyrak_by_id(self, id: str) -> dict:
        shanyrak = self.database["shanyraks"].find_one(
            {
                "_id": ObjectId(id),
            }
        )
        return shanyrak
