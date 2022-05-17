# requests travel.py
import requests
from bs4 import BeautifulSoup

res = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
pic = res.text

soup = BeautifulSoup(pic,'html.parser')
items = soup.find_all(class_ = 'product_pod')

for i in items:
    kind = i.find('h3')
    print(kind.text)
    
    star = i.find('p')
    print(star['class'])

    prices = i.find(class_ = 'product_price')
    price = prices.find(class_ = 'price_color')
    print(price.text)