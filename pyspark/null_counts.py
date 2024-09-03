# get counts of nulls in each column of a dataframe

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when

spark = SparkSession.builder.appName("example").getOrCreate()

data = [(1, None, 2), (None, 3, None), (None, 1, 5), (None, 5, 6), 
        (7, 8, None), (8,None, 9), (None, 10, 11)]

df = spark.createDataFrame(data, ["A", "B", "C"])

# get counts of nulls in each column of a dataframe
df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns]).show() 
