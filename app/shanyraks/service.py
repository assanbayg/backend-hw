from pydantic import BaseSettings

from app.config import database

from .adapters.s3_service import S3Service
from .adapters.here_service import HereService
from .repository.repository import ShanyrakRepository


class Config(BaseSettings):
    HERE_API_KEY: str


class Service:
    def __init__(self):
        config = Config()
        self.repository = ShanyrakRepository(database)
        self.s3_service = S3Service()
        self.here_service = HereService()


def get_service():
    repository = ShanyrakRepository(database)

    svc = Service(repository)
    return svc
