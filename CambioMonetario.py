import flet as ft
import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']["bid"]

result_text = ft.TextField(value="1", width=200, text_align=ft.TextAlign.CENTER)

def main(page: ft.Page):
    def convert_dollar_to_real(e):
        try:
            dollar_amount = float(dollar_input.value)
            exchange_rate = float(cotacao_dolar)
            real_amount = dollar_amount * exchange_rate
            result_text.value = (real_amount)
            print (result_text.value)
            
        except ValueError:
            result_text.value = "Por favor, insira valores válidos."

    dollar_input = ft.TextField("Quantidade de dólares:", keyboard_type=ft.KeyboardType.NUMBER)
    convert_button = ft.TextButton("Converter", on_click=convert_dollar_to_real)
    result_text = ft.Text()

    page.add(
             ft.Row([dollar_input, result_text, convert_button], alignment=ft.MainAxisAlignment.CENTER)
             )
ft.app(target=main)