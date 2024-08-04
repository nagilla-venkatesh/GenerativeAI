# Generate a sequential number for each row within each group, ordered by date.

from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

spark = SparkSession.builder.appName("example").getOrCreate()

# Sample data
group_data = [
    Row(GroupID='A', Date='2023-01-01'),
    Row(GroupID='A', Date='2023-01-02'),
    Row(GroupID='B', Date='2023-01-01'),
    Row(GroupID='B', Date='2023-01-03')
]

df = spark.createDataFrame(group_data)

# Window specification
window_spec = Window.partitionBy('GroupID').orderBy('Date')

# Generate sequential number for each row within each group
df = df.withColumn('RowNumber', row_number().over(window_spec))

df.show()
