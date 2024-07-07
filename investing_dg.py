'Investing Data Get'
import re
import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()


URL = 'https://es.investing.com/currencies/usd-ars-historical-data'
url_request = requests.get(URL, timeout=5, verify=False)
html_request = BeautifulSoup(url_request.content, 'html.parser')


def usd_ano_pasado():
    'Dolar año pasado'
    step1 = html_request.find('div', string=re.compile('52 semanas'))
    step2 = step1.next_sibling
    step3 = step2.span.string
    step4 = round(float(step3.replace(',', '.')), 2)
    return step4
