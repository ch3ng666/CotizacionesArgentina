'USD Mayorista Extract'
import requests
from bs4 import BeautifulSoup


def func_usd_mayorista():
    'main'
    url = 'https://www.bna.com.ar/Cotizador/MonedasHistorico'
    url_request = requests.get(url, timeout=5)
    html_request = BeautifulSoup(url_request.text, 'html.parser')
    valor_1 = html_request.find_all('td')[2]
    valor_2 = valor_1.contents[0]
    return valor_2


usd_mayorista_value = func_usd_mayorista()
