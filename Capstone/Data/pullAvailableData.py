import os
import glob
import logging
import pandas as pd
import concurrent.futures
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen


"""
Logging for the whole file
Acknowledgement: https://medium.com/nerd-for-tech/logging-with-logging-in-python-d3d8eb9a155a
                https://www.programcreek.com/python/example/192/logging.Formatter
"""
current_filename = os.path.basename(__file__).rsplit('.', 1)[0]
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

info_file_handler = logging.FileHandler(current_filename + '_info.log')
info_file_handler.setLevel(logging.INFO)
info_file_handler.setFormatter(formatter)

error_file_handler = logging.FileHandler(current_filename + '_error.log')
error_file_handler.setLevel(logging.ERROR)
error_file_handler.setFormatter(formatter)

critical_file_handler = logging.FileHandler(current_filename + '_critical.log')
critical_file_handler.setLevel(logging.CRITICAL)
critical_file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(info_file_handler)
logger.addHandler(error_file_handler)
logger.addHandler(critical_file_handler)

def extract(info):
    """
    Pulls all the zip files from the World Bank, unzips them, and saves to a new folder in the cwd. 

    Parameters
    ----------
    info: dictionary of data files with the indicator name as the keys and url as values.
    """
    try:
        with urlopen(info[1]) as zipFile:
            with ZipFile(BytesIO(zipFile.read())) as file:
                file.extractall('{name}'.format(name = info[0]))
    except Exception as e:
        logger.critical(e)
        exit()
    finally:
        logger.info('Extracted Successfully')

def panda_read_csv(path):
    """
    Opens each csv per folder and turns the first csv into a dataframe.

    Parameters
    ----------
    path: path of the directory holding the csv files.

    Returns
    -------
    Dataframe stores information from a specific csv.
    Acknowledgement: https://stackoverflow.com/questions/33503993/read-in-all-csv-files-from-a-directory-using-python
    """
    try:
        csv_files = glob.glob(os.path.join(path, "*.csv"))
        csv_file = csv_files[0]
        df = pd.read_csv(csv_file, skiprows=4)
        df.drop(columns = df.columns[-1], axis=1, inplace=True)
        return df
    except Exception as e:
        logger.critical(e)
        exit()
    finally:
        logger.info("csv to pd successful")

def transform_load(frames):
    """
    Transforms each dataframe into the correct format and loads them to their csv.

    Parameters
    ----------
    frames: list of dataframes from the csv files.

    Returns
    -------
    csv files with transformed data.
    """
    try:
        df_country = frames[0][["Country Name", "Country Code"]]
        logger.info("Df_country")
        logger.info(df_country.info)
        df_indicator = pd.concat(item[["Indicator Name", "Indicator Code"]].iloc[[0]] for item in frames)
        logger.info("Df_indicator")
        logger.info(df_indicator.info)
        df_year = pd.DataFrame()
        df_year["Year"] = [x for x in frames[8].columns[4:]]
        logger.info("Df_year")
        logger.info(df_year.info)
        frames = [item.drop(columns=["Country Name", "Indicator Name"]) for item in frames]
        df_fact_table = pd.concat(item for item in frames)
        logger.info("Df_fact_table")
        logger.info(df_fact_table.info)
        logger.info('End Transform')

        logger.info('Begin Load')
        df_country.to_csv("countries.csv", index=False)
        df_indicator.to_csv("indicator.csv", index=False)
        df_year.to_csv("year.csv", index=False)
        df_fact_table.to_csv("fact_table.csv", index=False)
    except Exception as e:
        logger.critical(e)
        exit()
    finally:
        logger.info('End Load')

def main():
    """
    Creates dictonary of data that then is extracted, transformed, and loaded.
    """

    dataDict = {
                "Annual population growth rate (%)" : "https://api.worldbank.org/v2/country/all/indicator/SP.POP.GROW?per_page=20000&downloadformat=csv",
                "Coverage of social insurance programs (percent of population)" : "https://api.worldbank.org/v2/country/all/indicator/per_si_allsi.cov_pop_tot?per_page=20000&downloadformat=csv",
                "Current health expenditure (percent of GDP)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.CHEX.GD.ZS?per_page=20000&downloadformat=csv",
                "Current health expenditure per capita (current US$)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.CHEX.PC.CD?per_page=20000&downloadformat=csv",
                "Domestic general government health expenditure (percent of GDP)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.GHED.GD.ZS?per_page=20000&downloadformat=csv",
                "Domestic general government health expenditure (percent of current health expenditure)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.GHED.CH.ZS?per_page=20000&downloadformat=csv",
                "Domestic general government health expenditure per capita (current US$)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.GHED.PC.CD?per_page=20000&downloadformat=csv",
                "Domestic private health expenditure per capita (current US$)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.PVTD.PC.CD?per_page=20000&downloadformat=csv",
                "GDP (current US$)" : "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?per_page=20000&downloadformat=csv",
                "GDP per capita (current US$)" : "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.PCAP.CD?per_page=20000&downloadformat=csv",
                "Inflation, GDP deflator (annual percent)" : "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.DEFL.KD.ZG?per_page=20000&downloadformat=csv",
                "More than 10 percent of income on out-of-pocket health care" : "https://api.worldbank.org/v2/country/all/indicator/SH.UHC.OOPC.10.ZS?per_page=20000&downloadformat=csv",
                "More than 25 percent of income on out-of-pocket health care" :  "https://api.worldbank.org/v2/country/all/indicator/SH.UHC.OOPC.25.ZS?per_page=20000&downloadformat=csv",
                "Out-of-pocket expenditure per capita (current US$)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.OOPC.PC.CD?per_page=20000&downloadformat=csv",
                "People pushed below the $1.90 ($ 2011 PPP) poverty line" : "https://api.worldbank.org/v2/country/all/indicator/SH.UHC.NOP1.ZS?per_page=20000&downloadformat=csv",
                "People pushed below the $3.20 ($ 2011 PPP) poverty line" : "https://api.worldbank.org/v2/country/all/indicator/SH.UHC.NOP2.ZS?per_page=20000&downloadformat=csv",
                "Physicians (per 1,000 people)" : "https://api.worldbank.org/v2/country/all/indicator/SH.MED.PHYS.ZS?per_page=20000&downloadformat=csv",
                "Population, total" : "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?per_page=20000&downloadformat=csv"
                }

    logger.info('Begin Extract')
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract, dataDict.items())
    logger.info('End Extract')

    logger.info('Begin Transform')
    cwd = os.getcwd()
    pds = []
    with concurrent.futures.ThreadPoolExecutor() as executor2:
        directories = [x[0] for x in os.walk(cwd)]
        if "__pycache__" in directories[-1]:
            del directories[-1]
        del directories[0]
        logger.info('Begin csv to pd')
        pds = list(executor2.map(panda_read_csv, directories))

    transform_load(pds)

if __name__ == '__main__':
    logger.debug('Performing ETL')
    logger.info('Performing ETL')
    logger.info('ETL Begin')
    main()
    logger.info('ETL End')
    logger.debug('ETL End')