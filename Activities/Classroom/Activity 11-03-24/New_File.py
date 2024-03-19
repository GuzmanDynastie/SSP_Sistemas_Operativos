import requests
from bs4 import BeautifulSoup
import pandas as pd

categoria = 'zombie-horde'
listaImagen = list()
listaProducto = list()

urlPagina = ('https://hidralistico.com.mx/categoria-producto/juegos-de-cartas/yu-gi-oh/carta-suelta/{}/').format(categoria)

r = requests.get(urlPagina, headers={ "User-Agent": "Chrome/50.0.2661.94" })
html = r.content
soup = BeautifulSoup(html, "html.parser")

fichaProductos = soup.find_all('div', class_="box-image")
i = 0
for element in fichaProductos:
    imagenProducto = element.find('img')['data-lazy-src']
    nombreProducto = element.find('p')['name product-title woocommerce-loop-product__title']
    print(imagenProducto)
    