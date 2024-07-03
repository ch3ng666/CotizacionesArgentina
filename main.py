'''CotizacionesArgentina'''
import time
import flet as ft
from ambito_dg import ambito_data_get


class TableText(ft.Text):   # Texto Tablas
    'table_text'

    def __init__(self, text, weight='normal', expand=False, width=70, text_align='center'):
        super().__init__()
        self.value = text
        self.expand = expand
        self.width = width
        self.text_align = text_align
        self.weight = weight


class Rows(ft.Row):  # Filas Tablas
    'rows'

    def __init__(self, controls, aligment=ft.MainAxisAlignment.SPACE_BETWEEN, adaptive=True):
        super().__init__()
        self.controls = controls
        self.alignment = aligment
        self.adaptive = adaptive


def main(page: ft.Page):
    'main'

    # VALORES #

    cotizaciones = ambito_data_get()
    usd_mayv, usd_mayf = cotizaciones['usd_mayorista']['Venta'], cotizaciones['usd_mayorista']['Fecha']
    usd_minv, usd_minf = cotizaciones['usd_minorista']['Venta'], cotizaciones['usd_minorista']['Fecha']
    usd_mepv, usd_mepf = cotizaciones['usd_mep']['Venta'], cotizaciones['usd_mep']['Fecha']
    usd_cclv, usd_cclf = cotizaciones['usd_ccl']['Venta'], cotizaciones['usd_ccl']['Fecha']
    usd_crypv, usd_crypf = cotizaciones['usd_crypto']['Venta'], cotizaciones['usd_crypto']['Fecha']
    usd_bluev, usd_bluef = cotizaciones['usd_blue']['Venta'], cotizaciones['usd_blue']['Fecha']
    usd_infv, usd_inff = cotizaciones['usd_inflacion']['Venta'], cotizaciones['usd_inflacion']['Fecha']
    usd_solv, usd_solf = cotizaciones['usd_solidario']['Venta'], cotizaciones['usd_solidario']['Fecha']
    eur_minv, eur_minf = cotizaciones['eur_minorista']['Venta'], cotizaciones['eur_minorista']['Fecha']
    eur_bluev, eur_bluef = cotizaciones['eur_blue']['Venta'], cotizaciones['eur_blue']['Fecha']
    tp_monv, tp_monf = 5, 5
    pf_v, pf_f = 5, 5
    inf_v, inf_f = 5, 5
    inf_interv, inf_interf = 5, 5
    inf_espv, inf_espf = 5, 5

    # RELOAD FUNCTION #

    counter = 60

    def reload_page(e):  # pylint: disable=unused-argument
        'reload_page'
        page.clean()
        main(page)

    ######################################################################

    # WINDOWS PARAMETERS #

    page.window_width = 432
    page.window_height = 768
    page.window_resizable = False

    ######################################################################

    # MAIN CODE #

    c_time = time.localtime()

    page.adaptive = True
    page.bgcolor = '#000000'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 10

    app_bar = ft.AppBar(  # AppBar
        title=ft.Text('CotizacionesArgentina', size=15,
                      text_align='Center', weight='bold'),
        center_title=False,
        actions=[
            ft.Text(f'Actualizado: {c_time.tm_hour}:{c_time.tm_min}',
                    size=10, weight='bold'),
            contador := ft.Text(f' ({counter})', size=10, text_align='Center', weight='bold'),
            boton := ft.IconButton(
                ft.icons.REFRESH,
                visual_density=ft.ThemeVisualDensity.COMPACT,
                on_click=reload_page)
        ],
        bgcolor='#50253370',
        toolbar_height=25,
        color='indigo',
        elevation=0
    )

    boton.disabled = True

    stack_tables = ft.Stack(  # pylint: disable=unused-variable
        [
        scroll_table := ft.Column(  # Tablas
            [
                ft.Container(  # Datos Financieros
                    content=ft.Text('Datos Financieros', color='indigo',
                                    size=15, weight=ft.FontWeight.BOLD),
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(0),
                    border=ft.border.all(1, 'indigo'),
                    border_radius=ft.border_radius.all(10),
                    bgcolor='#25253370',
                ),
                ft.Container(  # Tabla Datos Financieros
                    content=ft.Column(
                        [
                            Rows(  # Enunciado
                                [
                                    TableText('  Nombre', expand=True,
                                            weight='bold'),
                                    ft.Text('-', color='indigo'),
                                    TableText('Valor', weight='bold'),
                                    ft.Text('-', color='indigo'),
                                    TableText('Actualizado', width=95, weight='bold')  # nopep8
                                ]
                            ), ft.Divider(color='indigo'),
                            Rows(  # Riesgo Pais
                                [
                                    TableText('Riesgo Pais', expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText('---'),
                                    ft.Text('-', color='indigo'),
                                    TableText('', width=95)
                                ]
                            ),
                            Rows(  # Calificación S&P
                                [
                                    TableText('Calificación S&P',
                                                expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText('---'),
                                    ft.Text('-', color='indigo'),
                                    TableText('', width=95)
                                ]
                            ),
                            Rows(  # Merval
                                [
                                    TableText('Merval', expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText('---'),
                                    ft.Text('-', color='indigo'),
                                    TableText('', width=95)
                                ]
                            ),
                            Rows(  # Merval USD
                                [
                                    TableText('Merval USD', expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText('---'),
                                    ft.Text('-', color='indigo'),
                                    TableText('', width=95)
                                ]
                            ),
                        ], spacing=1
                    ), border=ft.border.all(2, 'indigo'), border_radius=ft.border_radius.all(10)
                ),
                ft.Container(  # Cotizaciones
                    content=ft.Text('Cotizaciones', color='indigo',
                                    size=15, weight=ft.FontWeight.BOLD),
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(0),
                    border=ft.border.all(1, 'indigo'),
                    border_radius=ft.border_radius.all(10),
                    bgcolor='#25253370',
                ),
                ft.Container(  # Tabla Cotizaciones
                    content=ft.Column(
                        [
                            Rows(  # Enunciado
                                [
                                    TableText('  Nombre', expand=True,
                                            weight='bold'),
                                    ft.Text('-', color='indigo'),
                                    TableText('Valor', weight='bold'),
                                    ft.Text('-', color='indigo'),
                                    TableText('Spread', weight='bold'),
                                    ft.Text('-', color='indigo'),
                                    TableText('Actualizado',
                                            width=95, weight='bold')
                                ]
                            ), ft.Divider(color='indigo'),
                            Rows(  # USD Mayorista
                                [
                                    TableText('USD Mayorista',
                                                expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(usd_mayv),
                                    ft.Text('-', color='indigo'),
                                    TableText('---'),
                                    ft.Text('-', color='indigo'),
                                    TableText(usd_mayf, width=95)
                                ]
                            ),
                            Rows(  # USD Minorista
                                [
                                    TableText('USD Minorista',
                                                expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(usd_minv),
                                    ft.Text('-', color='indigo'),
                                    TableText(
                                        f'{round(float(usd_minv)/float(usd_mayv), 2)*100-100} %'),
                                    ft.Text('-', color='indigo'),
                                    TableText(usd_minf, width=95)
                                ]
                            ),
                            Rows(  # USD MEP
                                [
                                    TableText('USD MEP', expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(usd_mepv),
                                    ft.Text('-', color='indigo'),
                                    TableText(
                                        f'{round(float(usd_mepv)/float(usd_mayv), 2)*100-100} %'),
                                    ft.Text('-', color='indigo'),
                                    TableText(usd_mepf, width=95)
                                ]
                            ),
                            Rows(  # USD CCL GD30
                                [
                                    TableText('USD CCL GD30', expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(usd_cclv),
                                    ft.Text('-', color='indigo'),
                                    TableText(
                                        f'{round(float(usd_cclv)/float(usd_mayv), 2)*100-100} %'),
                                    ft.Text('-', color='indigo'),
                                    TableText(usd_cclf, width=95)
                                ]
                            ),
                            Rows(  # USD Solidario
                                [
                                    TableText('USD Solidario',
                                                expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(usd_solv),
                                    ft.Text('-', color='indigo'),
                                    TableText('60 %'),
                                    ft.Text('-', color='indigo'),
                                    TableText(usd_solf, width=95)
                                ]
                            ),
                            Rows(  # USD Crypto
                                [
                                    TableText('USD Crypto', expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(usd_crypv),
                                    ft.Text('-', color='indigo'),
                                    TableText(
                                        f'{round(float(usd_crypv)/float(usd_mayv), 2)*100-100} %'),
                                    ft.Text('-', color='indigo'),
                                    TableText(usd_crypf, width=95)
                                ]
                            ),
                            Rows(  # USD Blue
                                [
                                    TableText('USD Blue', expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(usd_bluev),
                                    ft.Text('-', color='indigo'),
                                    TableText(
                                        f'{round(float(usd_bluev)/float(usd_mayv), 2)*100-100} %'),
                                    ft.Text('-', color='indigo'),
                                    TableText(usd_bluef, width=95)
                                ]
                            ),
                            Rows(  # USD Inflacion
                                [
                                    TableText('USD Inflacion',
                                                expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(usd_infv),  # nopep8
                                    ft.Text('-', color='indigo'),
                                    TableText(
                                        f'{round(float(usd_infv)/float(usd_mayv), 2)*100-100} %'),
                                    ft.Text('-', color='indigo'),
                                    TableText(usd_inff, width=95)
                                ]
                            ),
                            ft.Divider(thickness=2, color='indigo',
                                    trailing_indent=20, leading_indent=20, opacity=0.5),
                            Rows(  # EUR Mayorista
                                [
                                    TableText('EUR Mayorista',
                                                expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(''),
                                    ft.Text('-', color='indigo'),
                                    TableText('%'),
                                    ft.Text('-', color='indigo'),
                                    TableText('', width=95)
                                ]
                            ),
                            Rows(  # EUR Minorista
                                [
                                    TableText('EUR Minorista',
                                                expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(eur_minv),
                                    ft.Text('-', color='indigo'),
                                    TableText('%'),
                                    ft.Text('-', color='indigo'),
                                    TableText(eur_minf, width=95)
                                ]
                            ),
                            Rows(  # EUR Crypto
                                [
                                    TableText('EUR Crypto', expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(''),
                                    ft.Text('-', color='indigo'),
                                    TableText('%'),
                                    ft.Text('-', color='indigo'),
                                    TableText('', width=95)
                                ]
                            ),
                            Rows(  # EUR Blue
                                [
                                    TableText('EUR Blue', expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(eur_bluev),
                                    ft.Text('-', color='indigo'),
                                    TableText('%'),
                                    ft.Text('-', color='indigo'),
                                    TableText(eur_bluef, width=95)
                                ]
                            ),
                        ], spacing=1
                    ), border=ft.border.all(2, 'indigo'), border_radius=ft.border_radius.all(10)
                ),
                ft.Container(  # Tasas
                    content=ft.Text('Tasas', color='indigo',
                                    size=15, weight=ft.FontWeight.BOLD),
                    alignment=ft.alignment.center,
                    margin=ft.margin.all(0),
                    border=ft.border.all(1, 'indigo'),
                    border_radius=ft.border_radius.all(10),
                    bgcolor='#25253370',
                ),
                ft.Container(  # Tabla Tasas
                    content=ft.Column(
                        [
                            Rows(  # Enunciado
                                [
                                    TableText('  Nombre', expand=True,
                                            weight='bold'),
                                    ft.Text('-', color='indigo'),
                                    TableText('Valor', weight='bold'),
                                    ft.Text('-', color='indigo'),
                                    TableText('Actualizado',
                                            width=95, weight='bold')
                                ]
                            ), ft.Divider(color='indigo'),
                            Rows(  # Tasa Interés
                                [
                                    TableText('Tasa Interés', expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(f'{tp_monv}%'),
                                    ft.Text('-', color='indigo'),
                                    TableText(tp_monf, width=95)
                                ]
                            ),
                            Rows(  # Plazo Fijo 30D
                                [
                                    TableText('Plazo Fijo 30D',
                                                expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(f'{pf_v}%'),
                                    ft.Text('-', color='indigo'),
                                    TableText(pf_f, width=95)
                                ]
                            ),
                            Rows(  # Inflación
                                [
                                    TableText('Inflacion', expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(f'{inf_v}%'),
                                    ft.Text('-', color='indigo'),
                                    TableText(inf_f, width=95)
                                ]
                            ),
                            Rows(  # Inflacion Interanual
                                [
                                    TableText(
                                        'Inflacion Interanual', expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(f'{inf_interv}%'),
                                    ft.Text('-', color='indigo'),
                                    TableText(inf_interf, width=95)
                                ]
                            ),
                            Rows(  # Inflacion Esperada
                                [
                                    TableText(
                                        'Inflacion Esperada (12M)', expand=True),
                                    ft.Text('-', color='indigo'),
                                    TableText(f'{inf_espv}%'),
                                    ft.Text('-', color='indigo'),
                                    TableText(inf_espf, width=95)
                                ]
                            ),
                        ], spacing=1
                    ), border=ft.border.all(2, 'indigo'), border_radius=ft.border_radius.all(10)
                )
            ], scroll=ft.ScrollMode.ALWAYS, spacing=5)
        ################ agregar dialogo#####################
        ]
    )

    page.add(app_bar)
    page.add(scroll_table)

    ######################################################################

    # CONTADOR #

    contador.visible = True

    while True:
        time.sleep(1)
        counter -= 1
        contador.value = f' ({counter})'
        page.update()
        if counter == 0:
            break

    boton.disabled = False
    contador.visible = False

    ######################################################################

    page.update()


ft.app(main)
