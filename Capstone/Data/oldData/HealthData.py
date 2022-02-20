import json
import concurrent.futures
import time
from urllib.request import Request, urlopen

t1 = time.perf_counter()

dataDict = {"Hospital Provider Cost Report" : "https://data.cms.gov/data-api/v1/dataset/44060663-47d8-4ced-a115-b53b4c270acb/data",
            "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries" : "https://data.cms.gov/data-api/v1/dataset/5f9f1216-6fd9-455d-bfbc-0efade687a4e/data"
            }

def pullData(item):
    request = Request(item[1], headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(request) as response:
        source = response.read()
        with open("healthdata/{name}.json".format(name = item[0]), 'w') as file:
            data = json.loads(source)
            json.dump(data, file)


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(pullData, dataDict.items())

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')