import pyspark
from pyspark.sql import SparkSession
#import broadcast
from pyspark.sql.functions import count, month, broadcast
import os


spark = SparkSession.builder.appName('Optimize I').getOrCreate()

#partition management
spark.conf.set("spark.sql.shuffle.partitions", 4)

base_path = os.getcwd()

#wrong path used updated to correct path
answers_input_path = 'data/answers'

questions_input_path = 'data/questions'

#cache the data frames in case they're used multiple times
answersDF = spark.read.option('path', answers_input_path).load().cache()

questionsDF = spark.read.option('path', questions_input_path).load().cache()

answers_month = answersDF.withColumn('month', month('creation_date')).groupBy('question_id', 'month').agg(count('*').alias('cnt')).cache()

#broadcast the smaller DF to the bigger one
resultDF = questionsDF.join(broadcast(answers_month), 'question_id').select('question_id', 'creation_date', 'title', 'month', 'cnt')

resultDF.orderBy('question_id', 'month').show()