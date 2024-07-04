'########## Ambito GET DATA##########'
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.ambito.com/contenidos/dolar.html', timeout=0)
    url_request = page.content()
    browser.close()

html_request = BeautifulSoup(url_request, 'html.parser')
html_prettified = html_request.prettify()

# pylint: disable=C0301

# Get data of: Dolar Mayorista, Dolar Minorista, Dolar MEP, Dolar CCL, Dolar Crypto, Dolar Blue, Euro Minorista, Euro Blue
# Value of Dolar Solidario, Dolar Inflacion, Euro Mayorista and Euro Crypto gets calculated.

FC_DOLAR_SOLIDARIO = 1.57
FC_DOLAR_INFLACION = 3.57  # ARREGLAR


def ambito_data_get():
    'Main'

    # Dolar Mayorista

    step1 = html_request.find('div', attrs={"data-indice": '/dolar/mayorista'})  # nopep8
    usd_may_compra = step1.find('span', attrs={"class": "variation-max-min__value data-valor data-compra"}).text  # nopep8
    usd_may_venta = step1.find('span', attrs={"class": "variation-max-min__value data-valor data-venta"}).text  # nopep8
    usd_may_fecha = step1.find('span', attrs={"class": "variation-max-min__date-time data-fecha"}).text  # nopep8
    usd_may_compra = round(float(usd_may_compra.replace(',', '.')), 2)
    usd_may_venta = round(float(usd_may_venta.replace(',', '.')), 2)
    usd_mayorista = {'Compra': usd_may_compra, 'Venta': usd_may_venta, 'Fecha': usd_may_fecha}  # nopep8

    # Dolar Minorista

    step1 = html_request.find('div', attrs={"data-indice": '/dolar/oficial'})  # nopep8
    usd_min_compra = step1.find('span', attrs={"class": "variation-max-min__value data-valor data-compra"}).text  # nopep8
    usd_min_venta = step1.find('span', attrs={"class": "variation-max-min__value data-valor data-venta"}).text  # nopep8
    usd_min_fecha = step1.find('span', attrs={"class": "variation-max-min__date-time data-fecha"}).text  # nopep8
    usd_min_compra = round(float(usd_min_compra.replace(',', '.')), 2)
    usd_min_venta = round(float(usd_min_venta.replace(',', '.')), 2)
    usd_minorista = {'Compra': usd_min_compra, 'Venta': usd_min_venta, 'Fecha': usd_min_fecha}  # nopep8

    # Dolar MEP

    step1 = html_request.find('div', attrs={"data-indice": '/dolarrava/mep'})  # nopep8
    # usd_mep_compra = step1.find('span', attrs={"class": "variation-max-min__value data-valor"}).text  # nopep8
    usd_mep_venta = step1.find('span', attrs={"class": "variation-max-min__value data-valor"}).text  # nopep8
    usd_mep_fecha = step1.find('span', attrs={"class": "variation-max-min__date-time data-fecha"}).text  # nopep8
    usd_mep_venta = round(float(usd_mep_venta.replace(',', '.')), 2)
    usd_mep = {'Venta': usd_mep_venta, 'Fecha': usd_mep_fecha}  # nopep8

    # Dolar CCL

    step1 = html_request.find('div', attrs={"data-indice": '/dolarrava/cl'})  # nopep8
    # usd_ccl_compra = step1.find('span', attrs={"class": "variation-max-min__value data-valor"}).text  # nopep8
    usd_ccl_venta = step1.find('span', attrs={"class": "variation-max-min__value data-valor"}).text  # nopep8
    usd_ccl_fecha = step1.find('span', attrs={"class": "variation-max-min__date-time data-fecha"}).text  # nopep8
    usd_ccl_venta = round(float(usd_ccl_venta.replace(',', '.')), 2)
    usd_ccl = {'Venta': usd_ccl_venta, 'Fecha': usd_ccl_fecha}  # nopep8

    # Dolar Crypto

    step1 = html_request.find('div', attrs={"data-indice": '/dolarcripto'})  # nopep8
    # usd_cry_compra = step1.find('span', attrs={"class": "variation-max-min__value data-valor"}).text  # nopep8
    usd_cry_venta = step1.find('span', attrs={"class": "variation-max-min__value data-valor"}).text  # nopep8
    usd_cry_fecha = step1.find('span', attrs={"class": "variation-max-min__date-time data-fecha"}).text  # nopep8
    usd_cry_venta = round(float(usd_cry_venta.replace(',', '.')), 2)
    usd_crypto = {'Venta': usd_cry_venta, 'Fecha': usd_cry_fecha}  # nopep8

    # Dolar Blue

    step1 = html_request.find('div', attrs={"data-indice": '/dolar/informal'})  # nopep8
    usd_blu_compra = step1.find('span', attrs={"class": "variation-max-min__value data-valor data-compra"}).text  # nopep8
    usd_blu_venta = step1.find('span', attrs={"class": "variation-max-min__value data-valor data-venta"}).text  # nopep8
    usd_blu_fecha = step1.find('span', attrs={"class": "variation-max-min__date-time data-fecha"}).text  # nopep8
    usd_blu_compra = round(float(usd_blu_compra.replace(',', '.')), 2)
    usd_blu_venta = round(float(usd_blu_venta.replace(',', '.')), 2)
    usd_blue = {'Compra': usd_blu_compra, 'Venta': usd_blu_venta, 'Fecha': usd_blu_fecha}  # nopep8

    # Euro Minorista

    step1 = html_request.find('div', attrs={"data-indice": '/euro/'})  # nopep8
    eur_min_compra = step1.find('span', attrs={"class": "variation-max-min__value data-valor data-compra"}).text  # nopep8
    eur_min_venta = step1.find('span', attrs={"class": "variation-max-min__value data-valor data-venta"}).text  # nopep8
    eur_min_fecha = step1.find('span', attrs={"class": "variation-max-min__date-time data-fecha"}).text  # nopep8
    eur_min_compra = round(float(eur_min_compra.replace(',', '.')), 2)
    eur_min_venta = round(float(eur_min_venta.replace(',', '.')), 2)
    eur_minorista = {'Compra': eur_min_compra, 'Venta': eur_min_venta, 'Fecha': eur_min_fecha}  # nopep8

    # Euro Blue

    step1 = html_request.find('div', attrs={"data-indice": '/euro/informal'})  # nopep8
    eur_blu_compra = step1.find('span', attrs={"class": "variation-max-min__value data-valor data-compra"}).text  # nopep8
    eur_blu_venta = step1.find('span', attrs={"class": "variation-max-min__value data-valor data-venta"}).text  # nopep8
    eur_blu_fecha = step1.find('span', attrs={"class": "variation-max-min__date-time data-fecha"}).text  # nopep8
    eur_blu_compra = round(float(eur_blu_compra.replace(',', '.')), 2)
    eur_blu_venta = round(float(eur_blu_venta.replace(',', '.')), 2)
    eur_blue = {'Compra': eur_blu_compra, 'Venta': eur_blu_venta, 'Fecha': eur_blu_fecha}  # nopep8

    # USD Solidario

    usd_solidario = {'Compra': round(usd_min_compra*FC_DOLAR_SOLIDARIO, 2), 'Venta': round(usd_min_venta*FC_DOLAR_SOLIDARIO, 2), 'Fecha': usd_min_fecha}  # nopep8

    ### COTIZACIONES###

    cotizaciones = {'usd_mayorista': usd_mayorista, 'usd_minorista': usd_minorista, 'usd_mep': usd_mep, 'usd_ccl': usd_ccl,
                    'usd_solidario': usd_solidario, 'usd_crypto': usd_crypto, 'usd_blue': usd_blue, 'eur_minorista': eur_minorista, 'eur_blue': eur_blue}

    return cotizaciones


print(ambito_data_get())
