import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta
from ingestors import FundsExplorer


ingestor = FundsExplorer(wallet=["HGCR11"])

args = {"owner": "airflow", "start_date": airflow.utils.dates.days_ago(0)}

dag = DAG(
    dag_id="fundos_imobiliarios",
    default_args=args,
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=60),
)

t1 = PythonOperator(task_id="get_data", python_callable=ingestor.get_data, dag=dag)

t1
