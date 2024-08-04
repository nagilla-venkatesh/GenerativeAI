data = [( 
'3000' ,  '22-may'), 
('5000' ,  '23-may'),
('5000' ,  '25-may'),
('10000' , '22-june'),  
('1250'  , '03-july')]
schema = ['revenue','date']

from pyspark.sql.functions import col, to_date, date_format
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Python Spark SQL basic example").getOrCreate()

spark.conf.set("spark.sql.legacy.timeParserPolicy", "LEGACY")

df= spark.createDataFrame(data=data, schema=schema)
df2 = df.withColumn('month', date_format(to_date(col('date'), 'dd-MMM'), 'MMM'))
df2.createOrReplaceTempView('temp')
qry = '''select revenue,month,sum(revenue) 
OVER(PARTITION BY Month ORDER BY Revenue) as cumulative_sum
from temp 
'''
df2.show()

result = spark.sql(qry).show()