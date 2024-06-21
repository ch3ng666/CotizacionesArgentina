'########## DOLARHoy GET DATA##########'
import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()

url = 'https://dolarhoy.com/'
url_request = requests.get(url, timeout=5).text
html_request = BeautifulSoup(url_request, 'html.parser')


def usd_mep_value():
    step1 = html_request.find_all(class_='title', href="/cotizaciondolarbolsa")
    step2 = step1[0].next_sibling
    step3 = step2.find(class_='label', string='Venta').next_sibling.text
    step4 = step3.strip('$')
    return step4


def usd_mepcclcryp_fechas():
    step1 = html_request.find_all(class_='title', href="/cotizaciondolarblue")
    step2 = step1[0].parent
    step3 = step2.find(class_='tile update').text
    step4 = (step3.strip('Actualizado el ')[:-9].split('/'))
    step4[2] = '2024'
    step5 = '/'.join(step4)
    return step5


print(usd_mepcclcryp_fechas())


def usd_ccl_value():
    step1 = html_request.find_all(
        class_='title', href="/cotizaciondolarcontadoconliqui")
    step2 = step1[0].next_sibling
    step3 = step2.find(class_='label', string='Venta').next_sibling.text
    step4 = step3.strip('$')
    return step4


def usd_crypto_value():
    step1 = html_request.find_all(class_='title', href="/seccion/bitcoins")
    step2 = step1[0].next_sibling
    step3 = step2.find(class_='label', string='Venta').next_sibling.text
    step4 = step3.strip('$')
    return step4


def usd_blue_value():
    step1 = html_request.find_all(class_='title', href="/cotizaciondolarblue")
    step2 = step1[0].next_sibling
    step3 = step2.find(class_='label', string='Venta').next_sibling.text
    step4 = step3.strip('$')
    return step4
