from datetime import datetime

from bson.objectid import ObjectId
from pymongo.database import Database

from ..utils.security import hash_password


class AuthRepository:
    def __init__(self, database: Database):
        self.database = database

    def get_favorites(self, user_id: str):
        user = self.database["users"].find_one({"_id": ObjectId(user_id)})
        return user["favorites"] if "favorites" in user else []

    def make_favorite(self, user_id: str, shanyrak_id: str):
        favorites = self.get_favorites(user_id)
        if shanyrak_id not in favorites:
            favorites.append(shanyrak_id)

        self.database["users"].update_one(
            filter={"_id": ObjectId(user_id)},
            update={"$set": {"favorites": favorites}},
        )

    def create_user(self, user: dict):
        payload = {
            "email": user["email"],
            "password": hash_password(user["password"]),
            "created_at": datetime.utcnow(),
        }

        self.database["users"].insert_one(payload)

    def get_user_by_id(self, user_id: str) -> dict | None:
        user = self.database["users"].find_one(
            {
                "_id": ObjectId(user_id),
            }
        )
        return user

    def get_user_by_email(self, email: str) -> dict | None:
        user = self.database["users"].find_one(
            {
                "email": email,
            }
        )
        return user

    def update_user_by_id(self, user_id: str, data: dict):
        self.database["users"].update_one(
            filter={"_id": ObjectId(user_id)},
            update={
                "$set": {
                    "phone": data["phone"],
                    "name": data["name"],
                    "city": data["city"],
                }
            },
        )
