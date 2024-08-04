# Write a Pypark code to filter customer transactions 
# greater than $10,000, transform customer names to have 
# the first letter capitalized and the rest in lowercase 
# and compute the average transaction amount for each product 
# category.

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, initcap

# Create a SparkSession
spark = SparkSession.builder \
    .appName("CustomerTransactionAnalysis") \
    .getOrCreate()

# Sample data for customer transactions with customer names in all capitals
data = [
    (1, "ALICE", 12000, "Electronics"),
    (2, "BOB", 9000, "Home Appliances"),
    (3, "CHARLIE", 15000, "Fashion"),
    (4, "DANIEL", 8000, "Electronics"),
    (5, "EMMA", 11000, "Fashion"),
    (6, "FRANK", 13000, "Home Appliances"),
    (7, "GINA", 10000, "Electronics"),
    (8, "HENRY", 14000, "Fashion"),
    (9, "ISABELLA", 9500, "Home Appliances"),
    (10, "JACK", 10500, "Electronics")
]

customer_df = spark.createDataFrame(data, ["customer_id", "customer_name", "transaction_amount", "product_category"])

# Show initial data 
customer_df.show()

# Transform the customer name to initcap format 
transformed_df = customer_df.withColumn("customer_name_transformed", initcap(col("customer_name")))

# filter transactions greater than $10,000
filtered_transactions = transformed_df.filter(col("transaction_amount") > 10000)

# calculate average transaction amount for each product category
avg_transaction_by_category = filtered_transactions.groupBy("product_category").agg(avg("transaction_amount").alias("average_transaction_amount"))

# show the average transaction amount for each product category

result = filtered_transactions.select("customer_name_transformed", "transaction_amount", "product_category")\
    .join(avg_transaction_by_category, "product_category")\
        .orderBy("product_category")

result.show()

spark.stop()



