import time
import os
import requests
from urllib.parse import urlparse

# Цвета
RED = "\033[31m"
RESET = "\033[0m"

# Функция для анимации текста
def animate_text(text, delay=0.2):
    for line in text.split('\n'):
        print(line)
        time.sleep(delay)

# Меню
def main_menu():
    os.system('clear')
    animate_text(f"{RED}1) WIFI FUNCS\n2) Info{RESET}")
    choice = input("\nВыберите опцию: ")

    if choice == '1':
        wifi_menu()
    elif choice == '2':
        info()
    else:
        print("Неверный выбор!")
        main_menu()

# Меню для WiFi функций
def wifi_menu():
    os.system('clear')
    animate_text(f"{RED}1) URL Requests\n2) URL Html\n3) URL Check{RESET}")
    choice = input("\nВыберите опцию: ")

    if choice == '1':
        url_requests()
    elif choice == '2':
        url_html()
    elif choice == '3':
        url_check()
    else:
        print("Неверный выбор!")
        wifi_menu()

# Функция для отправки спам-запросов на URL
def url_requests():
    url = input("Введите URL для спама: ")
    data = {"message": "spam"}
    while True:
        try:
            response = requests.post(url, data=data)
            print(f"Запрос отправлен! Статус: {response.status_code}")
            time.sleep(0.5)
        except Exception as e:
            print(f"Ошибка: {e}")
            break

# Функция для копирования кода сайта и сохранения его на устройство
def url_html():
    url = input("Введите URL для копирования HTML: ")
    try:
        response = requests.get(url)
        html_code = response.text
        file_name = f"{urlparse(url).netloc}.html"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(html_code)
        print(f"Код сайта скопирован и сохранен в файл: {file_name}")
    except Exception as e:
        print(f"Ошибка: {e}")

# Функция для проверки URL (домен, активность сайта, защита)
def url_check():
    url = input("Введите URL для проверки: ")
    try:
        response = requests.get(url)
        domain = urlparse(url).netloc
        https_status = "Активен" if response.url.startswith("https") else "Не активен"
        print(f"Домен: {domain}\nHTTPS защита: {https_status}\nСтатус сайта: {response.status_code}")
    except Exception as e:
        print(f"Ошибка: {e}")

# Информация
def info():
    print("Скрипт для работы с WiFi функциями и запросами URL.")
    input("\nНажмите Enter, чтобы вернуться в главное меню...")
    main_menu()

if __name__ == "__main__":
    main_menu()