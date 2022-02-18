import json
import concurrent.futures
import time
from urllib.request import Request, urlopen

t1 = time.perf_counter()

dataDict = {"finance10per" : "https://apps.who.int/gho/athena/api/GHO/FINPROTECTION_CATA_TOT_10_POP,FINPROTECTION_CATA_TOT_10_LEVEL_SH,FINPROTECTION_CATA_TOT_10_LEVEL_MILLION.json",
            "finance25per" :  "https://apps.who.int/gho/athena/api/GHO/FINPROTECTION_CATA_TOT_25_LEVEL_SH,FINPROTECTION_CATA_TOT_25_LEVEL_MILLION,FINPROTECTION_CATA_TOT_25_POP.json", 
            "finance190" : "https://apps.who.int/gho/athena/api/GHO/FINPROTECTION_IMP_NP190_POP,FINPROTECTION_IMP_PG_190_STD,FINPROTECTION_IMP_PG_190,FINPROTECTION_IMP_P190_POP,FINPROTECTION_IMP_P190_LEVEL_SH,FINPROTECTION_IMP_P190_LEVEL_MILLION,FINPROTECTION_IMP_NP_190_LEVEL_SH,FINPROTECTION_IMP_NP_190_LEVEL_MILLION.json",
            "finance310" : "https://apps.who.int/gho/athena/api/GHO/FINPROTECTION_IMP_P310_POP,FINPROTECTION_IMP_PG_310_STD,FINPROTECTION_IMP_PG_310,FINPROTECTION_IMP_NP_310_LEVEL_SH,FINPROTECTION_IMP_NP_310_LEVEL_MILLION,FINPROTECTION_IMP_NP310_POP,FINPROTECTION_IMP_P310_LEVEL_SH,FINPROTECTION_IMP_P310_LEVEL_MILLION.json",
            "healthExpenditures" : "https://apps.who.int/gho/athena/api/GHO/WHS7_103,WHS7_120,WHS7_134,WHS7_139,WHS7_143,WHS7_150,WHS4_154,WHS7_156.json",
            "medicines" : "https://apps.who.int/gho/athena/api/GHO/MDG_0000000010,MDG_0000000011,WHS6_101,WHS6_116.json",
            "nhaData" : "https://apps.who.int/gho/athena/api/GHO/NHAGGHEGDP,NHAOOPSTHE,NHAPREPAIDTHE.json",
            "poverty" : "https://apps.who.int/gho/athena/api/GHO/FINPROTECTION_IMP_PRELPL_POP,FINPROTECTION_CATA_ESTIMATE_AVAILABLE,FINPROTECTION_IMPOV_ESTIMATE_AVAILABLE,FINPROTECTION_IMP_NP_REL_LEVEL_SH,FINPROTECTION_CATA_CTPFHU_40_HH,FINPROTECTION_IMP_BNLFHU_TOT_HH,FINPROTECTION_IMP_BNLFHU_P_HH,FINPROTECTION_IMP_BNLFHU_FURIMP_HH,FINPROTECTION_IMP_NPRELPL_POP,FINPROTECTION_IMP_PG_RELPL_STD,FINPROTECTION_IMP_PREL_LEVEL_SH,FINPROTECTION_IMP_PREL_LEVEL_MILLION.json",
            "population" : "https://apps.who.int/gho/athena/api/GHO/WHS9_86,WHS9_88,WHS9_89,WHS9_90,WHS9_92,WHS9_96,WHS9_97.json",
            "universalHealthcare": "https://apps.who.int/gho/athena/api/GHO/GOE_Q001,UHC_DATA_AVAIL_CODE,UHC_INDEX_REPORTED,UHC_INDEX_ACTUAL,UHC_AVAILABILITY_SCORE.json"
            }

def pullData(item):
    request = Request(item[1], headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(request) as response:
        source = response.read()
        with open("WHO/{name}.json".format(name = item[0]), 'w') as file:
            data = json.loads(source)
            json.dump(data, file)


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(pullData, dataDict.items())

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')