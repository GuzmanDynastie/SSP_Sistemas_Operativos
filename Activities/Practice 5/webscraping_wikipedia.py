import requests
import os
from bs4 import BeautifulSoup

website = 'https://es.wikipedia.org'
response = requests.get(website)
path = 'Activities/Practice 5'

os.makedirs(path, exist_ok=True)

content = response.content
soup = BeautifulSoup(content, 'lxml')

title_featured_articled = soup.find('h2', class_='main-header main-box-header').get_text(strip=True, separator=' ')
text_featured_articled = soup.find('div', class_='main-box main-box-responsive-image').get_text(strip=True, separator=' ')
full_path_1 = os.path.join(path, title_featured_articled + '.txt')

title_featured_good = soup.find('div', id='main-tga').find('h2').get_text(strip=True, separator=' ')
text_featured_good = soup.find('div', id='main-tga').find('p').get_text(strip=True, separator=' ')
full_path_2 = os.path.join(path, title_featured_good + '.txt')


# print(soup.prettify()) # Identa todas las etiquetas
with open(full_path_1, 'w', encoding='utf-8') as file:
    file.write(text_featured_articled)
    
with open(full_path_2, 'w', encoding='utf-8') as file:
    file.write(text_featured_good)
