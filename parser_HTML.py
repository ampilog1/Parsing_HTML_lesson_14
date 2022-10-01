import requests
from bs4 import BeautifulSoup
import pprint

url = 'http://dedmorozural.ru/novosti'

response = requests.get(url)
# print(response.status_code)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.title.string)
# print(soup.a.string)
# print(soup.p.string)
# print(soup.a.get('href'))
news_a = soup.find_all('a')

news_a_class = soup.find_all('a', class_='con_titlelink')
for one_news in news_a_class:
    print(one_news.get('href'))