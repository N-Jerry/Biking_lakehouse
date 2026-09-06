from pyspark.sql.functions import col, trim, when

def rename_columns(df, key_names):
    for key in key_names:
        df = df.withColumnRenamed(key, key_names[key])
    return df

def trim_text(df):
    return df.select(*[
        trim(col(c)).alias(c) if dtype == 'string' else col(c) for c, dtype in df.dtypes
    ])

def gender_fix(df):
    return df.withColumn('gender', when(df.gender == 'M', 'Male').when(df.gender == 'F', 'Female').otherwise(df.gender))

def marital_status_fix(df):
    return df.withColumn('marital_status', when(df.marital_status == 'M', 'Married').when(df.marital_status == 'S', 'Single').otherwise(df.marital_status))

def location_fix(df):
    return df.withColumn('country', when((df.country == 'US') | (df.country == 'United_states'), 'USA').when((df.country == 'DE') | (df.country == 'Germany'), 'Germany').otherwise(df.country))

def drop_nulls(df):
    return df.dropna(how='any')

def drop_duplicates(df):
    return df.dropDuplicates()


