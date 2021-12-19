import requests
import pandas as pd
import logging
import boto3
from dotenv import load_dotenv
from os import getenv
from abc import ABC
from datetime import datetime
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

load_dotenv("/opt/airflow/outputs/.env")


class AWS_Airflow(ABC):
    def __init__(self, wallet: str) -> None:
        self.wallet = wallet
        self.url = "https://www.fundsexplorer.com.br/ranking"
        self.headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
            "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        }
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=getenv("AWS_ID"),
            aws_secret_access_key=getenv("AWS_KEY"),
        )
        self.s3_resource = boto3.resource(
            "s3",
            aws_access_key_id=getenv("AWS_ID"),
            aws_secret_access_key=getenv("AWS_KEY"),
        )

    def _validate_bucket(self) -> bool:
        try:
            self.s3_client.list_buckets()["Buckets"][0]["Name"]
        except IndexError:
            print("There is no bucket")
            return True
        return False

    def _create_bucket(self, name) -> bool:
        try:
            self.s3_client.create_bucket(Bucket=name)
        except ClientError as e:
            logging.error(e)
            return False
        return True


class FundsExplorer(AWS_Airflow):
    def collect_data(self) -> pd.DataFrame:
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            try:
                df = pd.read_html(response.content, encoding="utf-8")[0]
                df.insert(
                    0, "Data", datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M")
                )
                df = df[(df["Códigodo fundo"].isin(self.wallet))]
                df.to_csv("/opt/airflow/outputs/fundos.csv", sep=";", index=False)
            except Exception as e:
                print(e)

    def start_bucket(self) -> None:
        if self._validate_bucket():
            self._create_bucket("kay-s3-bucket-fii")
            print("bucket created successfully: kay-s3-bucket-fii")
        else:
            name = self.s3_client.list_buckets()["Buckets"][0]["Name"]
            print(f"bucket already created: {name}")

    def send_files_s3(self) -> None:
        data_proc = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.s3_resource.Bucket("kay-s3-bucket-fii").upload_file(
            "/opt/airflow/outputs/fundos.csv",
            f"airflow/fundos/input/fundos_{data_proc}.csv",
        )
