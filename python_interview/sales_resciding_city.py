# We have 3 table ( Sales Details, Store Details, and 
# Customer Details). find out how many sales happened for 
# the customers and store residing in same location/city.

sales_data = [
    (1, 101, "01-01-2020", 30),
    (1, 102, "02-01-2020", 50),
    (4, 101, "11-06-2020", 150),
    (5, 108, "13-06-2020", 20),
    (5, 104, "14-07-2020", 220),
    (6, 108, "15-08-2020", 190),
    (1, 103, "03-03-2020", 60),
    (2, 104, "04-03-2020", 100),
    (3, 101, "08-05-2020", 60),
    (3, 107, "09-05-2020", 120),
    (4, 103, "10-05-2020", 110),
    (7, 105, "18-09-2020", 40),
    (7, 102, "19-10-2020", 120),
    (1, 103, "03-06-2020", 120)
]

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

spark = SparkSession.builder.appName("Python Spark SQL basic example").getOrCreate()

sales_columns = ["STORE_ID", "CUST_ID", "TRANSACTION_DATE", "SALES"]
sales_df = spark.createDataFrame(sales_data, sales_columns)

store_data = [
    (1, "STORE-1", "Chennai"),
    (2, "STORE-2", "Mumbai"),
    (3, "STORE-3", "Calcutta"),
    (4, "STORE-4", "New Delhi"),
    (5, "STORE-5", "Bangalore"),
    (8, "STORE-6", "Pune")
]

store_columns = ["STORE_ID", "STORE_NAME", "LOCATION"]
store_df = spark.createDataFrame(store_data, store_columns)

customer_data = [
    (101, "Arun", "Chennai"),
    (102, "Vijay", "Mumbai"),
    (105, "Meera", "Kolkatta"),
    (106, "Rajesh", "New Delhi"),
    (107, "Sanjay", "New Delhi"),
    (108, "Ram", "Bangalore")
]

customer_columns = ["CUST_ID", "CUST_NAME", "CUST_LOCATION"]
customer_df = spark.createDataFrame(customer_data, customer_columns)

# Join Sales_Details with Store Details
sales_store_df = sales_df.join(store_df, on="STORE_ID")

# Join the result with Customer Details
sales_store_customer_df = sales_store_df.join(customer_df, on="CUST_ID")

sales_store_cust_df=sales_store_df.join(customer_df,on="CUST_ID")
sales_store_cust_df.show()

matching_location_df = sales_store_customer_df.filter(
    col("LOCATION") == col("CUST_LOCATION")
)

result_df = matching_location_df.groupBy("STORE_ID", "CUST_ID").agg(
    count("*").alias("no_of_transaction")
)

result_df.select("STORE_ID", "CUST_ID", "no_of_transaction").show()
