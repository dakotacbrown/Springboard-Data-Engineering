from logger.logger import Log
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName('Load - Finance').getOrCreate()                            # session created
spark.conf.set("spark.sql.shuffle.partitions", 4)                                               # partition management
log = Log(__name__)                                                                             # logger for project


class Loader:

    def __init__(self, today):
        self.URI = f's3a://sb-de-c2/transformed/{today}/'

    def load(self, frames, quote):
        """
        load

        Loads the dataframes into S3 as parquet files

        Attributes
        ----------
        frames: pyspark dataframes that needs to be saved
        quote: pyspark dataframe that needs to be saved
        """
        frames[0].coalesce(1).write.mode('overwrite').parquet(f'{self.URI}trade_data.parquet')
        frames[1].coalesce(1).write.mode('overwrite').parquet(f'{self.URI}joined_data.parquet')
        quote.coalesce(1).write.mode('overwrite').parquet(f'{self.URI}quote_data.parquet')
