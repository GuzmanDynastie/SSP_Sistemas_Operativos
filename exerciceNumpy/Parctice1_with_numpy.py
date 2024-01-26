import numpy as np

def validarEntero(entero):
    try:
        numero = int(entero)
        return True
    except ValueError:
        return False

def obtener_matriz(size):
    matriz = []
    for x in range(size):
        while True:
            valor = input(f'Ingrese los valores para su matriz en la posicion {x + 1} -> ')
            if validarEntero(valor):
                matriz.append(int(valor))
                break
            else:
                print("Por favor, ingrese solo numeros enteros.")

    return matriz

def obtener_tamano_matriz():
    while True:
        valor = input("Ingrese el tamaño para sus matrices: ")
        if validarEntero(valor) and int(valor) > 0:
            return int(valor)
        else:
            print("Por favor, ingrese un numero entero mayor que 0 para el tamaño de las matrices.")

print("Matrices array1 y array2")
tamanio_matrices = obtener_tamano_matriz()

print("\n -Matriz 1")
array1 = np.array([obtener_matriz(tamanio_matrices) for _ in range(tamanio_matrices)])

print("\n -Matriz 2")
array2 = np.array([obtener_matriz(tamanio_matrices) for _ in range(tamanio_matrices)])

print("\nMatriz 1:")
print(array1)

print("\nMatriz 2:")
print(array2)

print("\n -------------------------------------------- \n")

print("SUMA")
sumResult = np.add(array1, array2)
print(sumResult)

print("\n -------------------------------------------- \n")

print("RESTA")
restResult = np.subtract(array1, array2)
print(restResult)

print("\n -------------------------------------------- \n")

print("MULTIPLICACION")
multiplicationResult = np.dot(array1, array2)
print(multiplicationResult)

print("\n -------------------------------------------- \n")

print("DIVISION")
try:
    inverseArray = np.linalg.inv(array1)
    divisionResult = np.dot(array2, inverseArray)
    print(divisionResult)
except np.linalg.LinAlgError:
    print("La matriz no es invertible, la division no es posible.")
except ValueError:
    print("Las matrices no cumplen con las dimensiones requeridas para la division.")
    
print("\n -------------------------------------------- \n")