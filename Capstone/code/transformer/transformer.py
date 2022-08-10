from logger.logger import Log
from pyspark.sql.types import *
from pyspark.sql import SparkSession
import pyspark.sql.functions as f

spark = SparkSession.builder.appName('Transform - World Bank').getOrCreate()  # session created
spark.conf.set("spark.sql.shuffle.partitions", 4)  # partition management
log = Log(__name__)  # logger for project


class Transformer:
    def __init__(self):
        self.URI = f's3a://sb-de-c1/'

    def csv_to_df(self, csv_file):
        """
        csv_to_df

        Opens each csv per folder and turns the first csv into a dataframe

        Attributes
        ----------
        csv_file: path of the directory holding the csv file

        Returns
        -------
        Dataframe stores information from a specific csv

        Acknowledgement:
        https://stackoverflow.com/questions/33503993/read-in-all-csv-files-from-a-directory-using-python
        """

        try:
            rdd = spark.sparkContext.textFile(f'{self.URI}{csv_file}')  # create rdd from CSV
            rdd = rdd.zipWithIndex().filter(lambda a: a[1] > 3).map(
                lambda a: a[0].split('\",\"'))  # removes first 4 rows
            columns = rdd.collect()[0]  # captures header for schema
            columns = [i.strip('\"') for i in columns]
            columns = [i.replace(' ', '') for i in columns]
            columns[-1] = columns[-1].strip(',\"')
            data = rdd.collect()[1:]
            tmp = []
            for value in data:
                tmp.append([x.strip('\"') for x in value])
            data = spark.sparkContext.parallelize(tmp)
            df = spark.createDataFrame(data, columns)
            for col in df.columns[4:]:
                df = df.withColumn(col, f.col(col).cast('float'))
            return df
        except Exception as e:
            log.logger.critical(e)
        finally:
            log.logger.info(f'Spark DataFrame Successfully created from CSV {csv_file}.')

    def transform(self, frames):
        """
        transform

        Transforms each dataframe into the correct format

        Attributes
        ----------
        frames: list of dataframes from the csv files

        Returns
        -------
        Transformed dataframes
        """

        try:
            log.logger.info('Transforming Country Data')
            df_country = frames[0].select(frames[0].columns[:2])
            log.logger.info(df_country.show(5))
            log.logger.info('Country Data Transformed')

            log.logger.info('Transforming Indicator Data')
            df_indicator = spark.createDataFrame(df.select(df.columns[2:4]).first() for df in frames)
            df_indicator = df_indicator.select(df_indicator.columns).distinct()
            log.logger.info(df_indicator.show(5))
            log.logger.info('Country Data Transformed')

            log.logger.info('Transforming Year Data')
            year = StructType([StructField('Year', IntegerType(), True)])
            rdd_year = spark.sparkContext.parallelize([int(i) for i in frames[0].columns[4:]])
            rdd_year = rdd_year.map(lambda x: [x])
            df_year = spark.createDataFrame(rdd_year, year)
            log.logger.info(df_year.show(5))
            log.logger.info('Year Transformed')

            log.logger.info('Transforming Fact Table')
            df_fact = frames[0]
            for lst in frames[1:]:
                df_fact = df_fact.union(lst)
            log.logger.info(df_fact.show(5))
            return [df_country, df_indicator, df_year, df_fact]
        except Exception as e:
            log.logger.critical(e)
        finally:
            log.logger.info('End Transform')
