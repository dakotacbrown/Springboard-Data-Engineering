import json
import concurrent.futures
import time
from urllib.request import Request, urlopen

t1 = time.perf_counter()

dataDict = {
            "Coverage of social insurance programs (\% \of population)" : "https://api.worldbank.org/v2/country/all/indicator/per_si_allsi.cov_pop_tot?format=json",
            "Inflation, GDP deflator (annual \%)" : "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.DEFL.KD.ZG?format=json",
            "GDP (current US$)" : "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json",
            "Domestic general government health expenditure (\% \of GDP)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.GHED.GD.ZS?format=json",
            "Domestic general government health expenditure (\% \of current health expenditure)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.GHED.CH.ZS?format=json",
            "Current health expenditure per capita (current US$)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.CHEX.PC.CD?format=json",
            "Out-of-pocket expenditure per capita (current US$)" : "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.OOPC.PC.CD?format=json",
            "Physicians (per 1,000 people)" : "https://api.worldbank.org/v2/country/all/indicator/SH.MED.PHYS.ZS?format=json"
            }

def pullData(item):
    request = Request(item[1], headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(request) as response:
        source = response.read()
        with open("worldBank/{name}.json".format(name = item[0]), 'w') as file:
            data = json.loads(source)
            json.dump(data, file)


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(pullData, dataDict.items())

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')