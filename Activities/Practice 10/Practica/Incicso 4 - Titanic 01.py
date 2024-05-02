import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./Activities/Practice 10/CSV/titanic.csv')

# 1. Diagrama de sectores con los fallecidos y supervivientes
sobrevivientes = df['Survived'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(sobrevivientes, labels=['Fallecidos', 'Supervivientes'], autopct='%1.1f%%', startangle=90)
plt.title('Fallecidos y Supervivientes en el Titanic')
plt.show()

# 2. Histograma con las edades
plt.figure(figsize=(8, 6))
plt.hist(df['Age'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.title('Histograma de Edades')
plt.show()

# 3. Diagrama de barras con el número de personas en cada clase
clases = df['Pclass'].value_counts().sort_index()
plt.figure(figsize=(8, 6))
plt.bar(clases.index, clases.values, color='salmon')
plt.xlabel('Clase')
plt.ylabel('Número de Personas')
plt.title('Número de Personas en Cada Clase')
plt.xticks(clases.index, ['1ra Clase', '2da Clase', '3ra Clase'])
plt.show()

# 4. Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase
survived_clase = df.groupby(['Pclass', 'Survived'])['Survived'].count().unstack()
survived_clase.plot(kind='bar', stacked=True, figsize=(8, 6))
plt.xlabel('Clase')
plt.ylabel('Número de Personas')
plt.title('Fallecidos y Supervivientes por Clase')
plt.xticks(rotation=0)
plt.legend(['Fallecidos', 'Supervivientes'])
plt.show()

# 5. Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase
survived_clase_cumsum = survived_clase.cumsum(axis=1)
survived_clase_cumsum.plot(kind='bar', stacked=True, figsize=(8, 6))
plt.xlabel('Clase')
plt.ylabel('Número de Personas')
plt.title('Fallecidos y Supervivientes Acumulados por Clase')
plt.xticks(rotation=0)
plt.legend(['Fallecidos', 'Supervivientes'])
plt.show()