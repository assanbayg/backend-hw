from bson.objectid import ObjectId
from pymongo.database import Database


class ShanyrakRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_shanyrak(self, data: dict):
        payload = {
            "user_id": ObjectId(data["user_id"]),
            "type": data["type"],
            "price": data["price"],
            "address": data["address"],
            "area": data["area"],
            "rooms_count": data["rooms_count"],
            "description": data["description"],
        }

        result = self.database["shanyraks"].insert_one(payload)
        created_shanyrak_id = str(result.inserted_id)
        return created_shanyrak_id

    def get_shanyrak_by_id(self, id: str) -> dict:
        return self.database["shanyraks"].find_one({"_id": ObjectId(id)})

    def update_shanyrak(self, id: str, user_id: str, data: dict):
        self.database["shanyraks"].update_one(
            filter={"_id": ObjectId(id), "user_id": ObjectId(user_id)},
            update={
                "$set": {
                    "type": data["type"],
                    "price": data["price"],
                    "address": data["address"],
                    "area": data["area"],
                    "rooms_count": data["rooms_count"],
                    "description": data["description"],
                }
            },
        )
