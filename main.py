# sudo apt install libmpv1
import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Мое первое приложение на Flet"    
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Привет, мир!")

    greeting_history = []

    history_text = ft.Text("История приветствий:")

    def on_button_click(e):
        name = name_input.value.strip()

        if name:
            greeting_text.value = f"Привет, {name}!"
            name_input.value = ""
            greet_button.text = 'Поздороваться еще раз'

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f"{timestamp} - {name}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Пожалуйста, введите имя."
        
        page.update()
    
    name_input = ft.TextField(label="Введите ваше имя", autofocus=True, on_submit=on_button_click)

    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, tooltip='Сменить тему')

    greet_button = ft.ElevatedButton("Поздороваться", on_click=on_button_click)

    page.add(greeting_text, name_input, greet_button, theme_button, history_text)

ft.app(main)