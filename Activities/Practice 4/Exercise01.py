'''
El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Crear un dataframe con Pandas y a partir de él 
generar los siguientes diagramas.

1.- Diagrama de sectores con los fallecidos y supervivientes.
2.- Histograma con las edades.
3.- Diagrama de barras con el número de personas en cada clase.
4.- Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase.
5.- Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase.
'''
from matplotlib import pyplot as plt
from pylab import *
import math
import pandas as pd
import numpy as np
import seaborn as sns

path = 'Activities/Practice 4/Files/titanic.csv'

# Diagrama de sectores con los fallecidos y supervivientes.
def Graph_1(path):
    file_titanic = pd.read_csv(path)
    titanic = file_titanic
    
    deceased, survivor = titanic['Survived'].value_counts()

    # Crea el diagrama de sectores
    fig, ax = plt.subplots()
    ax.pie([deceased, survivor], labels=['Fallecidos', 'Sobrevivientes'], autopct='%1.2f%%')
    ax.axis('equal')  # Para asegurar que el círculo se vea como un círculo

    plt.show()


# Histograma con las edades.
def Graph_2(path):
    file_titanic = pd.read_csv(path)
    titanic = file_titanic
    # Obtenemos edades con decimales y sin NaNs
    ages_decimal = titanic[~titanic["Age"].isnull()]["Age"].astype("float").values
    ages_nan = titanic["Age"].values

    # Convertimos a enteros y ordenamos
    ages = np.round(ages_decimal).astype(np.int_)
    array_sorted = np.sort(ages)
    unique_numbers, counts = np.unique(array_sorted, return_counts=True)

    for i, (number, count) in enumerate(zip(unique_numbers, counts)):
        print(f"Número {number} aparece {count} veces.")

    # Limpiamos datos y creamos columnas adicionales
    titanic["Age"] = pd.to_numeric(titanic["Age"], errors="coerce")
    not_ages = titanic["Age"].isna().sum()

    # Definimos rangos y etiquetas para las categorías
    bins = [0, 10, 20, 30, 40, 50, 60, 70, float("inf")]
    labels = ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "Sin registro"]

    # Agregamos una nueva columna 'AgeCategory' al DataFrame
    titanic["AgeCategory"] = pd.cut(titanic["Age"], bins=bins, labels=labels, right=False)

    # Contamos las edades en cada categoría
    counts = titanic["AgeCategory"].value_counts()
    counts.loc["Sin registro"] = not_ages

    # Ordenamos las categorías por los límites definidos en 'bins'
    counts = counts.reindex(labels, fill_value=0)

    # Gráfico de barras
    figura, ax = plt.subplots()
    bars = ax.bar(counts.index, counts, color=sns.color_palette("husl", len(counts)))

    # Títulos y etiquetas
    ax.set_xlabel("Categoría de Edades")
    ax.set_ylabel("Cantidad")
    ax.set_title("Distribución de Edades en Categorías")

    # Legenda
    legend_labels = list(counts.index)
    ax.legend(bars, legend_labels)

    # Etiquetas con los valores en las barras
    for i, v in enumerate(counts):
        ax.text(i, v + 5, str(v), ha="center", va="bottom")

    plt.show()



# Diagrama de barras con el número de personas en cada clase.
def Graph_3(path):
    file_titanic = pd.read_csv(path)
    titanic = file_titanic

    class_titanic = np.array(titanic['Pclass']) # Obtengo el arreglo de todas las clases
    array_sorted = np.sort(class_titanic) # Ordeno todas las clases

    unique_values, counts = np.unique(array_sorted, return_counts=True) # Retorna el conteo del valor y del cuantas veces se repite

    for value, count in zip(unique_values, counts): # Esto es opcional
        print(f'El número {value} se repite {count} veces') # Imprime el numero y la suma de las repeticiones del mismo

    fig, ax = plt.subplots() # Crea una nueva figura y un conjunto de ejes
    bars = ax.bar(range(len(unique_values)), counts, color=sns.color_palette('husl', len(unique_values))) # Se crean los graficos en el eje ax (sirve para reducir codigo)

    ax.set_xticks(range(len(unique_values))) # Se proporciona la secuencia de posiciones generada con range(len(unique_values))
    ax.set_xticklabels(unique_values) # Se proporciona el array unique_values como etiquetas.

    ax.set_xlabel('Clases')
    ax.set_ylabel('Cantidades')
    ax.set_title('Número de personas en cada clase')

    labels = (f'Clase {i + 1}' for i in range(len(unique_values))) # Esto crea una expresión generadora que produce etiquetas del tipo "Clase 1", "Clase 2", ..., "Clase n", donde n es la longitud de unique_values. 
    ax.legend(bars, labels) #  Esto agrega una leyenda al gráfico utilizando las barras (bars) y las etiquetas proporcionadas.

    for i, v in zip(range(len(unique_values)), counts): # Asigna los datos correspondientes a cada barra
        ax.text(i, v, str(v), ha='center', va='bottom')

    plt.show()


# Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase.
def Graph_4(path):
    file_titanic = pd.read_csv(path)
    titanic = file_titanic

    survived_class_1 = np.array(titanic[(titanic.Pclass == 1) & (titanic.Survived == 1)]).shape[0]  
    deceased_class_1 = np.array(titanic[(titanic.Pclass == 1) & (titanic.Survived == 0)]).shape[0]
    survived_class_2 = np.array(titanic[(titanic.Pclass == 2) & (titanic.Survived == 1)]).shape[0] 
    deceased_class_2 = np.array(titanic[(titanic.Pclass == 2) & (titanic.Survived == 0)]).shape[0] 
    survived_class_3 = np.array(titanic[(titanic.Pclass == 3) & (titanic.Survived == 1)]).shape[0]   
    deceased_class_3 = np.array(titanic[(titanic.Pclass == 3) & (titanic.Survived == 0)]).shape[0] 

    data_labels = ['S Class 1', 'M Class 1', 'S Class 2', 'M Class 2', 'S Class 3', 'M Class 3']

    data = np.array([survived_class_1, deceased_class_1, survived_class_2, deceased_class_2, survived_class_3, deceased_class_3])

    fig, ax = plt.subplots()
    bars = ax.bar(range(len(data)), data, color=sns.color_palette('husl', len(data)))

    ax.set_xticks(range(len(data)))
    ax.set_xticklabels(data_labels)

    ax.set_xlabel('Clases')
    ax.set_ylabel('Cantidades')
    ax.set_title('Numeros de personas en cada clase')

    labels = (f'{data_labels[i]}' for i in range(len(data_labels)))
    ax.legend(bars, labels)

    for i, v in zip(range(len(data)), data):
        ax.text(i, v, str(v), ha='center', va='bottom') 

    plt.show()


# Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase.
def Graph_5(path):
    file_titanic = pd.read_csv(path)
    titanic = file_titanic

    survived_class_1 = np.array(titanic[(titanic.Pclass == 1) & (titanic.Survived == 1)]).shape[0]  
    deceased_class_1 = np.array(titanic[(titanic.Pclass == 1) & (titanic.Survived == 0)]).shape[0]
    survived_class_2 = np.array(titanic[(titanic.Pclass == 2) & (titanic.Survived == 1)]).shape[0] 
    deceased_class_2 = np.array(titanic[(titanic.Pclass == 2) & (titanic.Survived == 0)]).shape[0] 
    survived_class_3 = np.array(titanic[(titanic.Pclass == 3) & (titanic.Survived == 1)]).shape[0]   
    deceased_class_3 = np.array(titanic[(titanic.Pclass == 3) & (titanic.Survived == 0)]).shape[0] 
    
    total_class_1 = survived_class_1 + deceased_class_1
    total_class_2 = survived_class_2 + deceased_class_2
    total_class_3 = survived_class_3 + deceased_class_3

    data_labels = ['Clase 1', 'Clase 2', 'Clase 3']
    data = np.array([total_class_1, total_class_2, total_class_3])

    fig, ax = plt.subplots()
    bars = ax.bar(range(len(data)), data, color=sns.color_palette('husl', len(data)))

    ax.set_xticks(range(len(data)))
    ax.set_xticklabels(data_labels)

    ax.set_xlabel('Clases')
    ax.set_ylabel('Cantidades')
    ax.set_title('Numero de personas en cada clase')

    labels = (f'{data_labels[i]}' for i in range(len(data_labels)))
    ax.legend(bars, labels)

    for i, v in zip(range(len(data)), data):
        ax.text(i, v, str(v), ha='center', va='bottom')

    plt.show()

path = 'Activities/Practice 4/Files/titanic.csv'

Graph_1(path) # Diagrama de sectores con los fallecidos y supervivientes.
Graph_2(path) # Histograma con las edades.
Graph_3(path) # Diagrama de barras con el número de personas en cada clase.
Graph_4(path) # Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase.
Graph_5(path) # Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase.