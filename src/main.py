import flet as ft
from components.AppBar import AppBar_
from components.TextField import TextField_
from components.Select import Select_
from helpers import margin_calculator


def main(page: ft.Page):
    page.title = "Calculadora de Margenes"

    #variables
    global price
    global currency
    global margin
    margin = 0.15
    price = 0
    currency = "usd"
    total = ft.Text(
            value="$0.00 MXN",
            weight=ft.FontWeight.BOLD,
            size=50, text_align=ft.TextAlign.CENTER, selectable=True
        )
    
    #onchange
    def price_change(e):
        global price
        price = e.control.value

    def currency_change(e):
        global currency
        currency = e.control.value

    def margin_change(e):
        global margin
        margin = e.control.value
        if margin == "15 %": margin = 0.15
        if margin == "20 %": margin = 0.20
        if margin == "25 %": margin = 0.25
        if margin == "30 %": margin = 0.30

    def cal_total(e):
        global margin, price, currency
        total.value = margin_calculator(margin, price, currency)
        page.update()
    #fields
    price_field = TextField_("Precio", 400, onchange=price_change).create()

    #select
    m = Select_(margin_change, 400).create()

    #radio
    o = ft.RadioGroup(on_change=currency_change,value=currency,content=ft.Row([
    ft.Radio(value="usd", label="USD",),
    ft.Radio(value="mxn", label="MXN")]))

    #containers
    c = ft.Container(
        width=600,
        height=120,
        border=ft.border.all(2, "#0079a7"),
        border_radius=5,
        padding=20,
        margin=ft.margin.only(top=50),
        content=total
        
    )


    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.appbar = AppBar_().create()
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD
    )
    page.add(
        ft.Column(
            [
                ft.Text(value="Ingrese los datos", size=30, weight=ft.FontWeight.BOLD),
                ft.Row(
                    [
                        price_field,o
                    ]
                ),
                ft.Row(
                    [
                        m
                    ]
                ),
                ft.Row(
                    [
                        ft.ElevatedButton("Calcular precio", on_click=lambda _: cal_total(_), width=300, height=70, bgcolor="#0079a7", 
                                          color=ft.colors.WHITE, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)))
                    ], expand=True, alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Divider(),
                ft.Row(
                    [
                        ft.Text("Precio al cliente", size=30),
                    ], expand=True, alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        c
                    ], expand=True, alignment=ft.MainAxisAlignment.CENTER
                ),
            ]
        )
    )


ft.app(main)
