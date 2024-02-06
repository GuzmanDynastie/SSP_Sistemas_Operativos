'''Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y devuelva una serie con la nota mínima, 
la máxima, media y la desviación estandar.'''

import pandas as pd

def statistics_notes(dictionary_notes):
    df = pd.DataFrame(list(dictionary_notes.items()), columns=["Alumno", "Nota"])

    print(df, "\n")

    min_note = df["Nota"].min() 
    max_note = df["Nota"].max()
    medium_note = df["Nota"].mean()
    std_desviation = df["Nota"].std()

    f'{df.loc[df['Nota'].idxmin()]['Alumno']}' #Por si el profe quiere nombre del alumno para nota min y max

    statistics = pd.Series({
        'Nota minima': min_note,
        'Nota maxima': max_note,
        'Nota media': medium_note,
        'Desviacion estandar': std_desviation
    })

    return statistics

student_notes = {
    'Emmanuel': 100,
    'Mario': 90,
    'Damian': 80,
    'Jose Luis': 95,
    'Oscar': 87
}

print()

result = statistics_notes(student_notes)
print(result)