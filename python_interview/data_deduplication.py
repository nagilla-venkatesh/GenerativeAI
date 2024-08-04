from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("data_deduplication").getOrCreate()

# Creating sample dataframe with duplicated records
data = [("John", "Doe", 28, "Male"),
        ("John", "Doe", 28, "Male"),
        ("Jane", "Doe", 25, "Female"),
        ("Jane", "Doe", 25, "Female"),
        ("Jane", "Doe", 25, "Female"),
        ("Jane", "Doe", 25, "Female"),
        ("Bob", "Smith", 35, "Male"),
        ("Alice", "Johnson", 42, "Female")]

columns = ["first_name", "last_name", "age", "gender"]
df = spark.createDataFrame(data, columns)
df.show()

from pyspark.sql.functions import count, col, when, lit
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number


def find_deduplicate_rows(df, cols):
    """
    Find and return deduplicated records based on a list of columns
    
    Parameters:
        df         : The dataframe to check
        cols (list): A list of columns to use for identifying duplicate rows
        
    Returns:
        PySparkDataFrame: The deduplicated rows from the input dataframe
    """
    print("Returing deduplicated records into df")
    return df.drop_duplicates(subset=cols)

def find_duplicate_rows(df, cols):
    """
    Find and return duplicated records based on a list of columns

    Parameters:
        df       : pyspark.sql.DataFrame : The dataframe to check
        cols     : list[str]              : A list of column names to use for identifying duplicate rows

    Returns:
        pyspark.sql.DataFrame : The duplicated rows from the input dataframe
    """
    
    window = Window.partitionBy(cols).orderBy(cols)
    duplicate_df = df.select('*', row_number().over(window).alias('row_number')).filter(col('row_number') > 1).orderBy(cols)
    print("Returing duplicated records into df")
    return duplicate_df


def get_duplicates_or_deduplicates(df, cols, dedup=None):
    """
    Find and return duplicated records based on a list of columns

    Parameters:
        df       : pyspark.sql.DataFrame : The dataframe to check
        cols     : list[str]              : A list of column names to use for identifying duplicate rows

    Returns:
        pyspark.sql.DataFrame : The duplicated rows from the input dataframe if dedup is True
        pyspark.sql.DataFrame : The duplicated rows from the input dataframe if dedup is None
    """
    if  dedup == True:
        print("Returing deduplicated records into df")
        return df.drop_duplicates(subset=cols)
    else:
        print("Returing duplicated records into df")
        window = Window.partitionBy(cols).orderBy(cols)
        duplicate_df = df.select('*', row_number().over(window).alias('row_number')).filter(col('row_number') > 1).orderBy(cols)
        return duplicate_df


cols = ['first_name','last_name','age','gender']
display(df) # type: ignore

# 01 Calling Find find_deduplicate_rows Function
display(find_deduplicate_rows(df, cols)) # type: ignore

# 02. Calling find_duplicate_rows Function
display(find_duplicate_rows(df, cols)) # type: ignore

# 03. Calling get_duplicates_or_deduplicates Function
display(get_duplicates_or_deduplicates(df,cols,False)) # type: ignore