'########## BCRA GET DATA##########'
import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()

url = 'https://www.bcra.gob.ar/'
url_request = requests.get(url, timeout=5, verify=False)
html_request = BeautifulSoup(url_request.text, 'html.parser')


def usd_mayorista_value():
    'main'
    target_td = None
    for td in html_request.find_all('td'):
        if 'Tipo de Cambio Mayorista' in td.get_text():
            target_td = td
            break
    if target_td:
        parent_tr = target_td.find_parent('tr')
        sibling_td = parent_tr.find_all('td')[1]
        value = sibling_td.find('div').text.strip()
    else:
        value = 'Error'

    return value.replace(',', '.')


def usd_mayorista_fecha():
    'main'
    target_td = None
    for td in html_request.find_all('td'):
        if 'Tipo de Cambio Mayorista' in td.get_text():
            target_td = td
            break
    if target_td:
        value = target_td.text
        value = value.split(' ')[14]
    else:
        value = 'Error'

    return value


def usd_minorista_value():
    'main'
    target_td = None
    for td in html_request.find_all('td'):
        if 'Tipo de Cambio Minorista' in td.get_text():
            target_td = td
            break
    if target_td:
        parent_tr = target_td.find_parent('tr')
        sibling_td = parent_tr.find_all('td')[1]
        value = sibling_td.find('div').text.strip()
    else:
        value = 'Error'

    return value.replace(',', '.')


def usd_minorista_fecha():
    'main'
    target_td = None
    for td in html_request.find_all('td'):
        if 'Tipo de Cambio Minorista' in td.get_text():
            target_td = td
            break
    if target_td:
        value = target_td.text
        value = value.split(' ')[15]
    else:
        value = 'Error'

    return value
