import pyspark
from delta import *
import uuid

builder = pyspark.sql.SparkSession.builder.appName("delta").master("spark://spark-master:7077") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .config("spark.sql.extensions","io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog","org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .config("spark.hadoop.fs.s3a.access.key","datalake") \
    .config("spark.hadoop.fs.s3a.secret.key","datalake") \
    .config("spark.hadoop.fs.s3a.endpoint","http://minio:9000") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")


spark = configure_spark_with_delta_pip(builder).enableHiveSupport().getOrCreate()
df = spark.read.csv("s3a://delta-lake/results.csv",header=True)
df = df.withColumnRenamed('date','dt')
myuuid = uuid.uuid4()
path = ("s3a://delta-lake/demo/{}").format(myuuid)
print(path)
df.write.format("delta").mode('overwrite').save(path)