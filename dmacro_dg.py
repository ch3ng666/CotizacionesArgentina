'################ DATOSMACRO GET DATA ##################'
# Merval, Merval USD, S&P
import re
import requests
from bs4 import BeautifulSoup


def datosmacro_data_get():
    'Main'

    # S&P

    url = 'https://datosmacro.expansion.com/paises/argentina'
    url_request = requests.get(url, timeout=5)
    html_request = BeautifulSoup(url_request.text, 'html.parser')

    step1 = html_request.find('a', href=re.compile('.ratings.'))
    s_and_p = list(step1.parent.parent.next_sibling)[2].text

    # Merval

    url = 'https://datosmacro.expansion.com/bolsa/argentina'
    url_request = requests.get(url, timeout=5)
    html_request = BeautifulSoup(url_request.text, 'html.parser')

    merval = html_request.find('td', class_='numero').text
    merval = float(merval.replace('.', '').replace(',', '.'))

    datos = {'S&P': s_and_p, 'Merval': merval}

    return datos
