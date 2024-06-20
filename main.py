'''App'''
import time
import flet as ft
from bcra import (usd_mayorista_value, usd_mayorista_fecha,
                  usd_minorista_value, usd_minorista_fecha,
                  tasa_politica_monetaria_value, tasa_politica_monetaria_fecha,
                  plazo_fijo_value, plazo_fijo_fecha,
                  inflacion_value, inflacion_fecha,
                  inflacion_inter_value, inflacion_inter_fecha,
                  inflacion_esperada_value, inflacion_esperada_fecha)
from investing import inf_ano_pasado


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

    usd_mayv, usd_mayf = usd_mayorista_value(), usd_mayorista_fecha()
    usd_minv, usd_minf = usd_minorista_value(), usd_minorista_fecha()
    tp_monv, tp_monf = tasa_politica_monetaria_value(), tasa_politica_monetaria_fecha()
    pf_v, pf_f = plazo_fijo_value(), plazo_fijo_fecha()
    inf_v, inf_f = inflacion_value(), inflacion_fecha()
    inf_interv, inf_interf = inflacion_inter_value(), inflacion_inter_fecha()
    inf_espv, inf_espf = inflacion_esperada_value(), inflacion_esperada_fecha()
    usd_infv, usd_inff = inf_ano_pasado(), usd_mayorista_fecha()

    # RELOAD FUNCTION #

    counter = 10

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
        title=ft.Text('DATA', size=15, text_align='Center', weight='bold'),
        center_title=True,
        actions=[
            ft.Text(f'{c_time.tm_hour}:{c_time.tm_min}',
                    size=15, weight='bold'),
            contador := ft.Text(f' ({counter})', size=15, text_align='Center', weight='bold'),
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

    scroll_table = ft.Column(  # Tablas
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
                                TableText(usd_mayf, width=95)
                            ]
                        ),
                        Rows(  # Calificación S&P
                            [
                                TableText('Calificación S&P', expand=True),
                                ft.Text('-', color='indigo'),
                                TableText('---'),
                                ft.Text('-', color='indigo'),
                                TableText(usd_mayf, width=95)
                            ]
                        ),
                        Rows(  # Merval
                            [
                                TableText('Merval', expand=True),
                                ft.Text('-', color='indigo'),
                                TableText('---'),
                                ft.Text('-', color='indigo'),
                                TableText(usd_mayf, width=95)
                            ]
                        ),
                        Rows(  # Merval USD
                            [
                                TableText('Merval USD', expand=True),
                                ft.Text('-', color='indigo'),
                                TableText('---'),
                                ft.Text('-', color='indigo'),
                                TableText(usd_mayf, width=95)
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
                                TableText('USD Mayorista', expand=True),
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
                                TableText('USD Minorista', expand=True),
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
                                TableText(''),
                                ft.Text('-', color='indigo'),
                                TableText('%'),
                                ft.Text('-', color='indigo'),
                                TableText('', width=95)
                            ]
                        ),
                        Rows(  # USD CCL GD30
                            [
                                TableText('USD CCL GD30', expand=True),
                                ft.Text('-', color='indigo'),
                                TableText(''),
                                ft.Text('-', color='indigo'),
                                TableText('%'),
                                ft.Text('-', color='indigo'),
                                TableText('', width=95)
                            ]
                        ),
                        Rows(  # USD Solidario
                            [
                                TableText('USD Solidario', expand=True),
                                ft.Text('-', color='indigo'),
                                TableText(round(float(usd_minv)*1.6, 2)),
                                ft.Text('-', color='indigo'),
                                TableText('60 %'),
                                ft.Text('-', color='indigo'),
                                TableText(usd_minf, width=95)
                            ]
                        ),
                        Rows(  # USD Crypto
                            [
                                TableText('USD Crypto', expand=True),
                                ft.Text('-', color='indigo'),
                                TableText(''),
                                ft.Text('-', color='indigo'),
                                TableText('%'),
                                ft.Text('-', color='indigo'),
                                TableText('', width=95)
                            ]
                        ),
                        Rows(  # USD Blue
                            [
                                TableText('USD Blue', expand=True),
                                ft.Text('-', color='indigo'),
                                TableText(''),
                                ft.Text('-', color='indigo'),
                                TableText('%'),
                                ft.Text('-', color='indigo'),
                                TableText('', width=95)
                            ]
                        ),
                        Rows(  # Atraso Cambiario (USD)
                            [
                                TableText('USD Inflacion', expand=True),
                                ft.Text('-', color='indigo'),
                                TableText(round(float(usd_infv) * (float(inf_interv)/100+1)), 2),  # nopep8
                                ft.Text('-', color='indigo'),
                                TableText('%'),
                                ft.Text('-', color='indigo'),
                                TableText(usd_inff, width=95)
                            ]
                        ),
                        ft.Divider(thickness=2, color='indigo',
                                   trailing_indent=20, leading_indent=20, opacity=0.5),
                        Rows(  # EUR Mayorista
                            [
                                TableText('EUR Mayorista', expand=True),
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
                                TableText('EUR Minorista', expand=True),
                                ft.Text('-', color='indigo'),
                                TableText(''),
                                ft.Text('-', color='indigo'),
                                TableText('%'),
                                ft.Text('-', color='indigo'),
                                TableText('', width=95)
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
                                TableText(''),
                                ft.Text('-', color='indigo'),
                                TableText('%'),
                                ft.Text('-', color='indigo'),
                                TableText('', width=95)
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
                                TableText('Plazo Fijo 30D', expand=True),
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
        ], scroll=ft.ScrollMode.AUTO, expand=True, spacing=5)

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
