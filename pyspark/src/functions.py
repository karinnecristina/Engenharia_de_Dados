# =======================================
#             Bibliotecas
# =======================================
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace, when, upper, lower

# ==============================================
# Iniciando o Spark e lendo o conjunto de dados
# ==============================================

# Define a nossa aplicação Spark
spark = SparkSession.builder.appName("Pyspark_Commands").getOrCreate()

# Leitura do dataframe
df = (
    spark.read.format("csv")
    .option("inferSchema", "True")
    .option("header", "True")
    .load("raw/Employee_Salary_Dataset.csv")
)

# =======================================
#               Funções
# =======================================

# Imprime os datatypes das colunas do dataframe
df.printSchema()

# Número de linhas
df.count()

# Visualizando as 5 primeiras linhas
df.show(5)

# Visualizando estatísticas descritivas
df.describe()

# Valores únicos de uma determinada coluna
df.select("Salary").distinct()

# Ordenando o dataframe
df.orderBy(col("Age").desc())
df.orderBy(col("Experience_Years").asc(), col("Age").desc())

# Selecionando colunas
# Opção 1
df.select(col("Age"), col("Gender"))

# Opção 2
df.select("Age", "Gender")

# Renomeando uma coluna
df.withColumnRenamed("Age", "Idade")

# Mudando o tipo de uma coluna
df.withColumn("Salary", col("Salary").cast("double"))

# Substituindo os valores de uma coluna
df.withColumn("Gender", regexp_replace(col("Gender"), "Female", "F"))

df.withColumn("Gender", regexp_replace(col("Gender"), "Female", "F")).withColumn(
    "Gender", regexp_replace(col("Gender"), "Male", "M")
)

# Convertendo os valores de uma coluna para maiúsculo e minúsculo
# Lower (minúsculo)
df.select(col("Gender"), lower(col("Gender"))).withColumnRenamed(
    "lower(Gender)", "Lower"
)

# Upper (maiúsculo)
df.select(col("Gender"), upper(col("Gender"))).withColumnRenamed(
    "upper(Gender)", "Upper"
)

# Criando novas colunas
df = df.withColumn(
    "Age_Group",
    when(col("Age") < 19, "Young")
    .when((col("Age") >= 20) & (col("Age") <= 59), "Adult")
    .when(col("Age") >= 60, "Old"),
)

# Removendo uma ou mais colunas
df.drop("Experience_Years")
df.drop("Experience_Years", "ID")

# Filtrando valores
# Filter
df.filter(df.Salary > 40000)
df.filter((df.Salary > 40000) & (df.Gender == "Female"))

# Where
df.where(df.Salary > 40000)
df.where((df.Salary > 40000) & (df.Gender == "Female"))

# Select e Where
df.select(df.Age, df.Gender, df.Salary).where(df.Salary > 400000)

# GroupBy
# Somatória do salário por sexo
df.groupBy("Gender").sum("Salary").withColumnRenamed("sum(Salary)", "Sum")

# Média de salário por faixa etária
df.groupBy("Age_Group").mean("Salary").withColumnRenamed("mean(Salary)", "Mean")
