data = [('4529', 'Nancy', 'Young', '4125'),
('4238','John', 'Simon', '4329'),
('4329', 'Martina', 'Candreva', '4125'),
('4009', 'Klaus', 'Koch', '4329'),
('4125', 'Mafalda', 'Ranieri', 'NULL'),
('4500', 'Jakub', 'Hrabal', '4529'),
('4118', 'Moira', 'Areas', '4952'),
('4012', 'Jon', 'Nilssen', '4952'),
('4952', 'Sandra', 'Rajkovic', '4529'),
('4444', 'Seamus', 'Quinn', '4329')]
schema = ['employee_id' ,'first_name', 'last_name', 'manager_id']

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Python Spark SQL basic example").getOrCreate()

df = spark.createDataFrame(data=data, schema=schema)

df.createOrReplaceTempView('EMP')
df.show()

# Method 1
query = '''select  e.manager_id as manager_id, 
count(e.employee_id) as no_of_emp,(m.First_name) as mangr_name 
from  emp e
inner join emp m 
on m.employee_id =e.manager_id
group by 1,3
'''
result=spark.sql(query).show()

from pyspark.sql.functions import col
# Method 2
# Self-join the DataFrame to get manager names
result_df = df.alias("e").join(df.alias("m"), 
col("e.manager_id") == col("m.employee_id"), "inner") \
.select(col("e.employee_id"), col("e.first_name"), col("e.last_name"),
col("e.manager_id"),col("m.first_name").alias("manager_first_name"))

result_df.show()
