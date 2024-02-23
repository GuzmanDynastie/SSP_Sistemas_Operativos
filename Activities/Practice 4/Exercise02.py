'''
Ejercicio2
El fichero bancos.csv contiene las cotizaciones de los principales bancos de España con : Empresa (nombre de la empresa), 
Apertura (precio de la acción a la apertura de bolsa), Máximo (precio máximo de la acción durante la jornada), 
Mínimo (precio mínimo de la acción durante la jornada), Cierre (precio de la acción al cierre de bolsa), 
Volumen (volumen al cierre de bolsa). Construir una función reciba el fichero bancos.csv y cree un diagrama de líneas con las series temporales 
de las cotizaciones de cierre de cada banco.
'''
from matplotlib import pyplot as plt
from pylab import *
import math
import pandas as pd
import numpy as np
import seaborn as sns

path = 'Activities/Practice 4/Files/bancos.csv'

def show_lineGraph(path):
    # Paso 1: Leer el archivo bancos.csv
    data = pd.read_csv(path)

    # Paso 2: Procesar los datos
    # Suponiendo que el nombre de la columna para el nombre del banco es 'Empresa' y para la fecha es 'Fecha'
    # y el nombre de la columna para la cotización de cierre es 'Cierre'
    banks = data['Empresa'].unique()
    for bank in banks:
        bank_data = data[data['Empresa'] == bank]
        plt.plot(bank_data['Fecha'], bank_data['Cierre'], label=bank)

    # Paso 3: Crear el diagrama de líneas
    plt.xlabel('Fecha')
    plt.ylabel('Cotización de Cierre')
    plt.title('Series Temporales de Cotizaciones de Cierre por Banco')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

show_lineGraph(path)

