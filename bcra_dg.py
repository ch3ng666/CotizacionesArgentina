'########## BCRA GET DATA##########'
import re
import requests
from bs4 import BeautifulSoup
import urllib3


# pylint: disable=C0301

urllib3.disable_warnings()

URL = 'https://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables.asp'
url_request = requests.get(URL, timeout=5, verify=False)
html_request = BeautifulSoup(url_request.text, 'html.parser')


def bcra_data_get():
    'main'

    # Tasa de Politica Monetaria
    step1 = html_request.find('a', string=re.compile('.Tasa de Política Monetaria.'))  # nopep8
    tasa_politica_monetaria_value = step1.find_next('td').find_next('td').text  # nopep8
    tasa_politica_monetaria_value = round(float(tasa_politica_monetaria_value.replace(',', '.')), 2)  # nopep8
    tasa_politica_monetaria_fecha = step1.find_next('td').text  # nopep8
    tasa_politica_monetaria = {
        'Value': tasa_politica_monetaria_value, 'Fecha': tasa_politica_monetaria_fecha}

    # Plazo Fijo
    step1 = html_request.find('a', string=re.compile('.Tasas de interés por depósitos a 30 días.'))  # nopep8
    plazo_fijo_value = step1.find_next('td').find_next('td').text  # nopep8
    plazo_fijo_value = round(float(plazo_fijo_value.replace(',', '.')), 2)  # nopep8
    plazo_fijo_fecha = step1.find_next('td').text  # nopep8
    plazo_fijo = {'Value': plazo_fijo_value, 'Fecha': plazo_fijo_fecha}

    # Inflacion
    step1 = html_request.find('a', string=re.compile('Inflación mensual.'))  # nopep8
    inflacion_value = step1.find_next('td').find_next('td').text  # nopep8
    inflacion_value = round(float(inflacion_value.replace(',', '.')), 2)  # nopep8
    inflacion_fecha = step1.find_next('td').text  # nopep8
    inflacion = {'Value': inflacion_value, 'Fecha': inflacion_fecha}

    # Inflacion Interanual
    step1 = html_request.find('a', string=re.compile('Inflación interanual.'))  # nopep8
    inflacion_inter_value = step1.find_next('td').find_next('td').text  # nopep8
    inflacion_inter_value = round(float(inflacion_inter_value.replace(',', '.')), 2)  # nopep8
    inflacion_inter_fecha = step1.find_next('td').text  # nopep8
    inflacion_inter = {'Value': inflacion_inter_value,
                       'Fecha': inflacion_inter_fecha}

    # Inflación esperada
    step1 = html_request.find('a', string=re.compile('Inflación esperada.'))  # nopep8
    inflacion_esperada_value = step1.find_next('td').find_next('td').text  # nopep8
    inflacion_esperada_value = round(float(inflacion_esperada_value.replace(',', '.')), 2)  # nopep8
    inflacion_esperada_fecha = step1.find_next('td').text  # nopep8
    inflacion_esperada = {'Value': inflacion_esperada_value,
                          'Fecha': inflacion_esperada_fecha}

    ###  TASAS ###

    tasas = {
        'tasa_politica_monetaria': tasa_politica_monetaria,
        'plazo_fijo': plazo_fijo,
        'inflacion': inflacion,
        'inflacion_interanual': inflacion_inter,
        'inflacion_esperada': inflacion_esperada
    }

    return tasas
