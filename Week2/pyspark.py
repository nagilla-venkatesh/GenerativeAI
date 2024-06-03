# How to merge two dataframe in PySpark of different Schema?
from pyspark.sql import SparkSession # type: ignore
from pyspark.sql.functions import col,lit # type: ignore


# Create a SparkSession
spark = SparkSession.builder.appName("MergeDifferentSchemasExample") \
        .getOrCreate()

# Create first dataframe
data1 = [("John", 25),
         ("Alice", 30),
         ("Bob", 35)]

df1 = spark.createDataFrame(data1, ["Name", "Age"])

# Create second dataframe with a different schema
data2 = [("John", "Developer"),
         ("Alice", "Engineer"),
         ("Eve", "Scientist")]

df2 = spark.createDataFrame(data2, ["Name", "Profession"])

# Add missing column to the first dataframe
df1 = df1.withColumn("Profession", lit(None))

# Select columns in the second dataframe to match the first dataframe
df2 = df2.select("Name", lit(None).alias("Age"), "Profession")

# Union the two dataframes
merged_df = df1.union(df2)

# Show the result
merged_df.show()