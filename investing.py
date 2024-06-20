import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()


URL = 'https://es.investing.com/currencies/usd-ars-historical-data'
url_request = requests.get(URL, timeout=5, verify=False)
html_request = BeautifulSoup(url_request.content, 'html.parser')


def inf_ano_pasado():
    'main'
    start = str(html_request).find('52 semanas</div>')
    value = str(html_request)[start+86:start+92].replace(',', '.')
    return value
