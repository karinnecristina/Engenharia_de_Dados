"""
Author: Karinne Cristina
Linkedin: https://www.linkedin.com/in/karinnecristinapereira/
"""

# =======================================
#  Connection of pyspark with postgresql
# =======================================

import os
from pyspark.sql import SparkSession

# Folders and Subfolders
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
JARS_DIR = os.path.join(BASE_DIR, "jars")


# Starting spark
spark = (
    SparkSession.builder.appName("pyspark_postgres")
    .config("spark.jars", os.path.join(JARS_DIR, "postgresql-42.3.1.jar"))
    .getOrCreate()
)

# Configuration files
config_file = {
    "url": "jdbc:postgresql:vendas",
    "driver": "org.postgresql.Driver",
    "dbtable": "Clientes",
    "user": "root",
    "password": "root",
}

# Database reading
df = spark.read.format("jdbc").options(**config_file).load()

# Viewing the data
df.show()
