import requests  # Importa la biblioteca requests para realizar solicitudes HTTP
from bs4 import BeautifulSoup  # Importa BeautifulSoup para analizar y extraer información de HTML
import cfscrape  # Importa cfscrape para evitar la verificación de CloudFare Anti-bot
import os  # Importa el módulo os para interactuar con el sistema operativo
import pprint  # Importa pprint para imprimir estructuras de datos de forma legible
import time  # Importa time para funciones relacionadas con el tiempo
import urllib.error  # Importa urllib.error para manejar errores en operaciones URL
import urllib.request  # Importa urllib.request para abrir y leer URLs

# Crea una sesión de requests y habilita la verificación SSL
session = requests.Session()
session.verify = True

# Crea un scraper utilizando cfscrape para evitar la verificación de CloudFare Anti-bot
scraper = cfscrape.create_scraper()

# Realiza una solicitud GET a la URL especificada
r = scraper.get("https://hidralistico.com.mx/categoria-producto/juegos-de-cartas/yu-gi-oh/carta-suelta/zombie-horde/")

# Inicializa listas para almacenar imágenes y productos
listaImagen = list()
listaProducto = list()

# Crea un objeto BeautifulSoup a partir del contenido HTML de la respuesta
soup = BeautifulSoup(r.content, "html.parser")

# Encuentra todos los elementos HTML con la clase "box-image" que contienen las imágenes de los productos
fichaProductos = soup.find_all('div', class_="box-image")

counter = 0  # Inicializa un contador

# Itera sobre cada elemento encontrado en 'fichaProductos'
for element in fichaProductos:
    img_url = element.find("img")['data-lazy-src']  # Extrae la URL de la imagen

    try:
        with urllib.request.urlopen(img_url) as web_file:  # Abre la URL de la imagen
            data = web_file.read()  # Lee los datos de la imagen

            # Guarda la imagen localmente en formato .jpg con un nombre basado en el contador
            with open(str(counter) + ".jpg", mode='wb') as imagen:
                imagen.write(data)  # Escribe los datos de la imagen en el archivo
                counter += 1  # Incrementa el contador

    except urllib.error.URLError as e:  # Maneja errores de tipo URLError
        print(e)  # Imprime el error en caso de excepción