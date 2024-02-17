'''
El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Crear un dataframe con Pandas y a partir de él 
generar los siguientes diagramas.

Diagrama de sectores con los fallecidos y supervivientes.
Histograma con las edades.
Diagrama de barras con el número de personas en cada clase.
Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase.
Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase.
'''
from matplotlib import pyplot as plt
from pylab import *
import math
import pandas as pd
import numpy as np
import seaborn as sns

path = 'Activities/Practice 4/Files/titanic.csv'

file_titanic = pd.read_csv(path)
titanic = file_titanic


# Diagrama de sectores con los fallecidos y supervivientes.
'''
deceased = int(titanic[titanic.Survived == 0].shape[0])
survivor = int(titanic[titanic.Survived == 1].shape[0])

figure = plt.figure()
ax = figure.add_axes([0,0,1,1])
ax.axis('equal')
survived = ['Fallecidos', 'Sobrevivientes']
values = np.array([deceased, survivor])
ax.pie(values, labels=survived, autopct='%1.2f%%')
plt.show()
'''

# Histograma con las edades.
'''
ages_decimal = np.array(titanic[titanic.Age.notna()]['Age']) #Edades con decimales
print(ages_decimal)

ages_nan = np.array(titanic['Age']) #Edades con 'nan'
print(ages_nan)

not_ages = np.array(titanic['Age'].isna())
print(not_ages)

ages = np.array(titanic[titanic.Age.notna()]['Age']).astype(int) #Edades redondeadas
array_sorted = np.sort(ages) #Ordena la lista de menor a mayor
unique_numbers, counts = np.unique(array_sorted, return_counts=True)
for i, (number, count) in enumerate(zip(unique_numbers, counts)):
    print(f"Número {number} aparece {count} veces.")
'''
'''
titanic['Age'] = pd.to_numeric(titanic['Age'], errors='coerce') # Convierte 'Age' a tipo numérico

not_ages = titanic['Age'].isna().sum() # Calcula el número de edades sin registro
# print(f"Sin registro aparece {not_ages} veces.")

# Definir límites y etiquetas para las categorías
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, float('inf')] # Agregamos cualquier valor para que no haya problemaa 
labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', 'Sin registro'] # Labels para mostrar la informacion

# Agregar una nueva columna 'AgeCategory' al DataFrame
titanic['AgeCategory'] = pd.cut(titanic['Age'], bins=bins, labels=labels, right=False)

# Contar las edades en cada categoría
counts = titanic['AgeCategory'].value_counts()
counts.loc['Sin registro'] = not_ages

# Ordenar las categorías por los límites definidos en 'bins'
counts = counts.reindex(labels, fill_value=0)
print(counts)

# Crear la gráfica de barras
figura, ax = plt.subplots()
bars = ax.bar(counts.index, counts, color=sns.color_palette('husl', len(counts))) # sns es la libreria que me permite manejar colores

# Etiquetas y título
ax.set_xlabel('Categoría de Edades')
ax.set_ylabel('Cantidad')
ax.set_title('Distribución de Edades en Categorías')

# Agregar leyenda
legend_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', 'Sin registro']
ax.legend(bars, legend_labels)

# Añadir etiquetas con los valores en las barras
for i, v in enumerate(counts):
    ax.text(i, v + 5, str(v), ha='center', va='bottom')

plt.show()
'''


# Diagrama de barras con el número de personas en cada clase.

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