
from bs4 import BeautifulSoup
import requests
import re

# Получаем HTML код сайта
html = requests.get('https://realty.yandex.ru/novosibirsk/snyat/kvartira/').text

# Парсим с использованием BeautifulSoup и парсера lxml
soup = BeautifulSoup(html, 'lxml')

# Получаем список ссылок и наименований
links = soup.find_all('a', class_='Link Link_js_inited Link_size_m Link_theme_islands SerpItemLink OffersSerpItem__link OffersSerpItem__titleLink')

# Создаем список для хранения всех объявлений
apartments = []

for i, link in enumerate(links):
    url = link.get("href")  # Получаем ссылку на объявление
    name = link.text.strip()  # Извлекаем наименование
    
    # Извлекаем цену
    price_elements = soup.find_all("div", class_='OffersSerpItem__price PriceWithDiscount__container--QehfS')
    if i < len(price_elements):
        price_text = price_elements[i].text.strip()
        # Преобразуем цену в числовое значение
        price = int(re.sub(r'[^\d]', '', price_text))  # Убираем все символы, кроме цифр, и преобразуем в число
    else:
        price = None

    # Фильтрация по числу комнат (однокомнатные квартиры)
    rooms_elements = soup.find_all("span", class_="Text__text--Z5x_y Text__text_m--1fDTw Text__text_medium--2JS_- OffersSerpItemTitle__title--1XhVm")
    if i < len(rooms_elements):
        rooms_text = rooms_elements[i].text.strip()
        if "1-комннатная" in rooms_text:  # Проверяем, что квартира однокомнатная
            apartments.append({
                "id": i + 1,
                "url": f"https://realty.yandex.ru{url}",
                "name": name,
                "price": price
            })

# Сортировка по цене по возрастанию
apartments_sorted = sorted(apartments, key=lambda x: x['price'])

# Выводим отсортированные объявления
for apt in apartments_sorted:
    print(f"ID: {apt['id']}")
    print(f"Url: {apt['url']}")
    print(f"Name: {apt['name']}")
    print(f"Price: {apt['price']} руб.\n")




