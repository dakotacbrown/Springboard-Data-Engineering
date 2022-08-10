from datetime import date
from loader.loader import Loader
from logger.logger import Log
from extractor.extractor import Extractor
from transformer.transformer import Transformer
import concurrent.futures
import boto3

log = Log(__name__)                                                                             # logger for project

log.logger.info('ELTL Starting')

today = date.today().strftime('%Y/%m/%d')
client = boto3.client('s3')
response = client.list_objects_v2(Bucket='sb-de-c1', Prefix=f'raw/{today}/')

extract = Extractor(today)
transform = Transformer(today)
load = Loader(today)

dataDict = {
    "Annual population growth rate (%)":
        "https://api.worldbank.org/v2/country/all/indicator/SP.POP.GROW?per_page=20000&downloadformat=csv",
    "Coverage of social insurance programs (percent of population)":
        "https://api.worldbank.org/v2/country/all/indicator/per_si_allsi.cov_pop_tot?per_page=20000&downloadformat=csv",
    "Current health expenditure (percent of GDP)":
        "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.CHEX.GD.ZS?per_page=20000&downloadformat=csv",
    "Current health expenditure per capita (current US$)":
        "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.CHEX.PC.CD?per_page=20000&downloadformat=csv",
    "Domestic general government health expenditure (percent of GDP)":
        "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.GHED.GD.ZS?per_page=20000&downloadformat=csv",
    "Domestic general government health expenditure (percent of current health expenditure)":
        "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.GHED.CH.ZS?per_page=20000&downloadformat=csv",
    "Domestic general government health expenditure per capita (current US$)":
        "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.GHED.PC.CD?per_page=20000&downloadformat=csv",
    "Domestic private health expenditure per capita (current US$)":
        "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.PVTD.PC.CD?per_page=20000&downloadformat=csv",
    "GDP (current US$)":
        "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?per_page=20000&downloadformat=csv",
    "GDP per capita (current US$)":
        "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.PCAP.CD?per_page=20000&downloadformat=csv",
    "Inflation, GDP deflator (annual percent)":
        "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.DEFL.KD.ZG?per_page=20000&downloadformat=csv",
    "More than 10 percent of income on out-of-pocket health care":
        "https://api.worldbank.org/v2/country/all/indicator/SH.UHC.OOPC.10.ZS?per_page=20000&downloadformat=csv",
    "More than 25 percent of income on out-of-pocket health care":
        "https://api.worldbank.org/v2/country/all/indicator/SH.UHC.OOPC.25.ZS?per_page=20000&downloadformat=csv",
    "Out-of-pocket expenditure per capita (current US$)":
        "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.OOPC.PC.CD?per_page=20000&downloadformat=csv",
    "People pushed below the $1.90 ($ 2011 PPP) poverty line":
        "https://api.worldbank.org/v2/country/all/indicator/SH.UHC.NOP1.ZS?per_page=20000&downloadformat=csv",
    "People pushed below the $3.20 ($ 2011 PPP) poverty line":
        "https://api.worldbank.org/v2/country/all/indicator/SH.UHC.NOP2.ZS?per_page=20000&downloadformat=csv",
    "Physicians (per 1,000 people)":
        "https://api.worldbank.org/v2/country/all/indicator/SH.MED.PHYS.ZS?per_page=20000&downloadformat=csv",
    "Population, total":
        "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?per_page=20000&downloadformat=csv"
}

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extract.extract, dataDict.items())

with concurrent.futures.ThreadPoolExecutor() as executor2:
    directories = list(filter(lambda d: 'csv' in d, [content['Key'] for content in response.get('Contents', [])]))
    rawFrames = list(executor2.map(transform.csv_to_df, directories))

transformedFrames = transform.transform(rawFrames)
load.load(transformedFrames)
