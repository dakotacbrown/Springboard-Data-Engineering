from logger.logger import Log
from datetime import datetime
from pyspark.sql.types import *
import pyspark.sql.functions as f
from pyspark.sql import SparkSession
from pyspark.sql.window import Window

spark = SparkSession.builder.appName('Transform - Finance').getOrCreate()       # session created
spark.conf.set("spark.sql.shuffle.partitions", 4)                               # partition management
log = Log(__name__)                                                             # logger for project


class Transformer:
    def __init__(self):
        self.URI = f's3a://sb-de-c2/'
        self.trade = StructType([
                StructField('trade_date', DateType(), True),
                StructField('file_time', TimestampType(), True),
                StructField('record_type', StringType(), True),
                StructField('symbol', StringType(), True),
                StructField('event_time', TimestampType(), True),
                StructField('event_sequence_number', IntegerType(), True),
                StructField('exchange', StringType(), True),
                StructField('trade_price', FloatType(), True),
                StructField('trade_size', IntegerType(), True),
            ])

        self.quote = StructType([
                StructField('trade_date', DateType(), True),
                StructField('file_time', TimestampType(), True),
                StructField('record_type', StringType(), True),
                StructField('symbol', StringType(), True),
                StructField('event_time', TimestampType(), True),
                StructField('event_sequence_number', IntegerType(), True),
                StructField('exchange', StringType(), True),
                StructField('bid_price', FloatType(), True),
                StructField('bid_size', IntegerType(), True),
                StructField('ask_price', FloatType(), True),
                StructField('ask_size', IntegerType(), True),
            ])

    def csv_to_df(self, csv_file):
        """
        csv_to_df

        Opens each csv per folder and turns them into a dataframe

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
            rdd = spark.read.csv(f'{self.URI}{csv_file}')       # create rdd from CSV

            rdd_trade = spark.sparkContext.parallelize([trade for trade in rdd.collect() if trade[2] == 'T'])
            rdd_quote = spark.sparkContext.parallelize([quote for quote in rdd.collect() if quote[2] == 'Q'])

            rdd_trade = rdd_trade.map(lambda t: (datetime.strptime(t[0], '%Y-%m-%d'),
                                                 datetime.strptime(t[1], '%Y-%m-%d %H:%M:%S.%f'), t[2], t[3],
                                                 datetime.strptime(t[4], '%Y-%m-%d %H:%M:%S.%f'), int(t[5]), t[6],
                                                 float(t[7]), int(t[8])))

            rdd_quote = rdd_quote.map(lambda q: (datetime.strptime(q[0], '%Y-%m-%d'),
                                                 datetime.strptime(q[1], '%Y-%m-%d %H:%M:%S.%f'), q[2], q[3],
                                                 datetime.strptime(q[4], '%Y-%m-%d %H:%M:%S.%f'), int(q[5]), q[6],
                                                 float(q[7]), int(q[8]), float(q[9]), int(q[10])))

            df_trade_csv = spark.createDataFrame(rdd_trade, self.trade).cache()
            df_quote_csv = spark.createDataFrame(rdd_quote, self.quote).cache()

            return df_trade_csv, df_quote_csv
        except Exception as e:
            log.logger.critical(e)
        finally:
            log.logger.info(f'Spark DataFrame Successfully created from CSV {csv_file}.')

    def json_to_df(self, json_file):
        """
        json_to_df

        Opens each json per folder and turns them into a dataframe

        Attributes
        ----------
        json_file: path of the directory holding the csv file

        Returns
        -------
        Dataframe stores information from a specific csv

        Acknowledgement:
        https://stackoverflow.com/questions/33503993/read-in-all-csv-files-from-a-directory-using-python
        """

        try:
            rdd = spark.read.json(f'{self.URI}{json_file}')     # create rdd from json

            rdd_trade = spark.sparkContext.parallelize([trade for trade in rdd.collect() if trade['event_type'] == 'T'])
            rdd_quote = spark.sparkContext.parallelize([quote for quote in rdd.collect() if quote['event_type'] == 'Q'])

            rdd_trade = rdd_trade.map(lambda t: (datetime.strptime(t['trade_dt'], '%Y-%m-%d'),
                                                 datetime.strptime(t['file_tm'], '%Y-%m-%d %H:%M:%S.%f'),
                                                 t['event_type'], t['symbol'],
                                                 datetime.strptime(t['event_tm'], '%Y-%m-%d %H:%M:%S.%f'),
                                                 int(t['event_seq_nb']), t['exchange'],
                                                 float(t['price']), int(t['size'])))

            rdd_quote = rdd_quote.map(lambda q: (datetime.strptime(q['trade_dt'], '%Y-%m-%d'),
                                                 datetime.strptime(q['file_tm'], '%Y-%m-%d %H:%M:%S.%f'),
                                                 q['event_type'], q['symbol'],
                                                 datetime.strptime(q['event_tm'], '%Y-%m-%d %H:%M:%S.%f'),
                                                 int(q['event_seq_nb']), q['exchange'], float(q['bid_pr']),
                                                 int(q['bid_size']), float(q['ask_pr']), int(q['ask_size'])))

            df_trade_json = spark.createDataFrame(rdd_trade, self.trade).cache()
            df_quote_json = spark.createDataFrame(rdd_quote, self.quote).cache()

            return df_trade_json, df_quote_json
        except Exception as e:
            log.logger.critical(e)
        finally:
            log.logger.info(f'Spark DataFrame Successfully created from CSV {json_file}.')

    def combine(self, frames):
        collection = frames[0].cache()
        for frame in frames[1:]:
            collection = collection.union(frame)
        return collection

    def transform(self, trade, quote):
        """
        transform

        Transforms each dataframe into the correct format

        Attributes
        ----------
        trade: dataframe that holds trade data
        quote: dataframe that holds quote data

        Returns
        -------
        Transformed dataframes of trade and quote data
        """

        try:
            window_avg = Window.partitionBy('symbol', 'exchange', 'trade_date').orderBy('event_time').rowsBetween(-1, 0)
            window_last = Window.partitionBy('symbol', 'exchange', 'trade_date').orderBy('event_time').rowsBetween(
                Window.unboundedPreceding, Window.unboundedFollowing)
            trade_tmp = trade.withColumn('mov_avg_pr', f.mean('trade_price').over(window_avg)).withColumn(
                'last_pr', f.last('trade_price').over(window_last))
            trade_tmp = trade_tmp.drop('event_sequence_number').drop('event_time')
            joined = quote.join(f.broadcast(trade_tmp), ['trade_date', 'symbol', 'exchange'])\
                .drop('file_time', 'record_type')\
                .orderBy(f.col('exchange').asc(),
                         f.col('symbol').asc(),
                         f.col('event_sequence_number').asc(),
                         f.col('event_time').asc())

            return trade, joined
        except Exception as e:
            log.logger.critical(e)
        finally:
            log.logger.info('End Transform')
