import requests
from bs4 import BeautifulSoup as BS
import os
import json
import csv



# Получаем содержимое страницы с новостями 
url = "https://primpress.ru/news"
# При этом необходимо считать accept и useragent с headers
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
# req Возвращает метод get lib requests и headers
req = requests.get(url, headers=headers)
# далее сохраним полученный объект и вызовем у него метод text
src = req.text
# print(src)
# Далее сохраним нашу страницу в отдельный файл
with open("index.html", "w") as file:
    file.write(src)