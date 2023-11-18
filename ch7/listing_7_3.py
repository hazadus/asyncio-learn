"""
Базовое использование `requests`
"""
import requests


def get_status_code(_url: str) -> int:
    response = requests.get(_url)
    return response.status_code


url = "https://hazadus.ru"
print(get_status_code(url))
print(get_status_code(url))
