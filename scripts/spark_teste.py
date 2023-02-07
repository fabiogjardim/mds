import pyspark
from delta import *
import uuid
import requests
import json

builder = pyspark.sql.SparkSession.builder.appName("delta").master("spark://spark-master:7077") 


spark = configure_spark_with_delta_pip(builder).enableHiveSupport().appName("DataExtraction").getOrCreate()

response = requests.get("https://api.mfapi.in/mf/118550")
data = response.json()
json_formatted = json.dumps(data)
with open("./api_data.json", "w") as data_file:
        data_file.write(json_formatted)

raw_json_dataframe = spark.read.format("json") \
                            .option("inferSchema","true") \
                            .load("./api_data.json")

raw_json_dataframe.printSchema()
