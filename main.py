'''App'''
import flet as ft
from usd_mayorista import usd_mayorista_value


def main(page: ft.Page):
    'main'
    page.bgcolor = '#000000'
    page.window_height = 768
    page.window_width = 432

    def reload_button(e):  # pylint: disable=unused-argument
        usd_mayorista.update()
        page.update()

    page.appbar = ft.AppBar(
        title=ft.Text(value='ECONOMY DATA', text_align='center',
                      italic=True, weight='bold', size=20, color='indigo999'),
        center_title=True,
        bgcolor=ft.colors.BLACK,
        actions=[ft.Container(
            content=ft.IconButton(ft.icons.REFRESH_ROUNDED,
                                  on_click=reload_button)
        )

        ]
    )

    usd_mayorista = ft.Row(
        [
            ft.Text(value='USD Mayorista:', weight='bold', text_align='right'),
            ft.Text(value=usd_mayorista_value)
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=100
    )

    page.add(usd_mayorista)


ft.app(main)
