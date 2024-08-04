# different delimiter in a file pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split, regexp_replace

spark = SparkSession.builder.appName("example").getOrCreate()

data = ["1,Alice\t30|New York"]

df = spark.createDataFrame(data, "string")

df = df.withColumn('value', regexp_replace(col('value'), "[,\t|]", ","))

split_col = split(df['value'], ',')

df = df.withColumns({
    "id": split_col.getItem(0),
    "name": split_col.getItem(1),
    "age": split_col.getItem(2),
    "city": split_col.getItem(3),
})

df.select("id", "name", "age", "city").show()

