#Problem: Given a dataset of sales records with monthly sales per product, reshape the data to have one row per product-month combination.

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

spark = SparkSession.builder.appName("example").getOrCreate()

# Sample data: Product sales per month
data = [("Product1", 100, 150, 200),
        ("Product2", 200, 250, 300),
        ("Product3", 300, 350, 400)]

columns = ["Product", "Sales_Jan", "Sales_Feb", "Sales_Mar"]

df = spark.createDataFrame(data, columns)

# Reshape the data to have one row per product-month combination
df_pivot = df.select(col("Product"), 
                     expr("stack(3, 'Jan', Sales_Jan, 'Feb', Sales_Feb, 'Mar', Sales_Mar) as (Month, Sales)"))

df_pivot.show()


