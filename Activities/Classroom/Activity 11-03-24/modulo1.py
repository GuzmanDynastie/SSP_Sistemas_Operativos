import requests
from bs4 import BeautifulSoup
import html5lib

url = 'https://es.99designs.com/inspiration/logos/distressed'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html5lib')

imagelink = soup.find("img",class_="design-figure__image-container__image").get('src')


print(imagelink)