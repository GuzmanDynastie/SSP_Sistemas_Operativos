'''El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:
Generar un DataFrame con los datos del fichero.Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, 
los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filasMostrar por pantalla
los datos del pasajero con identificador 148.Mostrar por pantalla las filas pares del DataFrame.Mostrar por pantalla los nombres de las 
personas que iban en primera clase ordenadas alfabéticamente.Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.Eliminar del DataFrame los pasajeros con edad desconocida.
Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.Añadir una nueva columna booleana para ver si el pasajero 
era menor de edad o no.Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.'''

import pandas as pd

df = pd.read_csv('Activities/Practice 2/titanic.csv')
titanic = df

def show_menu():
    print("1. Dimensiones del DataFrame")
    print("2. Numero de datos que contiene")
    print("3. Nombre de las filas y columnas")
    print("4. Tipos de datos de las columnas")
    print("5. 10 primera y 10 ultimas filas")
    print("6. Mostrar los datos del pasajero 148")
    print("7. Mostrar filas pares del DataFrame")
    print("8. Mostrar personas en primera clase")
    print("9. Porcentaje de personas que sobrevivieron y murieron")
    print("10. Personas que sobrevivieron en cada clase")
    print("11. Elimminar del DataFrame los pasajeros con edad desconocida")
    print("12. Mostrar media de las mujeres que viajaban en cada clase")
    print("13. Agregar columna booleana para mayotia de edad")
    print("14. Porcentaje de menores y mayores de edad que sobrevivieron en cada clase")
    print("15. Salir")

    while True:
        try:
            option = int(input("\n Selecciona una opcion: -> "))
            break
        except ValueError:
            print("Caracter invalido\n")
    return option

def rows_columns():
    print(f'NOMBRES DE LAS FILAS\n {titanic.index}\n')
    print(f'NOMBRES DE LAS COLUMNAS\n {titanic.columns}\n')

def show_first_class_passengers():
    first_class_names = titanic[titanic['Pclass'] == 1]['Name'].sort_values()
    print(f'Nombres de personas en primera clase ordenados alfabéticamente:\n{first_class_names}\n')

def show_survival_percentage():
    survival_percentage = titanic['Survived'].value_counts(normalize=True) * 100
    print(f'Porcentaje de personas que sobrevivieron y murieron:\n{survival_percentage}\n')

def show_survival_by_class():
    survival_by_class = titanic.groupby('Pclass')['Survived'].mean() * 100
    print(f'Porcentaje de personas que sobrevivieron en cada clase:\n{survival_by_class}\n')

def remove_unknown_age_passengers():
    titanic.dropna(subset=['Age'], inplace=True)
    print('Pasajeros con edad desconocida eliminados del DataFrame.\n')

def show_average_age_females_by_class():
    average_age_female_by_class = titanic[titanic['Sex'] == 'female'].groupby('Pclass')['Age'].mean()
    print(f'Edad media de mujeres que viajaban en cada clase:\n{average_age_female_by_class}\n')

def add_age_category_column():
    titanic['IsMinor'] = titanic['Age'] < 18
    print('Columna booleana agregada para indicar si el pasajero es menor de edad o no.\n')

def show_survival_by_age_class():
    survival_by_age_class = titanic.groupby(['Pclass', 'IsMinor'])['Survived'].mean() * 100
    print(f'Porcentaje de menores y mayores de edad que sobrevivieron en cada clase:\n{survival_by_age_class}\n')

options = {
    1: lambda: print(f'DIMENSIONES\n {titanic.shape}\n'),
    2: lambda: print(f'DATOS EN EL FRAME\n{titanic.size}\n'),
    3: rows_columns,
    4: lambda: print(f'TIPOS DE DATOS DE COLUMNA\n{titanic.dtypes}\n'),
    5: lambda: print(f'{titanic.head(10), titanic.tail(10)}\n'),
    6: lambda: print(f'Datos del pasajero con ID 148:\n{titanic.loc[147]}\n'),
    7: lambda: print(f'FILAS PARES DEL DATAFRAME\n{titanic.iloc[::2]}\n'),
    8: show_first_class_passengers,
    9: show_survival_percentage,
    10: show_survival_by_class,
    11: remove_unknown_age_passengers,
    12: show_average_age_females_by_class,
    13: add_age_category_column,
    14: show_survival_by_age_class,
    15: exit
}

while True:
    option = show_menu()
    print("------------------------------------")
    options.get(option, exit)()

    if option == 15:
        break