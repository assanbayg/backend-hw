from datetime import datetime
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
            "location": data["location"],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        result = self.database["shanyraks"].insert_one(payload)
        created_shanyrak_id = str(result.inserted_id)
        return created_shanyrak_id

    def get_shanyrak_by_id(self, id: str) -> dict:
        return self.database["shanyraks"].find_one({"_id": ObjectId(id)})

    # def get_search(self, data: dict):
    #     query = {"rooms_count": {"$gt": data["rooms_count"]}}

    #     if "type" in data:
    #         query["type"] = data["type"]

    #     if "price_from" in data:
    #         query["price"] = {"$gte": data["price_from"]}

    #     if "price_until" in data:
    #         query.setdefault("price", {})
    #         query["price"]["$lte"] = data["price_until"]

    #     total_count = self.database["shanyraks"].count_documents(query)

    #     cursor = (
    #         self.database["shanyraks"]
    #         .find(query)
    #         .limit(query["limit"])
    #         .skip(query["offset"])
    #         .sort(query["created_at"])
    #     )
    #     result = []

    #     for item in cursor:
    #         result.append(item)

    #     return {
    #         "total": total_count,
    #         "objects": result,
    #     }

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

    def delete_shanyrak(self, id: str, user_id: str):
        self.database["shanyraks"].delete_one(
            filter={
                "_id": ObjectId(id),
                "user_id": ObjectId(user_id),
            }
        )

    def get_posts(
        self,
        limit: int,
        offset: int,
        type: str,
        rooms_count: int,
        price_from: float,
        price_until: float,
    ):
        query = {
            "type": type,
            "rooms_count": {"$eq": rooms_count},
            "price": {"$gte": price_from, "$lte": price_until},
        }

        print("QUERY", query)

        total_count = self.database["posts"].count_documents(query)

        cursor = (
            self.database["posts"]
            .find(query)
            .limit(limit)
            .skip(offset)
            .sort("created_at")
        )

        print("CURSOOOOOR", cursor)

        result = list(cursor)

        print("RESULT", result)

        return {"total": total_count, "objects": result}
