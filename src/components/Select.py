import flet as ft

class Select_():
    def __init__(self, onChange, w):
        self.onChange = onChange
        self.w = w
        


    def create(self):
        return ft.Dropdown(
            options=[
                ft.dropdown.Option("15 %"),
                ft.dropdown.Option("20 %"),
                ft.dropdown.Option("25 %"),
                ft.dropdown.Option("30 %"),
            ],
            on_change=self.onChange,
            hint_content="-- Selecciona el margen --",
            value="15 %",
            label="Margen",
            width=self.w,

        )