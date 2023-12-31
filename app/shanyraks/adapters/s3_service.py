from typing import BinaryIO
from dotenv import load_dotenv

import boto3
import os

load_dotenv()


class S3Service:
    def __init__(self):
        self.s3 = boto3.client(
            "s3",
            # aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
            # aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
        )

    def upload_file(self, file: BinaryIO, filename: str):
        bucket = "asanbayg-bucket"
        filekey = f"{filename}"

        self.s3.upload_fileobj(file, bucket, filekey)

        bucket_location = boto3.client("s3").get_bucket_location(Bucket=bucket)
        object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
            bucket_location["LocationConstraint"], bucket, filekey
        )

        return object_url

    def get_files(self):
        bucket = "asanbayg-bucket"
        response = self.s3.list_objects_v2(Bucket=bucket)
        print(response)
