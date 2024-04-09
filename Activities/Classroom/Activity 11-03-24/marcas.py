import requests  # Importa la biblioteca requests para realizar solicitudes HTTP
from bs4 import BeautifulSoup  # Importa BeautifulSoup para analizar y extraer información de HTML
import cfscrape  # Importa cfscrape para evitar la verificación de CloudFare Anti-bot
import os  # Importa el módulo os para interactuar con el sistema operativo
import pprint  # Importa pprint para imprimir estructuras de datos de forma legible
import time  # Importa time para funciones relacionadas con el tiempo
import urllib.error  # Importa urllib.error para manejar errores en operaciones URL
import urllib.request  # Importa urllib.request para abrir y leer URLs
import pandas as pd

path = 'Activities/Classroom/Activity 11-03-24/images'
# path_csv = 'Activities/Classroom/Activity 11-03-24'

if not os.path.exists(path):
    os.makedirs(path)

session = requests.Session()
session.verify = True

scraper = cfscrape.create_scraper()

r = scraper.get("https://gameplanet.com/catalogo/?buscar_productos=1&product_cat=video-juegos")

listaImagen = list()
listaProducto = list()
listaPrecio = list()

soup = BeautifulSoup(r.content, "html.parser")

fichaProductos = soup.find_all('div', class_="product-small box")

counter = 0 

for element in fichaProductos:
    img_url = element.find("img")['data-lazy-src']
    des_url = element.find("a", class_='woocommerce-LoopProduct-link woocommerce-loop-product__link').getText(strip=True)
    pre_url = element.find("ins").getText(strip=True)
    pre_url_part1 = pre_url[:-2]
    pre_url_part2 = pre_url[-2:]

    # Unir las partes con un punto en el medio
    pre_url_with_dot = "{}.{}".format(pre_url_part1, pre_url_part2)
    
    listaProducto.append(des_url)
    listaPrecio.append(pre_url_with_dot)

    try:
        with urllib.request.urlopen(img_url) as web_file:
            data = web_file.read()

            with open(os.path.join(path, "Imagen" + str(counter) + ".jpg"), mode='wb') as imagen:
                imagen.write(data)
                counter += 1
                
                listaImagen.append("Imagen " + str(counter) + ".jpg")

    except urllib.error.URLError as e:
        print(e)
        
diccionario = {'Nombre':listaProducto, 'Precio':listaPrecio, 'Imagen':listaImagen}    
# print(diccionario)

df = pd.DataFrame(diccionario, columns=['Nombre', 'Precio', 'Imagen'])
df.to_csv('Activities/Classroom/Activity 11-03-24/listado_articulo.csv')