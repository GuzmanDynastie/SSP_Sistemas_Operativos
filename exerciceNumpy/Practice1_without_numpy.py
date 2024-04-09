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
array1 = [obtener_matriz(tamanio_matrices) for _ in range(tamanio_matrices)]

print("\n -Matriz 2")
array2 = [obtener_matriz(tamanio_matrices) for _ in range(tamanio_matrices)]

print("\nMatriz 1:")
for row in array1:
    print(row)

print("\nMatriz 2:")
for row in array2:
    print(row)

print("\n -------------------------------------------- \n")

print("SUMA")
sumResult = [[array1[i][j] + array2[i][j] for j in range(len(array1[0]))] for i in range(len(array1))]
for row in sumResult:
    print(row)

print("\n -------------------------------------------- \n")

print("RESTA")
restResult = [[array1[i][j] - array2[i][j] for j in range(len(array1[0]))] for i in range(len(array1))]
for row in restResult:
    print(row)

print("\n -------------------------------------------- \n")

print("MULTIPLICACION")
multiplicationResult = [[sum(array1[i][k] * array2[k][j] for k in range(len(array2))) for j in range(len(array2[0]))] for i in range(len(array1))]
for row in multiplicationResult:
    print(row)

print("\n -------------------------------------------- \n")

print("DIVISION")
#Calcula la matriz inversa
determinant = array1[0][0] * array1[1][1] - array1[0][1] * array1[1][0]
if determinant != 0:
    inverseArray = [[array1[1][1] / determinant, -array1[0][1] / determinant],
                    [-array1[1][0] / determinant, array1[0][0] / determinant]]
    divisionResult = [[sum(array2[i][k] * inverseArray[k][j] for k in range(len(inverseArray))) for j in range(len(inverseArray[0]))] for i in range(len(array2))]
    for row in divisionResult:
        print(row)
else:
    print("La matriz no es invertible, la division no es posible.")
    
print("\n -------------------------------------------- \n")