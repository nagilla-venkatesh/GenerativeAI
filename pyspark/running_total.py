# Write a pyspark code to calculate find running total for each dept in a store.

# Example output:
"""
+-----+-------+-----------+------+-------------+
|EmpID|   Name|       Dept|Salary|Running_Total|
+-----+-------+-----------+------+-------------+
|  100| Name 1|        HR |  2000|         2000|
|  104| Name 5|        HR |  2500|         4500|
|  108| Name 9|        HR |  1900|         6400|
|  101| Name 2|    Finance|  3000|         3000|
|  109|Name 10|    Finance|  7000|        10000|
|  102| Name 3|        IT |  3400|         3400|
|  110|Name 11|        IT |  5000|         8400|
|  103| Name 4|Operational|  5000|         5000|
+-----+-------+-----------+------+-------------+
"""

from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql import functions as f

def running_total():
    spark = SparkSession.builder.appName("running_total").getOrCreate()
    data = [(100, 'Name 1', 'HR', 2000), 
            (101, 'Name 2', 'Finance', 3000), 
            (102, 'Name 3', 'IT', 3400), 
            (103, 'Name 4', 'Operational', 5000), 
            (104, 'Name 5', 'HR', 2500), 
            (108, 'Name 9', 'HR', 1900), 
            (109, 'Name 10', 'Finance', 7000), 
            (110, 'Name 11', 'IT', 5000)]
    columns = ['EmpID', 'Name', 'Dept', 'Salary']
    df = spark.createDataFrame(data, columns)
    window = Window.partitionBy('Dept').orderBy('EmpID')
    df = df.withColumn('Running_Total', f.sum('Salary').over(window))
    df.show()
    spark.stop()
    



    
    