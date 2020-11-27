import json
import os
import requests
import time
from operator import itemgetter
dirname = os.path.dirname(__file__)
filename=os.path.join(dirname,'outputMineral.json')

def get_value(id):
    payload = {'datasource':'tranquility','order_type':'buy','region_id':'10000043','type_id':''}
    payload['type_id']=id
    r = requests.get("https://esi.evetech.net/latest/markets/10000043/orders", params=payload)
    orders=json.loads(r.text)
    orders = sorted(orders, key=itemgetter('price'), reverse=True)
    return orders[0]['price']

price = {
        "Veldspar":get_value(1230),
        "DVeldspar":get_value(17471),
        "CoVeldspar":get_value(17470),
        "CVeldspar":get_value(28432),
        "CDVeldspar":get_value(28431),
        "CCoVeldspar":get_value(28430),
        "Pyroxeres":get_value(1224),
        "SPyroxeres":get_value(17459),
        "VPyroxeres":get_value(17460),
        "CPyroxeres":get_value(28424),
        "CSPyroxeres":get_value(28425),
        "CVPyroxeres":get_value(28426),
        "Scoredite":get_value(1228),
        "MScoredite":get_value(17464),
        "CoScoredite":get_value(17463),
        "CScoredite":get_value(28429),
        "CMScoredite":get_value(28428),
        "CCoScoredite":get_value(28427)
        }
with open(filename, "a") as file:
    file.write(json.dumps(price)+",")
