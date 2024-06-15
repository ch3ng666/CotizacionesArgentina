'''App'''
import flet as ft
from bcra import usd_mayorista_value, usd_mayorista_fecha, usd_minorista_value, usd_minorista_fecha  # type: ignore


def main(page: ft.Page):
    'main'
    ######### Variables #############
    usd_mayv = usd_mayorista_value()
    usd_mayf = usd_mayorista_fecha()
    usd_minv = usd_minorista_value()
    usd_minf = usd_minorista_fecha()
    #################################
    page.adaptive = True
    page.bgcolor = '#000000'
    page.window_width = 432
    page.window_height = 768
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    title_separator = ft.Column(
        [
            ft.Row(
                [
                    ft.IconButton(ft.icons.MENU),
                    ft.Text('DATA', text_align='center',
                            expand=True, weight=ft.FontWeight.BOLD, color='indigo', size=20),
                    ft.IconButton(ft.icons.REFRESH, on_click=page.update())
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(color='indigo')
        ], spacing=0
    )

    table = ft.Column(
        [
            ft.Row(  # Enunciado
                [
                    ft.Text('Nombre', expand=True, text_align='center'),
                    ft.Text('Valor', text_align='center', width=65),
                    ft.Text('Spread', text_align='center', width=65),
                    ft.Text('Actualizado', text_align='center', width=75)
                ], alignment=ft.MainAxisAlignment.CENTER, adaptive=True
            ),
            ft.Row(  # USD Mayorista
                [
                    ft.Text('USD Mayorista', expand=True, text_align='center'),
                    ft.Text(usd_mayv, text_align='center', width=65),
                    ft.Text('---', text_align='center', width=65),
                    ft.Text(usd_mayf, text_align='center', width=75)
                ], alignment=ft.MainAxisAlignment.CENTER, adaptive=True
            ),
            ft.Row(  # USD Minorista
                [
                    ft.Text('USD Minorista', expand=True, text_align='center'),
                    ft.Text(usd_minv, text_align='center', width=65),
                    ft.Text(f'{round(float(usd_minv)/float(usd_mayv)
                            * 100-100, 2)} %', text_align='center', width=65),
                    ft.Text(usd_minf, text_align='center', width=75)
                ], alignment=ft.MainAxisAlignment.CENTER, adaptive=True
            )
        ]
    )

    # page.on_resize = lambda e: table.width = e.control.width

    page.add(title_separator)
    page.add(table)


ft.app(main)
