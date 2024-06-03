# PySpark Interview Questions and Answers 

## Question Context 
Consider you have written a Python recursive code to print the Fibonacci series inside your PySpark code. You run this code on a Databricks notebook attached to a Spark Cluster with a driver and two executors. 

### Question1
Where this code will be executed - On Driver or On Executor ? If on Executor then on how many?

### Answer 
The Python code will be executed on Driver.

### Question2 
What will happen on the cluster while this code is being executed?

### Answer 
The cluster will sit idle performing health checks while the driver executes the code and returns the result 

### Question3 
Consider a lot of CSV files of the same structure within many nested folders as mentioned below

```python
emp_folder (root)
|-- emp.csv
|-- folder_1/emp_1.csv
|-- folder_2/emp_2.csv
|-- folder_3/folder_4/emp_3.csv
```

How would you read all CSV files in a single go using Spark?

### Answer 
```python
df = spark.read.format("csv").option("recursiveFileLookup", True).option("header", True).load("emp_folder/")
```

## Context for Question 
Consider you are reading multiple CSV files together in your Spark DataFrame for Processing in a single shot.

```emp_details
|-- emp1.csv
|-- emp2.csv
|-- emp3.csv
```

### Question 4
How to get the file name in a new column for every data record which is read from the csv files?

### Answer
We can always use input_file_name() to get the name of the file.

### Question5
What if we also need the complete file path as new column ?

### Answer 
There is one hidden column _metadata, which can also be used to get the file names and paths.

### Question5
Consider the following JSON data.

```python
{
"name": "Subham",
"mobile": ["9888999", "8774773"],
}
```

Write PySpark DataFrame API code to generate data as follows

```
|-------------------|
| name    | mobile  |
| ------------------|
| Subham  | 9888999 |
| Subham  | 8774773 |
| ------------------|
```

### Answer
Since the phone number is an array/list field we need to explode the data in order to bring each phone number in each row.

So, consider we have already read the json data in a DataFrame df.

```python
from pyspark.sql.functions import explode
final_df = df.withColumn("mobile", explode("mobile"))
```

### Question7
Consider you have a Spark Cluster with 5 executors 3 cores and 30GB of memory each. You are reading some data in dataframe df and writing them in the form of CSV using the following two codes.

Case 1: 
```python
df.coalesce(1).write.format("csv").option("header", True).save("data/out/1/emp.csv")
```

Case 2: 
```python
df.repartition(1).write.format("csv").option("header", True).save("data/out/1/emp.csv")
```

How many CSV files will be created in the output directory for Case 1 and Case 2? And why so?

### Answer
Both cases will generate only 1 file. But there is a big difference in each one's execution plan.

Case 1: In case of coalesce Spark will try to avoid shuffling of data, thus it will use only 1 task from any one executor throughout to read, process and write the data in a single file. Now if you have a big file to read and process this can lead to issues as we are losing parallel processing capabilities here and also can spill data to disk if it doesn't fit in memory.

Case 2: Since, Repartition allow shuffling Spark will read and process the file using 15 tasks in parallel and then shuffle all data to an executor to write it using only 1 task. And we all know shuffling is a costly operation in Spark. But it doesn't lose the parallel processing capability and can be faster in certain cases where you have a huge processing plan for huge dataset.

Thus, it's very important to understand the use case and then decide between Repartition or Coalesce.

### Question8
Consider the following execution code on a cluster of 2 executors and 4 cores each

```python
df_1 = spark.range(0, 100, 2)
df_2 = spark.range(2, 100, 4)

df_3 = df_1.repartition(4)
df_4 = df_2.coalesce(4)

df_5 = df_3.join(df_4, on='id')

df_5.repartition(1).write.format("csv").save("numbers.csv")
```

Guess the number of stages for the above code, considering all code is executed in a single job.

### Answer
Spark divides the job in multiple stages based on shuffling/wide transformation. But the number of stages will also change based on - if Broadcast join is enabled or not. It's enabled by default starting Spark 3.

If enabled, there will be no shuffle and number stages would be 3. 

If not enabled, the soft merge join will take place resulting in shuffling of data and joining with 4 stages. 

### Question9
Consider you are reading data from a JDBC source such as SQLite or Postgres. You have some trx_id (transaction id) column in the table which is an increasing number.

```python
df_full = spark \
 .read \
 .format("jdbc") \
 .option("driver", driver) \
 .option("url", jdbc_url) \
 .option("dbtable", table_name) \
 .load()
```

How can we optimize the above code to make sure data can be read faster from the table ?

### Answer
JDBC allows us to use partitionColumn as an option while reading data. We need to provide the min and max value for that column and spark will automatically read the data in parallel based on the num of partitions provided.

```python
df_full = spark \
 .read \
 .format("jdbc") \
 .option("driver", driver) \
 .option("url", jdbc_url) \
 .option("dbtable", table_name) \
 .option("partitionColumn", "trx_id") \
 .option("lowerBound", 20) \
 .option("upperBound", 2147474653) \
 .option("numPartitions", 8) \
 .load()
```

Spark will utilise 8 parallel tasks to read the data.

### Question10 
Consider you are reading the following JSON data from a text file (json_dump.txt) in a DataFrame, which contains each line as JSON payload with an array/list field devices of deviceId dictionaries/struct/map.

```python
{"devices": [{"deviceId": "D007"}, {"deviceId": "D005"}]}
{"devices": [{}]}
{"devices": [{"deviceId": "D004"}]}
```

How would you filter out the records where there is no deviceId data for struct/map in array (In above example 2nd record) ? Output should contain only record 1 and 3 in DataFrame.

### Answer

```python
# Read JSON data from file into DataFrame
df = spark.read.json("json_dump.txt")

# Filter out records where the devices array is not empty and deviceld is not null
filtered_df = df.filter((size(col("devices")) > 0) & (col("devices.deviceld").isNotNull()))

# Show the resulting DataFrame
filtered_df.show(truncate=False)
```

### Question11
Consider you have a Spark Cluster with 5 executors 3 cores and 30GB of memory each. You are reading some data as follows in dataframe df and writing them in the form of Parquet.

```python
empno | deptno
101 | D12
102 | D12
103 | D11
104 | D11
105 | D14
```

```python
# Case 1: 
df.where("deptno='D10'").write.format("parquet").save("data/out/1/emp.parquet")

# Case 2: 
df.where("deptno='D10'").write.format("parquet").partitionBy("deptno").save("data/out/1/emp.parquet")
```
How many folders/Parquet files will be created in the output directory for Case 1 and Case 2? And why so?

### Answer
Case 1: One Parquet file will be created in emp.parquet folder which will be empty. In case you read this parquet file, you will read the correct schema with column names but there will be no data.

Case 2: No files or partition folders will be created in emp.parquet folder. Since partitionBy itself is on the department column and the department D10 is missing in data, thus there will be no folder/files created under emp.parquet folder.


# Checkout the YouTube videos for PySpark 
https://www.youtube.com/playlist?list=PL2IsFZBGM_IHCl9zhRVC1EXTomkEp_1zm

