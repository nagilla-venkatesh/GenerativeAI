from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import countDistinct

spark = SparkSession.builder.appName("example").getOrCreate()

# Sample data
visitor_data = [Row(Date='2023-01-01', VisitorID=101),
                Row(Date='2023-01-01', VisitorID=102),
                Row(Date='2023-01-01', VisitorID=101),
                Row(Date='2023-01-02', VisitorID=103),
                Row(Date='2023-01-02', VisitorID=101)]

df = spark.createDataFrame(visitor_data)

# Find unique visitors per day
unique_visitors = df.groupBy('Date').agg(
    countDistinct('VisitorID').alias('UniqueVisitors'))

unique_visitors.show()
