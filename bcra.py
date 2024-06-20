'########## BCRA GET DATA##########'
import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()

URL = 'https://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables.asp'
url_request = requests.get(URL, timeout=5, verify=False)
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
        sibling_td = parent_tr.find_all('td')[2]
        start = str(sibling_td).find('>')+1
        end = str(sibling_td).find('</td')
        value = str(sibling_td)[start:end].replace(',', '.')
    else:
        value = 'Error'
    return value


def usd_mayorista_fecha():
    'main'
    target_td = None
    for td in html_request.find_all('td'):
        if 'Tipo de Cambio Mayorista' in td.get_text():
            target_td = td
            break
    if target_td:
        parent_tr = target_td.find_parent('tr')
        sibling_td = parent_tr.find_all('td')[1]
        start = str(sibling_td).find('>')+1
        end = str(sibling_td).find('</td')
        value = str(sibling_td)[start:end].replace(',', '.')
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
        sibling_td = parent_tr.find_all('td')[2]
        start = str(sibling_td).find('>')+1
        end = str(sibling_td).find('</td')
        value = str(sibling_td)[start:end].replace(',', '.')
    else:
        value = 'Error'
    return value


def usd_minorista_fecha():
    'main'
    target_td = None
    for td in html_request.find_all('td'):
        if 'Tipo de Cambio Minorista' in td.get_text():
            target_td = td
            break
    if target_td:
        parent_tr = target_td.find_parent('tr')
        sibling_td = parent_tr.find_all('td')[1]
        start = str(sibling_td).find('>')+1
        end = str(sibling_td).find('</td')
        value = str(sibling_td)[start:end].replace(',', '.')
    else:
        value = 'Error'
    return value


def tasa_politica_monetaria_value():
    'main'
    target_td = None
    for td in html_request.find_all('td'):
        if 'Tasa de Política Monetaria' in td.get_text():
            target_td = td
            break
    if target_td:
        parent_tr = target_td.find_parent('tr')
        sibling_td = parent_tr.find_all('td')[2]
        start = str(sibling_td).find('>')+1
        end = str(sibling_td).find('</td')
        value = str(sibling_td)[start:end].replace(',', '.')
    else:
        value = 'Error'
    return value


def tasa_politica_monetaria_fecha():
    'main'
    target_td = None
    for td in html_request.find_all('td'):
        if 'Tasa de Política Monetaria' in td.get_text():
            target_td = td
            break
    if target_td:
        parent_tr = target_td.find_parent('tr')
        sibling_td = parent_tr.find_all('td')[1]
        start = str(sibling_td).find('>')+1
        end = str(sibling_td).find('</td')
        value = str(sibling_td)[start:end].replace(',', '.')
    else:
        value = 'Error'
    return value


def plazo_fijo_value():
    'main'
    target_td = None
    for td in html_request.find_all('td'):
        if 'Tasas de interés por depósitos a 30 días' in td.get_text():
            target_td = td
            break
    if target_td:
        parent_tr = target_td.find_parent('tr')
        sibling_td = parent_tr.find_all('td')[2]
        start = str(sibling_td).find('>')+1
        end = str(sibling_td).find('</td')
        value = str(sibling_td)[start:end].replace(',', '.')
    else:
        value = 'Error'
    return value


def plazo_fijo_fecha():
    'main'
    target_td = None
    for td in html_request.find_all('td'):
        if 'Tasas de interés por depósitos a 30 días' in td.get_text():
            target_td = td
            break
    if target_td:
        parent_tr = target_td.find_parent('tr')
        sibling_td = parent_tr.find_all('td')[1]
        start = str(sibling_td).find('>')+1
        end = str(sibling_td).find('</td')
        value = str(sibling_td)[start:end].replace(',', '.')
    else:
        value = 'Error'
    return value


def inflacion_value():
    'main'
    target_td = None
    for td in html_request.find_all('td'):
        if 'Inflación mensual' in td.get_text():
            target_td = td
            break
    if target_td:
        parent_tr = target_td.find_parent('tr')
        sibling_td = parent_tr.find_all('td')[2]
        start = str(sibling_td).find('>')+1
        end = str(sibling_td).find('</td')
        value = str(sibling_td)[start:end].replace(',', '.')
    else:
        value = 'Error'
    return value


def inflacion_fecha():
    'main'
    target_td = None
    for td in html_request.find_all('td'):
        if 'Inflación mensual' in td.get_text():
            target_td = td
            break
    if target_td:
        parent_tr = target_td.find_parent('tr')
        sibling_td = parent_tr.find_all('td')[1]
        start = str(sibling_td).find('>')+1
        end = str(sibling_td).find('</td')
        value = str(sibling_td)[start:end].replace(',', '.')
    else:
        value = 'Error'
    return value


def inflacion_inter_value():
    'main'
    target_td = None
    for td in html_request.find_all('td'):
        if 'Inflación interanual' in td.get_text():
            target_td = td
            break
    if target_td:
        parent_tr = target_td.find_parent('tr')
        sibling_td = parent_tr.find_all('td')[2]
        start = str(sibling_td).find('>')+1
        end = str(sibling_td).find('</td')
        value = str(sibling_td)[start:end].replace(',', '.')
    else:
        value = 'Error'
    return value


def inflacion_inter_fecha():
    'main'
    target_td = None
    for td in html_request.find_all('td'):
        if 'Inflación interanual' in td.get_text():
            target_td = td
            break
    if target_td:
        parent_tr = target_td.find_parent('tr')
        sibling_td = parent_tr.find_all('td')[1]
        start = str(sibling_td).find('>')+1
        end = str(sibling_td).find('</td')
        value = str(sibling_td)[start:end].replace(',', '.')
    else:
        value = 'Error'
    return value


def inflacion_esperada_value():
    'main'
    target_td = None
    for td in html_request.find_all('td'):
        if 'Inflación esperada' in td.get_text():
            target_td = td
            break
    if target_td:
        parent_tr = target_td.find_parent('tr')
        sibling_td = parent_tr.find_all('td')[2]
        start = str(sibling_td).find('>')+1
        end = str(sibling_td).find('</td')
        value = str(sibling_td)[start:end].replace(',', '.')
    else:
        value = 'Error'
    return value


def inflacion_esperada_fecha():
    'main'
    target_td = None
    for td in html_request.find_all('td'):
        if 'Inflación esperada' in td.get_text():
            target_td = td
            break
    if target_td:
        parent_tr = target_td.find_parent('tr')
        sibling_td = parent_tr.find_all('td')[1]
        start = str(sibling_td).find('>')+1
        end = str(sibling_td).find('</td')
        value = str(sibling_td)[start:end].replace(',', '.')
    else:
        value = 'Error'
    return value
