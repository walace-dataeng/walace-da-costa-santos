import requests
import pandas as pd
from datetime import datetime

# lista de criptomoedas
moedas = "bitcoin,ethereum,solana,dogecoin"

# adicionar USD e BRL
url = f"https://api.coingecko.com/api/v3/simple/price?ids={moedas}&vs_currencies=usd,brl"

response = requests.get(url)
data = response.json()

lista = []

for moeda in data:
    lista.append({
        "coin": moeda,
        "price_usd": data[moeda]["usd"],
        "price_brl": data[moeda]["brl"],
        "timestamp": datetime.now()
    })

df = pd.DataFrame(lista)

print(df)

df.to_csv("crypto_prices.csv", index=False)
