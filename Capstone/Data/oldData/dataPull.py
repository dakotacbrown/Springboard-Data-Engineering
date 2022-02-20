import json
from urllib.request import Request, urlopen


req = Request("https://apps.who.int/gho/athena/api/GHO/WHS7_139.json", headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(req) as response:
    source = response.read()
    with open("WHO/Out-of-pocket expenditure.json", 'w') as file:
        data = json.loads(source)
        json.dump(data, file)

finance = Request("https://apps.who.int/gho/athena/api/GHO/FINPROTECTION_CATA_ESTIMATE_AVAILABLE,FINPROTECTION_IMPOV_ESTIMATE_AVAILABLE,FINPROTECTION_IMP_PG_190_STD,FINPROTECTION_IMP_PG_190,FINPROTECTION_IMP_PG_310_STD,FINPROTECTION_IMP_PG_310,FINPROTECTION_CATA_TOT_10_LEVEL_SH,FINPROTECTION_CATA_TOT_10_LEVEL_MILLION,FINPROTECTION_CATA_TOT_25_LEVEL_SH,FINPROTECTION_CATA_TOT_25_LEVEL_MILLION,FINPROTECTION_IMP_NP_190_LEVEL_SH,FINPROTECTION_IMP_NP_190_LEVEL_MILLION,FINPROTECTION_IMP_NP_310_LEVEL_SH,FINPROTECTION_IMP_NP_310_LEVEL_MILLION.json", headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(finance) as finRes:
    finSrc = finRes.read()
    with open("WHO/finance.json", 'w') as file:
        data = json.loads(finSrc)
        json.dump(data, file)