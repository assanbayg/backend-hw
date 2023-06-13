from bson.objectid import ObjectId
from pymongo.database import Database
from pymongo.results import UpdateResult


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
        }

        result = self.database["shanyraks"].insert_one(payload)
        created_shanyrak_id = str(result.inserted_id)
        return created_shanyrak_id

    def get_shanyrak_by_id(self, id: str) -> dict:
        shanyrak = self.database["shanyraks"].find_one({"_id": ObjectId(id)})
        return shanyrak

    def update_shanyrak(
        self,
        id: str,
        user_id: str,
        data: dict,
    ) -> UpdateResult:
        return self.database["shanyraks"].update_one(
            filter={"_id": ObjectId(id), "user_id": ObjectId(user_id)},
            update={"$set": data},
        )
