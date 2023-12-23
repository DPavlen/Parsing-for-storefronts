import requests
from bs4 import BeautifulSoup as BS
import os
import json
import csv



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
# В качестве параметра поиска передадим класс ссылок(id)
all_articles_hrefs = soup.find_all('div', id='sticky-content', limit=10)
# all_articles_hrefs = soup.find_all("a", class_="b-news-feed-home g-link-block d-flex flex-row mb-1 py-1")

#Создадим переменную {} и далее будем его наполнять
all_articles_dict = {}

for item in all_articles_hrefs:
    # item_text = item.find("div", class_="b-news-feed-home__title g-color--darkgrey font-weight-bold py-1").text.strip()
    item_text = item.find("a")["title"]
    item_href = item.find("a")["href"]
    print(f"{item_text}: {item_href}")
    all_articles_dict[item_text] = item_href

# Открываем файл на запись JSON
with open("all_articles_dict.json", "w", encoding='utf-8') as file:
    json.dump(all_articles_dict, file, indent=4, ensure_ascii=False)
