"""
Author: Karinne Cristina
Linkedin: https://www.linkedin.com/in/karinnecristinapereira/
"""

# =======================================
#  Connection of pyspark with mongodb
# =======================================

from pyspark.sql import SparkSession

# Starting spark
spark = (
    SparkSession.builder.appName("pyspark_mongodb")
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1")
    .getOrCreate()
)

# Configuration files
config_file = {"uri": "mongodb://127.0.0.1/posts.post"}

# Database reading
df = spark.read.format("mongo").options(**config_file).load()

# Viewing the data
df.show()
