# =======================================
#             Bibliotecas
# =======================================
import os
import time
from dotenv import load_dotenv, find_dotenv
from os.path import abspath
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, when, month, year, concat_ws, isnan

# =======================================
#         Variáveis de Ambiente
# =======================================
load_dotenv(find_dotenv())
url = os.environ.get("url")
user = os.environ.get("user")
password = os.environ.get("password")

# =======================================
#             Aplicação
# =======================================

# Setup da aplicação Spark
spark = (
    SparkSession.builder.master("local[2]")
    .appName("Pipeline")
    .config("spark.sql.warehouse.dir", abspath("spark-warehouse"))
    .config("fs.s3a.endpoint", url)
    .config("fs.s3a.access.key", user)
    .config("fs.s3a.secret.key", password)
    .config("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    .config("fs.s3a.path.style.access", "True")
    .getOrCreate()
)

# Definindo o método de logging da aplicação [INFO ou ERROR]
spark.sparkContext.setLogLevel("ERROR")

# Lendo os dados do Data Lake
df = (
    spark.read.format("com.databricks.spark.csv")
    .option("header", "True")
    .option("inferSchema", "True")
    .csv("s3a://landing/Pakistan_Ecommerce.csv")
)

# Imprime os dados lidos da landing
print("\nAmostra dos dados na landing:")
print(df.show(5, truncate=False))
print("\nSchema do dataframe")
print(df.printSchema())

# Converte os dados da landing para o formato parquet
# e salva na área de processing


def convert_data(df: DataFrame, format: str, mode: str, save: str) -> DataFrame:
    """Convert the .csv file to .parquet"""
    print(f"\nEscrevendo os dados da landing como parquet na {save[6:16]} zone...\n")
    (df.write.format(format).mode(mode).save(save))
    return df


# Lendo arquivos parquet
def read_parquet(df: DataFrame, format: str, parquet: str) -> DataFrame:
    """Read the .parquet file"""
    df = spark.read.format(format).parquet(parquet)
    return df


def validation(
    df: DataFrame, date_column: list[str], id_column: list[str]
) -> DataFrame:
    """Validates data types and checks for missing values"""
    print("Iniciando a transformação dos dados....\n")
    time.sleep(2.5)

    for item in date_column:
        df = df.withColumn(item, df[item].cast("date"))
        if dict(df.dtypes)[item] == "string":
            raise TypeError(
                f'Erro: O tipo de dado da coluna "{item}" deve ser datetime64[ns].'
            )
        else:
            print(f'-> O tipo da coluna "{item}" foi convertida para datetime.')

    for id in id_column:
        if df.filter((df[id].isNull()) | (isnan(df[id]))).count() > 0:
            raise TypeError(f'Erro: A coluna "{id}" não pode conter valores nulos.')
        else:
            print(f'-> A coluna "{id}" não possui valores nulos.')
    return df


def clean(df: DataFrame, replaceCols: list[str]) -> DataFrame:
    """Replace or change incorrect characters and remove duplicate lines"""
    count_rows = df.count()
    df = df.dropDuplicates()

    if df.count() < count_rows:
        print(f"-> Foram removidas {count_rows - df.count()} linha(s) duplicada(s).")
    else:
        print("-> Não existe linhas duplicadas.")

    for cols in replaceCols:
        df = df.withColumn(
            cols,
            when((col(cols) == "#REF!") | (col(cols) == "***"), None).otherwise(
                col(cols)
            ),
        )
        print(f"-> Os valores incorretos da coluna {cols} foram substituídos por Null.")

    return df


def transformation(df: DataFrame, date: str) -> DataFrame:
    """Creating the month, year, and month_year columns"""
    df = df.withColumn("Year", year(df[date]).cast("string"))
    print('-> Criando a coluna "Year".')

    df = df.withColumn("Month", month(df[date]).cast("string"))
    print('-> Criando a coluna "Month".')

    df = df.withColumn("Customer_Since", concat_ws("-", col("Year"), col("Month")))
    print('-> Criando a coluna "Customer_Since".')
    return df


def save_data(df: DataFrame, format: str, mode: str, save: str) -> DataFrame:
    """Saved the data"""
    print(f"\nEscrevendo os dados da processing como parquet na {save[6:13]} zone...\n")
    (df.write.format(format).mode(mode).save(save))
    print("Os dados foram salvos com sucesso!\n")
    time.sleep(2.5)
    print("Amostra de dados na curated")
    print(df.show(5, truncate=False))
    return df
