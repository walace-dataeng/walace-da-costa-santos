import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

response = requests.get(url)
data = response.json()

lista = []

for moeda in data:
    lista.append({
        "coin": moeda,
        "price_usd": data[moeda]["usd"]
    })

df = pd.DataFrame(lista)

print(df)

df.to_csv("crypto_prices.csv", index=False)
