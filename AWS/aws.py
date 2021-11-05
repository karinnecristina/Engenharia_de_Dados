# ==============================================
#                 Libraries
# ==============================================
import boto3
import logging
from botocore.exceptions import ClientError
from dotenv import load_dotenv
from os import getenv

load_dotenv("/home/karinne/.env")

# ==============================================
#                  Settings
# ==============================================


s3_client = boto3.client(
    "s3", aws_access_key_id=getenv("AWS_ID"), aws_secret_access_key=getenv("AWS_KEY")
)


def create_bucket(name):
    try:
        s3_client.create_bucket(Bucket=name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


# ==============================================
# Creating the zones
# ==============================================


create_bucket("bucket-landing")
create_bucket("bucket-processing")
create_bucket("bucket-curated")
