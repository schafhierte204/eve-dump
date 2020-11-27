import json
import os
import requests
import time
from operator import itemgetter
def get_value(id):
    payload = {'datasource':'tranquility','order_type':'buy','region_id':'10000043','type_id':''}
    payload['type_id']=id
    r = requests.get("https://esi.evetech.net/latest/markets/10000043/orders", params=payload)
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
        "Tritanium":get_value(34),
        "Pyerite":get_value(35),
        "Mexallon":get_value(36),
        "Isogen":get_value(37),
        "Noxium":get_value(38),
        "Zydrine":get_value(39),
        "Megacyte":get_value(40),
        "Morphite":get_value(11399),
        }

print("Tritanium="+"{:.2f}".format(price["Tritanium"])+" Pyerite="+"{:.2f}".format(price["Pyerite"])+" Mexallon="+"{:.2f}".format(price["Mexallon"])+" Isogen="+"{:.2f}".format(price["Isogen"])+" Noxium="+"{:.2f}".format(price["Noxium"])+" Zydrine="+"{:.2f}".format(price["Zydrine"])+" Megacyte="+"{:.2f}".format(price["Megacyte"])+" Morphite="+"{:.2f}".format(price["Morphite"])+" "+str(time.ctime(time.time())))
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'output.json')
f = open(filename, "a")
f.write(json.dumps(price)+",\n")
f.close


