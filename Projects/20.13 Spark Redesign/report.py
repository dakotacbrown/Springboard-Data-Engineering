import pyspark
from pyspark.sql.types import *
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.appName('Automobile').getOrCreate()

#partition management
spark.conf.set("spark.sql.shuffle.partitions", 1)

#creating the schema
schema = StructType([
    StructField('incident_id', IntegerType(), True),
    StructField('incident_type', StringType(), True),
    StructField('vin_number', StringType(), True),
    StructField('make', StringType(), True),
    StructField('model', StringType(), True),
    StructField('year', StringType(), True),
    StructField('incident_date', DateType(), True),
    StructField('description', StringType(), True),
])

#read in the file
auto = spark.read.format('csv').options(delimiter=',', header=False).load('data/auto.csv', schema=schema)
auto.cache()

#filter the incidents
incidents_filtered = auto.select('vin_number', 'make', 'year').where(F.col('incident_type') == 'I').cache()

#filter the accidents
accidents_filtered = auto.select('*').where(F.col('incident_type') == 'A').cache()

#combine the tables
joinedDF = incidents_filtered.join(F.broadcast(accidents_filtered), 'vin_number').select('*').cache()

#get the results
result = joinedDF.select('make', 'year').groupBy('make', 'year').agg(F.count('*').alias('total_num'))

#save results to folder
result.write.mode('overwrite').option("header", "true").format('csv').save("output/")
