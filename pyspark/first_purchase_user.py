from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import min

spark = SparkSession.builder.appName("example").getOrCreate()

purchase_data = [
    Row(UserID=1, PurchaseDate='2023-01-05'),
    Row(UserID=1, PurchaseDate='2023-01-10'),
    Row(UserID=2, PurchaseDate='2023-01-03'),
    Row(UserID=2, PurchaseDate='2023-01-04'),
    Row(UserID=3, PurchaseDate='2023-01-12')
]

df_purchase = spark.createDataFrame(purchase_data)

# Find the first purchase date for each user
first_purchase = df_purchase.groupBy('UserID').agg(
    min('PurchaseDate').alias('FirstPurchaseDate'))

first_purchase.show()
