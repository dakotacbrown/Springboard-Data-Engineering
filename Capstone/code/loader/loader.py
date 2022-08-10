from logger.logger import Log
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName('Load - World Bank').getOrCreate()                         # session created
spark.conf.set("spark.sql.shuffle.partitions", 4)                                               # partition management
log = Log(__name__)                                                                             # logger for project


class Loader:

    def __init__(self, today):
        self.URI = f's3a://sb-de-c1/transformed/{today}/'

    def load(self, frames):
        """
        load

        Loads the dataframes into S3 as parquet files

        Attributes
        ----------
        frames: pyspark dataframes that needs to be saved
        """
        for i, frame in enumerate(frames):
            frame.coalesce(1).write.mode('overwrite').parquet(f'{self.URI}{i}.parquet')
