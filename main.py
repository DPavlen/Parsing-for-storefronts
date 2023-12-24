import requests
from bs4 import BeautifulSoup as BS
import os
import json
import csv
# from fake_useragent import Useragent



# # Получаем содержимое страницы с новостями 
# url = "https://primpress.ru/news"
# # При этом необходимо считать accept и useragent с headers
# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }
# # req Возвращает метод get lib requests и headers
# req = requests.get(url, headers=headers)
# # далее сохраним полученный объект и вызовем у него метод text
# src = req.text
# # print(src)
# # Далее сохраним нашу страницу в отдельный файл
# with open("index.html", "w") as file:
#     file.write(src)

# Откроем, пррочитаем наш файл и сохраним в переменную src
with open("index.html") as file:
    src = file.read()

soup = BS(src, "lxml")
# # В качестве параметра поиска передадим класс ссылок(id)
# all_articles_hrefs = soup.find_all('div', id='sticky-content')

# Создаем пустой словарь для хранения заголовка и фото к сатье
titles_images_dict = {}
# Находим все элементы с классом "b-news-feed-home"
news_elements = soup.find_all('div', class_="b-news-feed-home")

# Проходимся по каждому элементу и извлекаем нужную информацию
for element in news_elements:
    # Находим заголовок статьи
    title = element.find(class_="b-news-feed-home__title").text.strip()
    
    # # Находим ссылку на статью
    # link_element = element.find("a", href=True)
    # link = link_element["href"] if link_element else ""

    # Находим ссылку на картинку
    image_element = element.find("img", src=True)
    image = image_element["data-src"] if image_element else ""

    # Добавляем статью в словарь
    # articles_dict[title] = {"link": link, "image": image}
    titles_images_dict[title] = {"image": image}

# Сохраняем словарь со статьями в формате JSON
with open("json_data/title_image.json", "w", encoding="utf-8") as file:
    json.dump(titles_images_dict, file, indent=4,  ensure_ascii=False)

# Выводим сообщение об успешном завершении
print("Заголовки и Картинки к статьям успешно спарсены и сохранены в файл articles.json")


#Создадим переменную {} и далее будем его наполнять заголовком и ссылкой к ней
# title_link_dict = []
title_link_dict = {}

# Находим ссылку и заголовок статьи
# <div id="sticky-content">
links = soup.find_all("a", href=True, title=True)
# href = links["href"]
# title = links["title"]

# Заполняем список словарей
for link in links:
    href = link["href"]
    title = link["title"]
    title_link_dict[title] = href


# Открываем файл на запись JSON
with open("json_data/title_link.json", "w", encoding='utf-8') as file:
    json.dump(title_link_dict, file, indent=4, ensure_ascii=False)



# if __name__ == "__main__":
#     result = main()