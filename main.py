'''App'''
import flet as ft
# from bcra import usd_mayorista_value, usd_mayorista_fecha, usd_minorista_value, usd_minorista_fecha  # type: ignore

# usd_mayv, usd_mayf = usd_mayorista_value(), usd_mayorista_fecha()
# usd_minv, usd_minf = usd_minorista_value(), usd_minorista_fecha()
# usd_minv_spread=round(float(usd_minv)/float(usd_mayv) * 100-100, 2

usd_mayv, usd_mayf = 500, '15/06/2024'
usd_minv, usd_minf = 500, '15/06/2024'
usd_minv_spread = round(float(usd_minv)/float(usd_mayv) * 100-100, 2)


class table_text(ft.Text):
    'table_text'

    def __init__(self, text, weight='normal', expand=False, width=70, text_align='center'):
        super().__init__()
        self.value = text
        self.expand = expand
        self.width = width
        self.text_align = text_align
        self.weight = weight


class rows(ft.Row):
    'rows'

    def __init__(self, controls, width, aligment=ft.MainAxisAlignment.SPACE_BETWEEN, adaptive=True):
        super().__init__()
        self.controls = controls
        self.width = width
        self.alignment = aligment
        self.adaptive = adaptive


def main(page: ft.Page):
    'main'
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
                            weight=ft.FontWeight.BOLD, color='indigo', size=20),
                    ft.IconButton(ft.icons.REFRESH, on_click=page.update())
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, adaptive=True),
            ft.Divider(color='indigo')
        ], spacing=0
    )
    scroll_table = ft.Column([
        ft.Container(  # Datos Financieros
            content=ft.Text('Datos Financieros', color='indigo',
                            size=20, weight=ft.FontWeight.BOLD),
            alignment=ft.alignment.center,
            margin=ft.margin.all(0),
            border=ft.border.all(1, 'indigo'),
            border_radius=ft.border_radius.all(10),
            bgcolor='#25253370',
            width=page.window_width-40
        ),
        ft.Container(  # Tabla Datos Financieros
            content=ft.Column(
                [
                    rows(  # Enunciado
                        [
                            table_text('  Nombre', expand=True, weight='bold'),
                            ft.Text('-', color='indigo'),
                            table_text('Valor', weight='bold'),
                            ft.Text('-', color='indigo'),
                            table_text('Actualizado', width=95, weight='bold')
                        ], width=page.window_width-50
                    ), ft.Divider(color='indigo'),
                    rows(  # Riesgo Pais
                        [
                            table_text('Riesgo Pais', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text('---'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_mayf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # Calificación S&P
                        [
                            table_text('Calificación S&P', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text('---'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_mayf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # Merval
                        [
                            table_text('Merval', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text('---'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_mayf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # Merval USD
                        [
                            table_text('Merval USD', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text('---'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_mayf, width=95)
                        ], page.window_width-50
                    ),
                ], spacing=2
            ), width=page.window_width-40, border=ft.border.all(2, 'indigo'), border_radius=ft.border_radius.all(10)
        ),
        ft.Container(  # Cotizaciones
            content=ft.Text('Cotizaciones', color='indigo',
                            size=20, weight=ft.FontWeight.BOLD),
            alignment=ft.alignment.center,
            margin=ft.margin.all(0),
            border=ft.border.all(1, 'indigo'),
            border_radius=ft.border_radius.all(10),
            bgcolor='#25253370',
            width=page.window_width-40
        ),
        ft.Container(  # Tabla Cotizaciones
            content=ft.Column(
                [
                    rows(  # Enunciado
                        [
                            table_text('  Nombre', expand=True, weight='bold'),
                            ft.Text('-', color='indigo'),
                            table_text('Valor', weight='bold'),
                            ft.Text('-', color='indigo'),
                            table_text('Spread', weight='bold'),
                            ft.Text('-', color='indigo'),
                            table_text('Actualizado', width=95, weight='bold')
                        ], width=page.window_width-50
                    ), ft.Divider(color='indigo'),
                    rows(  # USD Mayorista
                        [
                            table_text('USD Mayorista', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text(usd_mayv),
                            ft.Text('-', color='indigo'),
                            table_text('---'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_mayf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # USD Minorista
                        [
                            table_text('USD Minorista', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minv),
                            ft.Text('-', color='indigo'),
                            table_text(f'{usd_minv_spread} %'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # USD MEP
                        [
                            table_text('USD MEP', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minv),
                            ft.Text('-', color='indigo'),
                            table_text(f'{usd_minv_spread} %'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # USD CCL GD30
                        [
                            table_text('USD CCL GD30', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minv),
                            ft.Text('-', color='indigo'),
                            table_text(f'{usd_minv_spread} %'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # USD Solidario
                        [
                            table_text('USD Solidario', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minv),
                            ft.Text('-', color='indigo'),
                            table_text(f'{usd_minv_spread} %'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # USD Crypto
                        [
                            table_text('USD Crypto', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minv),
                            ft.Text('-', color='indigo'),
                            table_text(f'{usd_minv_spread} %'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # USD Blue
                        [
                            table_text('USD Blue', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minv),
                            ft.Text('-', color='indigo'),
                            table_text(f'{usd_minv_spread} %'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # Atraso Cambiario (USD)
                        [
                            table_text('USD Inflacion', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minv),
                            ft.Text('-', color='indigo'),
                            table_text(f'{usd_minv_spread} %'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minf, width=95)
                        ], page.window_width-50
                    ),
                    ft.Divider(thickness=2, color='indigo',
                               trailing_indent=20, leading_indent=20, opacity=0.5),
                    rows(  # EUR Mayorista
                        [
                            table_text('EUR Mayorista', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minv),
                            ft.Text('-', color='indigo'),
                            table_text(f'{usd_minv_spread} %'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # EUR Minorista
                        [
                            table_text('EUR Minorista', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minv),
                            ft.Text('-', color='indigo'),
                            table_text(f'{usd_minv_spread} %'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # EUR Crypto
                        [
                            table_text('EUR Crypto', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minv),
                            ft.Text('-', color='indigo'),
                            table_text(f'{usd_minv_spread} %'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # EUR Blue
                        [
                            table_text('EUR Blue', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minv),
                            ft.Text('-', color='indigo'),
                            table_text(f'{usd_minv_spread} %'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_minf, width=95)
                        ], page.window_width-50
                    ),
                ], spacing=2
            ), width=page.window_width-40, border=ft.border.all(2, 'indigo'), border_radius=ft.border_radius.all(10)
        ),
        ft.Container(  # Tasas
            content=ft.Text('Tasas', color='indigo',
                            size=20, weight=ft.FontWeight.BOLD),
            alignment=ft.alignment.center,
            margin=ft.margin.all(0),
            border=ft.border.all(1, 'indigo'),
            border_radius=ft.border_radius.all(10),
            bgcolor='#25253370',
            width=page.window_width-40
        ),
        ft.Container(  # Tabla Tasas
            content=ft.Column(
                [
                    rows(  # Enunciado
                        [
                            table_text('  Nombre', expand=True, weight='bold'),
                            ft.Text('-', color='indigo'),
                            table_text('Valor', weight='bold'),
                            ft.Text('-', color='indigo'),
                            table_text('Actualizado', width=95, weight='bold')
                        ], width=page.window_width-50
                    ), ft.Divider(color='indigo'),
                    rows(  # Tasa Interés
                        [
                            table_text('Tasa Interés', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text('---'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_mayf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # Plazo Fijo 30D
                        [
                            table_text('Plazo Fijo 30D', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text('---'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_mayf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # Inflación
                        [
                            table_text('Inflacion', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text('---'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_mayf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # Inflacion Interanual
                        [
                            table_text('Inflacion Interanual', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text('---'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_mayf, width=95)
                        ], page.window_width-50
                    ),
                    rows(  # Inflacion Anualizada
                        [
                            table_text('Inflacion Anualizada', expand=True),
                            ft.Text('-', color='indigo'),
                            table_text('---'),
                            ft.Text('-', color='indigo'),
                            table_text(usd_mayf, width=95)
                        ], page.window_width-50
                    ),
                ], spacing=2
            ), width=page.window_width-40, border=ft.border.all(2, 'indigo'), border_radius=ft.border_radius.all(10)
        )
    ], scroll=ft.ScrollMode.AUTO, expand=True,)

    page.add(title_separator)
    page.add(scroll_table)


ft.app(main)
