import flet as ft


class AppBar_():
    def __init__(self):
        pass
    def create(self):
        return ft.AppBar(
            elevation=1,
            leading_width=50,
            toolbar_height=60,
            bgcolor= "#0079a7",
            title=ft.Text(
                spans=[
                    ft.TextSpan(
                        "Calculador de margenes",
                        style=ft.TextStyle(
                            color=ft.Colors.WHITE,
                            weight=ft.FontWeight.BOLD
                        )
                    ),
                ],
            ),
            actions=[
            ]
        )