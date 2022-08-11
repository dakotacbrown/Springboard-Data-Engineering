import boto3
from datetime import date
import concurrent.futures
from logger.logger import Log
from loader.loader import Loader
from transformer.transformer import Transformer

log = Log(__name__)  # logger for project

log.logger.info('ETL Starting')

today = date.today().strftime('%Y/%m/%d')
client = boto3.client('s3')
response_csv = client.list_objects_v2(Bucket='sb-de-c2', Prefix=f'raw/csv')
response_json = client.list_objects_v2(Bucket='sb-de-c2', Prefix=f'raw/json')

transform = Transformer()
load = Loader(today)

with concurrent.futures.ThreadPoolExecutor() as executor:
    directories_csv = list(filter(lambda d: 'txt' in d and 'crc' not in d,
                                  [content['Key'] for content in response_csv.get('Contents', [])]))
    directories_json = list(filter(lambda d: 'txt' in d and 'crc' not in d,
                                   [content['Key'] for content in response_json.get('Contents', [])]))

    raw_frames_csv = list(executor.map(transform.csv_to_df, directories_csv))
    raw_frames_json = list(executor.map(transform.json_to_df, directories_json))

raw_trade = [x[0] for x in raw_frames_csv] + [x[0] for x in raw_frames_json]
raw_quote = [x[1] for x in raw_frames_csv] + [x[1] for x in raw_frames_json]

pre_transform_trade = transform.combine(raw_trade)
pre_transform_quote = transform.combine(raw_quote)

transformed_data = transform.transform(pre_transform_trade, pre_transform_quote)

load.load(transformed_data, pre_transform_quote)
