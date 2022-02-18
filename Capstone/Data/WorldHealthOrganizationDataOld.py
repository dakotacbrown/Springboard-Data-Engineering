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

"""
finance10 = Request("https://apps.who.int/gho/athena/api/GHO/FINPROTECTION_CATA_TOT_10_POP,FINPROTECTION_CATA_TOT_10_LEVEL_SH,FINPROTECTION_CATA_TOT_10_LEVEL_MILLION.json", headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(finance10) as f10Res:
    f10Src = f10Res.read()
    with open("WHO/finance10per.json", 'w') as f10File:
        f10Dat = json.loads(f10Src)
        json.dump(f10Dat, f10File)

finance25 = Request("https://apps.who.int/gho/athena/api/GHO/FINPROTECTION_CATA_TOT_25_LEVEL_SH,FINPROTECTION_CATA_TOT_25_LEVEL_MILLION,FINPROTECTION_CATA_TOT_25_POP.json", headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(finance25) as f25Res:
    f25Src = f25Res.read()
    with open("WHO/finance25per.json", 'w') as f25File:
        f25Dat = json.loads(f25Src)
        json.dump(f25Dat, f25File)

finance190 = Request("https://apps.who.int/gho/athena/api/GHO/FINPROTECTION_IMP_NP190_POP,FINPROTECTION_IMP_PG_190_STD,FINPROTECTION_IMP_PG_190,FINPROTECTION_IMP_P190_POP,FINPROTECTION_IMP_P190_LEVEL_SH,FINPROTECTION_IMP_P190_LEVEL_MILLION,FINPROTECTION_IMP_NP_190_LEVEL_SH,FINPROTECTION_IMP_NP_190_LEVEL_MILLION.json", headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(finance190) as f190Res:
    f190Src = f190Res.read()
    with open("WHO/finance190.json", 'w') as f190File:
        f190Dat = json.loads(f190Src)
        json.dump(f190Dat, f190File)

finance310 = Request("https://apps.who.int/gho/athena/api/GHO/FINPROTECTION_IMP_P310_POP,FINPROTECTION_IMP_PG_310_STD,FINPROTECTION_IMP_PG_310,FINPROTECTION_IMP_NP_310_LEVEL_SH,FINPROTECTION_IMP_NP_310_LEVEL_MILLION,FINPROTECTION_IMP_NP310_POP,FINPROTECTION_IMP_P310_LEVEL_SH,FINPROTECTION_IMP_P310_LEVEL_MILLION.json", headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(finance310) as f310Res:
    f310Src = f310Res.read()
    with open("WHO/finance310.json", 'w') as f310File:
        f310Dat = json.loads(f310Src)
        json.dump(f310Dat, f310File)

poverty = Request("https://apps.who.int/gho/athena/api/GHO/FINPROTECTION_IMP_PRELPL_POP,FINPROTECTION_CATA_ESTIMATE_AVAILABLE,FINPROTECTION_IMPOV_ESTIMATE_AVAILABLE,FINPROTECTION_IMP_NP_REL_LEVEL_SH,FINPROTECTION_CATA_CTPFHU_40_HH,FINPROTECTION_IMP_BNLFHU_TOT_HH,FINPROTECTION_IMP_BNLFHU_P_HH,FINPROTECTION_IMP_BNLFHU_FURIMP_HH,FINPROTECTION_IMP_NPRELPL_POP,FINPROTECTION_IMP_PG_RELPL_STD,FINPROTECTION_IMP_PREL_LEVEL_SH,FINPROTECTION_IMP_PREL_LEVEL_MILLION.json", headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(poverty) as povRes:
    povSrc = povRes.read()
    with open("WHO/poverty.json", 'w') as povFile:
        povDat = json.loads(povSrc)
        json.dump(povDat, povFile)

population = Request("https://apps.who.int/gho/athena/api/GHO/WHS9_86,WHS9_88,WHS9_89,WHS9_90,WHS9_92,WHS9_96,WHS9_97.json", headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(population) as popRes:
    popSrc = popRes.read()
    with open("WHO/population.json", 'w') as popFile:
        popDat = json.loads(popSrc)
        json.dump(popDat, popFile)

medicines = Request("https://apps.who.int/gho/athena/api/GHO/MDG_0000000010,MDG_0000000011,WHS6_101,WHS6_116.json", headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(medicines) as medRes:
    medSrc = medRes.read()
    with open("WHO/medicines.json", 'w') as medFile:
        medDat = json.loads(medSrc)
        json.dump(medDat, medFile)

healthExp = Request("https://apps.who.int/gho/athena/api/GHO/WHS7_103,WHS7_120,WHS7_134,WHS7_139,WHS7_143,WHS7_150,WHS4_154,WHS7_156.json", headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(healthExp) as heRes:
    heSrc = heRes.read()
    with open("WHO/health-expenditure.json", 'w') as heFile:
        heDat = json.loads(heSrc)
        json.dump(heDat, heFile)

universalHealthcare = Request("https://apps.who.int/gho/athena/api/GHO/GOE_Q001,UHC_DATA_AVAIL_CODE,UHC_INDEX_REPORTED,UHC_INDEX_ACTUAL,UHC_AVAILABILITY_SCORE.json", headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(universalHealthcare) as uhcRes:
    uhcSrc = uhcRes.read()
    with open("WHO/universalhealthcare.json", 'w') as uhcFile:
        uhcDat = json.loads(uhcSrc)
        json.dump(uhcDat, uhcFile)

NHAData = Request("https://apps.who.int/gho/athena/api/GHO/NHAGGHEGDP,NHAOOPSTHE,NHAPREPAIDTHE.json", headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(NHAData) as nhaRes:
    nhaSrc = nhaRes.read()
    with open("WHO/nhadata.json", 'w') as nhaFile:
        nhaDat = json.loads(nhaSrc)
        json.dump(nhaDat, nhaFile)
"""