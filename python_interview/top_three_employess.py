# Write a solution to find the top 3 employees 
# who are high earners in each of the departments.

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, dense_rank
from pyspark.sql.window import Window

spark = SparkSession.builder \
    .appName("TopThreeEmployees") \
    .getOrCreate()
    
# Define the schema for Employee and Department tables
employee_schema = "id INT, name STRING, salary INT, departmentId INT"
department_schema = "id INT, dname STRING"

# Sample data for Employee and Department tables
employee_data = [
    (1, 'Joe', 85000, 1), (2, 'Henry', 80000, 2), (3, 'Sam', 60000, 2),
    (4, 'Max', 90000, 1), (5, 'Janet', 69000, 1), (6, 'Randy', 85000, 1),
    (7, 'Will', 70000, 1)
]

department_data = [(1, 'IT'), (2, 'Sales')]

# Create DataFrame representations of Employee and Department tables
employee_df = spark.createDataFrame(employee_data, schema=employee_schema)
department_df = spark.createDataFrame(department_data, schema=department_schema)

# Join Employee and Department Datafarmes 
joined_df = employee_df.join(department_df, employee_df.departmentId == department_df.id)

# Rank employees within each department based on salary
ranked_df = joined_df.withColumn("rank", dense_rank()\
    .over(Window.partitionBy("departmentId")\
        .orderBy(col("salary").desc())))

final_result = ranked_df.filter(col("rank") <= 3)\
    .select("name", "salary", "dname")

final_result.show()

spark.stop()
