from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.operators.email_operator import EmailOperator
from fii_dag.collect_fii import FundsExplorer

collect_fii = FundsExplorer(
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
    ]
)


args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    dag_id="fundos_imobiliarios",
    default_args=args,
    schedule_interval="38 23 * * *",
    start_date=datetime(2021, 12, 17),
)

extract_task = PythonOperator(
    task_id="coletar_dados",
    python_callable=collect_fii.collect_data,
    do_xcom_push=False,
    dag=dag,
)

bucket_task = PythonOperator(
    task_id="iniciar_bucket",
    python_callable=collect_fii.start_bucket,
    do_xcom_push=False,
    dag=dag,
)

load_task = PythonOperator(
    task_id="carregar_dados_s3",
    email_on_failure=True,
    email="teste@gmail.com",
    python_callable=collect_fii.send_files_s3,
    do_xcom_push=False,
    dag=dag,
)

email_task = EmailOperator(
    task_id="enviar_email",
    to="teste@gmail.com",
    subject="Pipeline finalizado",
    html_content="<p> Os dados forma carregados no bucket com sucesso! <p>",
)

extract_task >> bucket_task >> load_task >> email_task
