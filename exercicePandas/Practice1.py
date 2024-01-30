import pandas as pd

lista_alumnos = pd.DataFrame({
    "Nombre": ["Juan", "Pedro", "Emmanuel"],
    "Apellido": ["Lopez", "Jimenez", "Guzman"],
    "Edad": [18, 21, 28],
    "Carrera": ["Abogado", "Ingeniero", "Sistemas"]
})

lista_alumnos1 = pd.DataFrame(
[
    ["Juan", "Lopez", 18, "Abogado"],
    ["Pedro", "Jimenez", 21, "Ingeniero"],
    ["Emmanuel", "Guzman", 28, "Sistemas"]
],
     columns=["Nombre", "Apellido", "Edad", "Carrera"])

print(lista_alumnos)
print(lista_alumnos1)