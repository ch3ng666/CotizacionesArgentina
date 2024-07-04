################ INVESTING GET DATA ##################
import requests
from bs4 import BeautifulSoup
import urllib3
import re

urllib3.disable_warnings()


URL = 'https://es.investing.com/currencies/usd-ars-historical-data'
url_request = requests.get(URL, timeout=5, verify=False)
html_request = BeautifulSoup(url_request.content, 'html.parser')


def usd_ano_pasado():
    step1 = html_request.find('div', string=re.compile('52 semanas'))
    return step1


print(html_request)
