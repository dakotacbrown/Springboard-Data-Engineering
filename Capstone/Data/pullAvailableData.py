import concurrent.futures
import time
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO

t1 = time.perf_counter()

dataDict = {
            # working files from world bank
            "Annual population growth rate (%)" : "https://api.worldbank.org/v2/country/all/indicator/SP.POP.GROW?per_page=20000&downloadformat=csv",
            "Coverage of social insurance programs (percent of population)" : "https://api.worldbank.org/v2/country/all/indicator/per_si_allsi.cov_pop_tot?per_page=20000&downloadformat=csv",
            "Current health expenditure (percent of GDP)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.CHEX.GD.ZS?per_page=20000&downloadformat=csv",
            "Domestic general government health expenditure (percent of GDP)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.GHED.GD.ZS?per_page=20000&downloadformat=csv",
            "Domestic general government health expenditure (percent of current health expenditure)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.GHED.CH.ZS?per_page=20000&downloadformat=csv",
            "Inflation, GDP deflator (annual percent)" : "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.DEFL.KD.ZG?per_page=20000&downloadformat=csv",
            "People pushed below the $1.90 ($ 2011 PPP) poverty line" : "https://api.worldbank.org/v2/country/all/indicator/SH.UHC.NOP1.TO?per_page=20000&downloadformat=csv",
            "People pushed below the $3.20 ($ 2011 PPP) poverty line" : "https://api.worldbank.org/v2/country/all/indicator/SH.UHC.NOP2.TO?per_page=20000&downloadformat=csv",
            "Physicians (per 1,000 people)" : "https://api.worldbank.org/v2/country/all/indicator/SH.MED.PHYS.ZS?per_page=20000&downloadformat=csv",
            "Population, total" : "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?per_page=20000&downloadformat=csv",
            "More than 10 percent of income on out-of-pocket health care" : "https://api.worldbank.org/v2/country/all/indicator/SH.UHC.OOPC.10.ZS?per_page=20000&downloadformat=csv",
            "More than 25 percent of income on out-of-pocket health care" :  "https://api.worldbank.org/v2/country/all/indicator/SH.UHC.OOPC.25.ZS?per_page=20000&downloadformat=csv",
            # files currently unable to download due to website errors
            "Current health expenditure per capita (current US$)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.CHEX.PC.CD?per_page=20000&downloadformat=csv",
            "Domestic general government health expenditure per capita (current US$)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.GHED.PC.CD?per_page=20000&downloadformat=csv",
            "Domestic private health expenditure per capita (current US$)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.PVTD.PC.CD?per_page=20000&downloadformat=csv",
            "GDP (current US$)" : "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?per_page=20000&downloadformat=csv",
            "GDP per capita (current US$)" : "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.PCAP.CD?per_page=20000&downloadformat=csv",
            "Out-of-pocket expenditure per capita (current US$)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.OOPC.PC.CD?per_page=20000&downloadformat=csv"
            }

def pullData(item):
    with urlopen(item[1]) as zipFile:
        with ZipFile(BytesIO(zipFile.read())) as file:
            file.extractall('{name}'.format(name = item[0]))

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(pullData, dataDict.items())

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')