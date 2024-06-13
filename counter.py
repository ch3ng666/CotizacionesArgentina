# pylint: disable=missing-module-docstring
import flet as ft


def main(page: ft.Page):  # pylint: disable=missing-function-docstring
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(
        value="0", text_align=ft.TextAlign.RIGHT, width=100, read_only=True)

    def minus_click(e):  # pylint: disable=unused-argument
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):  # pylint: disable=unused-argument
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(main)
