# from LxmlSoup import LxmlSoup
# import requests

# html = requests.get('https://novosibirsk.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4897&room1=1&room2=1&room9=1&type=4').text  # получаем html код сайта
# soup = LxmlSoup(html)  # создаём экземпляр класса LxmlSoup

# links = soup.find_all('a', class_='_93444fe79c--link--VtWj6')  # получаем список ссылок и наименований
# for i, link in enumerate(links):
#     url = link.get("href")  # получаем ссылку товара
#     name = link.text()  # извлекаем наименование из блока со ссылкой
#     price = soup.find_all("span", class_="_93444fe79c--color_black_100--Ephi7 _93444fe79c--lineHeight_28px--KFXmc _93444fe79c--fontWeight_bold--BbhnX _93444fe79c--fontSize_22px--sFuaL _93444fe79c--display_block--KYb25 _93444fe79c--text--e4SBY _93444fe79c--text_letterSpacing__normal--tfToq")[i].text()  # извлекаем цену
#     print(i)
#     print(f"Url - {url}")
#     print(f"Name - {name}")
#     print(f"Price - {price}\n")

# from LxmlSoup import LxmlSoup
# import requests

# html = requests.get('https://realty.ya.ru/novosibirsk/snyat/kvartira/').text  # получаем html код сайта
# soup = LxmlSoup(html)  # создаём экземпляр класса LxmlSoup

# links = soup.find_all('a', class_='Link Link_js_inited Link_size_m Link_theme_islands SerpItemLink OffersSerpItem__link OffersSerpItem__titleLink')  # получаем список ссылок и наименований
# for i, link in enumerate(links):
#     url = link.get("href")  # получаем ссылку товара
#     name = link.text()  # извлекаем наименование из блока со ссылкой
#     # price = soup.find_all("div", class_='OffersSerpItem__price PriceWithDiscount__container--QehfS')[i].text()  # извлекаем цену
#     print(i)
#     print(f"Url - {url}")
#     print(f"Name - {name}")
#     # print(f"Price - {price}\n")
    



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




