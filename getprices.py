import json
import os
import requests
import time
from operator import itemgetter
def get_value(id,region):
    payload = {'datasource':'tranquility','order_type':'buy','region_id':'','type_id':''}
    payload['type_id']=id
    payload['region_id']=region
    site = "https://esi.evetech.net/latest/markets/"+str(region)+"/orders"
    r = requests.get(site, params=payload)
    orders=json.loads(r.text)
    orders = sorted(orders, key=itemgetter('price'), reverse=True)
    i= 0
    l =len(orders)
    if l!=0:
        volume=100000000
        while volume>0:
            if i==l:
                break

            volume= volume-orders[i]['volume_remain']
            i=i+1

        average=[]
        for j in range(0,i):
            average.append(orders[j]['price'])
        return(sum(average)/len(average))
    else:
        return 0;

price = {
        "Tritanium":[get_value(34,10000043),get_value(34,10000002)],
        "Pyerite":[get_value(35,10000043),get_value(35,10000002)],
        "Mexallon":[get_value(36,10000043),get_value(36,10000002)],
        "Isogen":[get_value(37,10000043),get_value(37,10000002)],
        "Noxium":[get_value(38,10000043),get_value(38,10000002)],
        "Zydrine":[get_value(39,10000043),get_value(39,10000002)],
        "Megacyte":[get_value(40,10000043),get_value(40,10000002)],
        "Morphite":[get_value(11399,10000043),get_value(11399,10000002)],
        }

print("Domain: "+"Tritanium="+"{:.2f}".format(price["Tritanium"][0])+" Pyerite="+"{:.2f}".format(price["Pyerite"][0])+" Mexallon="+"{:.2f}".format(price["Mexallon"][0])+" Isogen="+"{:.2f}".format(price["Isogen"][0])+" Noxium="+"{:.2f}".format(price["Noxium"][0])+" Zydrine="+"{:.2f}".format(price["Zydrine"][0])+" Megacyte="+"{:.2f}".format(price["Megacyte"][0])+" Morphite="+"{:.2f}".format(price["Morphite"][0])+"\n"
  "The Forge: "+"Tritanium="+"{:.2f}".format(price["Tritanium"][1])+" Pyerite="+"{:.2f}".format(price["Pyerite"][1])+" Mexallon="+"{:.2f}".format(price["Mexallon"][1])+" Isogen="+"{:.2f}".format(price["Isogen"][1])+" Noxium="+"{:.2f}".format(price["Noxium"][1])+" Zydrine="+"{:.2f}".format(price["Zydrine"][1])+" Megacyte="+"{:.2f}".format(price["Megacyte"][1])+" Morphite="+"{:.2f}".format(price["Morphite"][1])+" "+str(time.ctime(time.time())))
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'output.json')
f = open(filename, "a")
f.write(json.dumps(price)+",\n")
f.close


