# Given a text file meeting_notes.txt, 
# count the frequency of each word and return top 10 words.

file_name = "meeting_notes.txt"
book = spark.read.text(file_name)

# Tokenize the words
from pyspark.sql.functions import split, explode
words = book.select(explode(split(book.value, "\s")).alias("word"))

# Cleaning: lowering and remove special characters
from pyspark.sql.functions import lower, regexp_extract

words_lower = words.select(lower(words.word).alias("word"))
words_clean = words_lower.select(regexp_extract(words_lower.word, "[a-z]+", 0).alias("word"))

# Filitering and counting
from pyspark.sql.functions import length

words_null = words_clean.filter(length(words_clean.word) > 0)
words_count = words_null.groupBy("word").count()

# Ordering the results
words_count.orderBy(words_count["count"].desc()).show(10)
