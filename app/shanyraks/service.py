from pydantic import BaseSettings

from app.config import database

from .adapters.s3_service import S3Service
from .adapters.here_service import HereService
from .repository.repository import ShanyrakRepository
from .repository.comments_repository import CommentRepository


class Service:
    def __init__(self):
        self.repository = ShanyrakRepository(database)
        self.comment_repository = CommentRepository(database)
        self.s3_service = S3Service()
        self.here_service = HereService()


def get_service():
    svc = Service()
    return svc
