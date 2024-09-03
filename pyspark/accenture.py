# Convert first letter of each word to upper case in pyspark datafarme 

from pyspark.sql import SparkSession
from pyspark.sql.functions import initcap
from pyspark.sql import Row

spark = SparkSession.builder.appName("Accenture").getOrCreate()

data = [Row(name= "joseph"), 
        Row(name="michael"),]

df = spark.createDataFrame(data)

df.withColumn("name", initcap(df.name)).show()
