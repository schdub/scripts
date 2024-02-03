import math
import requests

def volHostV2(e):
    if e >= 0 and e <= 143:
        t = "01"
    elif e >= 144 and e <= 287:
        t = "02"
    elif e >= 288 and e <= 431:
        t = "03"
    elif e >= 432 and e <= 719:
        t = "04"
    elif e >= 720 and e <= 1007:
        t = "05"
    elif e >= 1008 and e <= 1061:
        t = "06"
    elif e >= 1062 and e <= 1115:
        t = "07"
    elif e >= 1116 and e <= 1169:
        t = "08"
    elif e >= 1170 and e <= 1313:
        t = "09"
    elif e >= 1314 and e <= 1601:
        t = "10"
    elif e >= 1602 and e <= 1655:
        t = "11"
    elif e >= 1656 and e <= 1919:
        t = "12"
    elif e >= 1920 and e <= 2045:
        t = "13"
    elif e >= 2046 and e <= 2189:
        t = "14"
    else:
        t = "15"
    return "basket-{0}.wbbasket.ru".format(t)

def constructHostV2(e):
    r = int(e)
    n = math.floor(r / 1e5)
    a = math.floor(r / 1e3)
    return "https://{0}/vol{1}/part{2}/{3}".format(volHostV2(n),n,a,r)

def urlPriceHistoryStatic(e):
    return "{0}/info/price-history.json".format(constructHostV2(e))

priceUrlJson = urlPriceHistoryStatic(140481361)
print(priceUrlJson)
x = requests.get(priceUrlJson)
print(x.content)