import pandas as pd

votos_primarias_us = pd.read_csv('exercicePandas/primary_results.csv')
df = votos_primarias_us
'''
print(df)
print(df.shape) #muestra la cantidad de indices en el doc.
print(df.head(10)) #muestra los primeros 10 datos del doc.
print(df.tail(10)) #muestra los ultimos 10 datos del doc.
print(df.dtypes) #muestra los tipos de datos de las columnas
print(df.describe()) #crea estadisticos
print(df.index) #crea el rango de indice
print(df.loc[10]) #selecciona datos de la fila y muestra sus datos
'''
df2 = df.set_index("state") #muestra como indice el parametro
print(df2)
print(df2.loc["California"])
print(df2.shape)
print(df["state"][:10])
'''
print(df[["county", "candidate"]]) #muestra todas las filas que tienen esos parametros
print(df[df.votes<=1000]) #muestra los votos menores o igual a 1000
print(df[(df.county=="Manhattan") & (df.party=="Democrat")]) #muestra los resultados que coinciden con los parametros
print(df.query("county=='Manhattan' and party=='Democrat'")) #muestra los resultados que coinciden con los parametros
'''
df_sorted = df.sort_values(by="votes", ascending=False)
print(df_sorted.head()) #Muestra los primeros 5 valores del parametro
print(df.groupby(["state", "party"]).sum()) #suma los valores separados por los parametros

df.to_csv("exercicePandas/editado.csv") #Si el archivo existe lo edita y si no lo crea
df2.to_csv("exercicePandas/editado1.csv")
