from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Explode Array Columns") \
    .getOrCreate()

# Sample data
data = [
    (1, "John", "Doe", 101, ["cricket", "hockey", "kabbadi"]),
    (2, "Jane", "Smith", 102, ["volleyball", "hockey"])
]

# create a DataFrame
df = spark.createDataFrame(data, ["id", "first_name", "last_name", "dept_id", "sports"])

explode_df = df.withColumn("sport", explode(col("sports"))).drop("sports")