# In a DataFrame df_sales with columns Date, ProductID, and QuantitySold, how would you calculate a 7-day rolling average of QuantitySold for each product?

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col
from pyspark.sql import Row
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("example").getOrCreate()

data = [
    Row(Date="2021-01-01", ProductID=1, QuantitySold=10),
    Row(Date="2021-01-02", ProductID=1, QuantitySold=15),
    Row(Date="2021-01-03", ProductID=1, QuantitySold=20),
    Row(Date="2021-01-04", ProductID=1, QuantitySold=25),
    Row(Date="2021-01-05", ProductID=1, QuantitySold=30),
    Row(Date="2021-01-06", ProductID=1, QuantitySold=35),
    Row(Date="2021-01-07", ProductID=1, QuantitySold=40),
    Row(Date="2021-01-08", ProductID=1, QuantitySold=45),
]

df = spark.createDataFrame(data)

# Window specification for 7-day rolling average
window_spec = Window.partitionBy("ProductID").orderBy("Date").rowsBetween(-6, 0)

df = df.withColumn("RollingAvg", avg(col("QuantitySold")).over(window_spec))

df.show()

