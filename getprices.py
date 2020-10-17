import json
import requests
payload = {'datasource':'tranquility','order_type':'sell','region_id':'10000043','type_id':'52306'}
r = requests.get("https://esi.evetech.net/latest/markets/10000043/orders", params=payload)
orders=json.loads(r.text)
average =[]
low = orders[0]["price"]
for i in orders:
    average.append(i["price"])
    if low>i["price"]:
        low = i["price"]

print(" Durchsnitt="+str(sum(average)/len(average))+" Tiefstpreis="+str(low))
