import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta
from selenium_dag.ingestors import FundsExplorer


ingestor = FundsExplorer(
    [
        "HGCR11",
        "XPLG11",
        "KNRI11",
        "HGRU11",
        "TORD11",
        "VINO11",
        "IRDM11",
        "MXRF11",
        "MGFF11",
    ],
    "--disable-gpu",
    "--no-sandbox",
    "--headless",
)

args = {"owner": "airflow", "start_date": airflow.utils.dates.days_ago(0)}

dag = DAG(
    dag_id="fundos_imobiliarios",
    default_args=args,
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=60),
)

t1 = PythonOperator(
    task_id="access_website", python_callable=ingestor._access_website, dag=dag
)

t1
