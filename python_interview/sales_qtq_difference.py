# To calculate and analyze the percentage difference in sales 
# between Quarter 1 (Q1) and Quarter 2 (Q2) of the year 2010. 

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, quarter, sum
# Initialize Spark session
spark = SparkSession.builder.appName("SalesAnalysis").getOrCreate()
# Sample data (replace this with your actual data loading logic)
data = [
 ("2010–01–02", 500),
 ("2010–02–03", 1000),
 ("2010–03–04", 1000),
 ("2010–04–05", 1000),
 ("2010–05–06", 1500),
 ("2010–06–07", 1000),
 ("2010–07–08", 1000),
 ("2010–08–09", 1000),
 ("2010–10–10", 1000)
]

# Define schema for the sales data
schema = ["date", "sales"]

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Add a column for the quarter of the year
df = df.withColumn("quarter", quarter(col("date")))

quarterly_sales = df.groupBy("quarter").agg(sum("sales").alias("total_sales"))

q1_sales = quarterly_sales.filter(col("quarter") == 1).select("total_sales").collect()[0][0]
q2_sales = quarterly_sales.filter(col("quarter") == 2).select("total_sales").collect()[0][0]

percentage_difference = ((q2_sales - q1_sales) / q1_sales) * 100

print(f"The percentage difference in sales between Q1 and Q2 of 2010 is: {percentage_difference:.2f}%")
