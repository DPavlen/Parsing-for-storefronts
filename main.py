import requests
from bs4 import BeautifulSoup as BS


# Получаем содержимое страницы с новостями
res = requests.get("https://primpress.ru/news")
# Результат скармливаем в BS
html = BS(res.content, 'html.parser')
# Далее указываем селекторы(они такие же как в css)
for element in html.select(".items > .article-summary"):
    title = element.select('.caption > a')
    print(title[0].text)