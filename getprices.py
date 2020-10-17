import json
import requests
payload = {'datasource':'tranquility','order_type':'sell','region_id':'10000043','type_id':'52306'}
r = requests.get("https://esi.evetech.net/latest/markets/10000043/orders", params=payload)
orders=json.loads(r.text)
average =[]
for i in orders:
    average.append(i["price"])

print(sum(average)/len(average))
