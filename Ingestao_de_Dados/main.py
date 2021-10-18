# Imports
import json
import requests

# url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
# answer = requests.get(url)

# if answer:
#     print(answer.text)
# else:
#     print(f'{answer.status_code} --> A requisição falhou!')
    
# json.loads(answer.text)['USDBRL']

def cotacao(valor,moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
    answer = requests.get(url)
    dolar = json.loads(answer.text)[moeda.replace('-','')]
    print(f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")
    
cotacao(20,'USD-BRL')