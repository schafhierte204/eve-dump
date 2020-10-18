import json
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

print("Tritanium="+"{:.2f}".format(get_value(34))+" Pyereite="+"{:.2f}".format(get_value(35))+" Mexallon="+"{:.2f}".format(get_value(36))+" Isogen="+"{:.2f}".format(get_value(37))+" Noxium="+"{:.2f}".format(get_value(38))+" Zydrine="+"{:.2f}".format(get_value(39))+" Megacyte="+"{:.2f}".format(get_value(40))+" Morphite="+"{:.2f}".format(get_value(11399))+" "+str(time.ctime(time.time())))
