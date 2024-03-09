import requests
import json
from coinapi_config import API_KEY
from coinapi_config import BASE_URL


url = BASE_URL + 'v1/assets' #+ "?apikey=" + API_KEY

headers = {'X-CoinAPI-Key': API_KEY}
response = requests.get(url, headers=headers)

# 200 /sinon afficher le code d'erreur
if response.status_code == 200:
    print("L'appel à l'API a fonctionné")
    data = json.loads(response.text)
    nb_assets = len(data)
    # asset_id

    #name
    print("Nombre d'assets monetaire:", nb_assets)
    if nb_assets >= 10:
        for i in range(10):
            d = data[i]
            print(d['asset_id'] + ":" + d['name'])
        print()
        print("Quota restant:", response.headers["x-ratelimit-remaining"])
else:
    # cas d'erreur
    print("L'appel à l'api a retourné une erreur: ", response.status_code)



