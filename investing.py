################ INVESTING GET DATA ##################
import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()


URL = 'https://es.investing.com/currencies/usd-ars-historical-data'
url_request = requests.get(URL, timeout=5, verify=False)
html_request = BeautifulSoup(url_request.content, 'html.parser')


def inf_ano_pasado():
    step1 = html_request.find(string='52 semanas',)
    step2 = step1.parent.parent
    step3 = step2.span.string
    step4 = round(float(step3.replace(',', '.')), 2)
    return step4
