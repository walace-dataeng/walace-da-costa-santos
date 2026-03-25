import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados.csv")

print(df)

df["faturamento"] = df["preco"] * df["quantidade"]

print(df)

df.plot(x="produto", y="faturamento", kind="bar")
plt.show()
