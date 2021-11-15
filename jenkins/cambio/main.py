import requests
import json
from datetime import datetime


def cotacao(valor):
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    ret = requests.get(url)
    dolar = json.loads(ret.text)["USDBRL"]
    return float(dolar["bid"]) * valor


moeda = cotacao(1)
print(f"Cotacao atual: {moeda}")

with open("cambio.csv", "a") as file:
    file.write(f"{datetime.strftime(datetime.now(),'%d/%m/%Y %H:%M')};{moeda}")
