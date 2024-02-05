'''El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes 
columnas: nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), 
Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), 
volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros). 
Construir una función que construya un DataFrame a partir del un fichero con el formato anterior y 
devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.'''

import pandas as pd

def company_statistics(file_path):
    df = pd.read_csv(file_path, delimiter=';')

    # Convierte las columnas numéricas al formato adecuado (reemplaza ',' por '.')
    df['Final'] = pd.to_numeric(df['Final'].str.replace(',', '.'), errors='coerce')
    df['Máximo'] = pd.to_numeric(df['Máximo'].str.replace(',', '.'), errors='coerce')
    df['Mínimo'] = pd.to_numeric(df['Mínimo'].str.replace(',', '.'), errors='coerce')
    df['Volumen'] = pd.to_numeric(df['Volumen'].str.replace('.', '').str.replace(',', '.'), errors='coerce')
    df['Efectivo'] = pd.to_numeric(df['Efectivo'].str.replace('.', '').str.replace(',', '.'), errors='coerce')

    # Calcula la media solo para las columnas numéricas
    summary = pd.DataFrame({
        'Mínimo': df[['Final', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo']].min(),
        'Máximo': df[['Final', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo']].max(),
        'Media': df[['Final', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo']].mean()
    })

    summary.to_csv('Activities/Practice 2/edit.csv')

    return summary

file_path = 'Activities/Practice 2/cotizacion.csv'
result = company_statistics(file_path)
print(result)