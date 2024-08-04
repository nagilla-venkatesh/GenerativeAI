from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("example").getOrCreate()

data = [(1,), (2,), (4,), (5,), (7,), (8,), (10,)]
df = spark.createDataFrame(data, ["Number"])

# find the missing values in the column
full_range = spark.range(1, 11).toDF("Number")
missing_values = full_range.join(df, "Number", "left_anti")
missing_values.show()


