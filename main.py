from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Define connection details
jdbc_url = "jdbc:postgresql://localhost:5432/follow-de-roadmap"
connection_properties = {"user": "postgres", "password": "1234"}

# Create SparkSession
spark = SparkSession.builder \
        .appName("Follow DE Roadmap") \
        .config("spark.jars", "postgresql-42.7.2.jar") \
        .config("spark.driver.extraClassPath", "postgresql-42.7.2.jar") \
        .getOrCreate()

# Define schema for the CSV data (replace with your actual schema)
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("Age", IntegerType(), True),
    StructField("Sex", StringType(), True),
    StructField("Job", IntegerType(), True),
    StructField("Housing", StringType(), True),
    StructField("Saving accounts", StringType(), True),
    StructField("Checking account", StringType(), True),
    StructField("Credit amount", IntegerType(), True),
    StructField("Duration", IntegerType(), True),
    StructField("Purpose", StringType(), True)
])

# Read CSV data with schema
df = spark.read.csv("./dataset/german_credit_risk_data.csv", header=True, schema=schema)

# Name index column to id
df.show()

# Write data into postgresql
df.write.jdbc(url=jdbc_url, properties=connection_properties, table="public.german_credit_risk", mode="append")

# Query to check result 
df2 = spark.read \
        .format("jdbc") \
        .option("driver", "org.postgresql.Driver") \
        .option("url", jdbc_url) \
        .option("user", "postgres") \
        .option("password", 1234) \
        .option("dbtable", "public.german_credit_risk").load()

df2.show()

# Stop SparkSession
spark.stop()
