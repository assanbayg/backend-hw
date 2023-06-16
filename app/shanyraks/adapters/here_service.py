import os
import requests
from dotenv import load_dotenv

from fastapi import HTTPException


class HereService:
    def __init__(self):
        self.api_key = os.getenv("HERE_API_KEY")

    def get_coordinates(self, address):
        print(os.getenv("HERE_API_KEY"))
        url = f"https://geocode.search.hereapi.com/v1/geocode?q={address}&apiKey={self.api_key}"

        response = requests.get(url)
        json = response.json()

        if "items" in json and len(json["items"]) > 0:
            return {
                "latitude": json["items"][0]["position"]["lat"],
                "longitude": json["items"][0]["position"]["lng"],
            }
        else:
            raise HTTPException(status_code=404, detail="Address not found")
