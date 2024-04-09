import requests
from bs4 import BeautifulSoup

website = 'https://subslikescript.com/movie/Titanic-120338'
resultado = requests.get(website)

contenido = resultado.text
# soup = BeautifulSoup(contenido)
soup = BeautifulSoup(contenido, 'lxml') # signa el formato
# caja = soup.find('article', class_='main-article') # Busca por etiquetas 
# texto = caja.find('h1').get_text() # Seleccionas la etiqueta precisa y obtienes el texto

texto = soup.find('article', class_='main-article').find('h1').get_text() # Puedes realizar busqueda por una sola linea

caja1 = soup.find('div', class_='full-script').get_text(strip=True, separator=' ')

texto_pPlot = soup.find('p', class_='plot').get_text()
# print(soup.prettify()) # Identa todas las etiquetas
print(texto_pPlot)

