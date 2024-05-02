import pandas as pd

# 1. Generar un DataFrame con los datos del fichero
df = pd.read_csv('./Activities/Practice 10/CSV/titanic.csv')

# 2. Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
print("Dimensiones del DataFrame:", df.shape)
print("\nNúmero de datos que contiene:", df.size)
print("\nNombres de las columnas:", df.columns.to_list())
print("\nTipos de datos de las columnas:\n", df.dtypes)
print("\nPrimeras 10 filas:\n", df.head(10))
print("\nÚltimas 10 filas:\n", df.tail(10))

# 3. Mostrar por pantalla los datos del pasajero con identificador 148
print("\nDatos del pasajero con identificador 148:\n", df.loc[147])

# 4. Mostrar por pantalla las filas pares del DataFrame
print("\nFilas pares del DataFrame:\n", df.iloc[::2])

# 5. Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente
print("\nNombres de las personas que iban en primera clase ordenadas alfabéticamente:\n", df[df['Pclass'] == 1]['Name'].sort_values())

# 6. Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron
sobrevivientes = df['Survived'].value_counts(normalize=True) * 100
print("\nPorcentaje de personas que sobrevivieron y murieron:\n", sobrevivientes)

# 7. Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase
sobrevivientes_clase = df.groupby('Pclass')['Survived'].mean() * 100
print("\nPorcentaje de personas que sobrevivieron en cada clase:\n", sobrevivientes_clase)

# 8. Eliminar del DataFrame los pasajeros con edad desconocida
df_sin_edad_desconocida = df.dropna(subset=['Age'])
df_sin_edad_desconocida.to_csv('./Activities/Practice 10/CSV/titanic_sin_edad_desconocida.csv', index=False)

# 9. Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase
edad_media_mujeres = df[df['Sex'] == 'female'].groupby('Pclass')['Age'].mean()
print("\nEdad media de las mujeres que viajaban en cada clase:\n", edad_media_mujeres)

# 10. Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no
df['Menor de Edad'] = df['Age'] < 18
df.to_csv('./Activities/Practice 10/CSV/titanic_con_menor_de_edad.csv', index=False)

# 11. Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase
sobrevivientes_por_edad_clase = df.groupby(['Pclass', 'Menor de Edad'])['Survived'].mean() * 100
print("\nPorcentaje de menores y mayores de edad que sobrevivieron en cada clase:\n", sobrevivientes_por_edad_clase)
