from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
from logger.logger import Log
import boto3

log = Log(__name__)                                                                             # logger for project


class Extractor:

    def __init__(self, today):
        self.client = boto3.Session().client('s3')
        self.resource = boto3.resource('s3')
        self.S3_BUCKET = 'sb-de-c1'
        self.FOLDER = f'raw/{today}/'

    def extract(self, info):
        """
        Extract

        Pulls all the information from the source, unzips them, and saves to a new folder in S3.

        Attributes
        ----------
        info: Dict
            Dictionary of data files to be pulled.
        """

        log.logger.info(f'Extracting {info[0]}')
        try:
            with urlopen(info[1]) as zipFile:
                with ZipFile(BytesIO(zipFile.read())) as file:
                    self.client.put_object(
                        Body=file.open(file.namelist()[1]).read(),
                        Bucket=self.S3_BUCKET,
                        Key=f'{self.FOLDER}{file.namelist()[1]}'
                    )
        except Exception as e:
            log.logger.critical(e)
            exit()
        finally:
            log.logger.info(f'{info[0]} has been successfully extracted from source and loaded into S3')
