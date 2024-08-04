from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("example").getOrCreate()

data = [Row(UserID=4001, Age=17),
        Row(UserID=4002, Age=45),
        Row(UserID=4003, Age=65),
        Row(UserID=4004, Age=30),
        Row(UserID=4005, Age=80)]

df = spark.createDataFrame(data)

# creating udf for categorizing age
def find_age_category(age):
    if age < 18:
        return "Child"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

udf_find_age = udf(find_age_category, StringType())
df = df.withColumn("AgeCategory", udf_find_age(df.Age))

df.show()