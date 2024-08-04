#Problem: Given a dataset of sales records, identify and replace all missing values in the 'amount' column with the average sales amount.

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

spark = SparkSession.builder.appName("example").getOrCreate()

sales_data = [("1", 100), ("2", 150), ("3", None), ("4", 200), ("5", None)]

df_sales = spark.createDataFrame(sales_data, ["salesID", "Amount"])

# Calculate the average sales amount
avg_sales_amount = df_sales.select(avg(col("Amount"))).collect()[0][0]

# Replace missing values with the average amount
sales_df = df_sales.na.fill(avg_sales_amount, ["Amount"])   

sales_df.show()

