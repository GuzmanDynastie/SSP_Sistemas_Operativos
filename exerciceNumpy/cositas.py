array1 = np.array([[1,2],[2,1]])
array2 = np.array([[2,1],[1,2]])
#Mattriz 1
print(array1)
#Matriz 2
print("\n",array2)

print("\n -------------------------------------------- \n")

print("SUMA")
sumResult = (array1 + array2)
print(sumResult)
print("\n -------------------------------------------- \n")

print("RESTA")
restResult = (array1 - array2)
print(restResult)
print("\n -------------------------------------------- \n")

'''Para poder multiplicar dos matrices, la primera debe tener el mismo numero
de columnas que filas la segunda. La matriz resultante del producto quedara 
con el mismo numerode filas de la primera y con el mismo numero de columnas
de la segunda'''

print("MULTIPLICACION")
multiplicactionResult = np.dot(array1, array2)
print(multiplicactionResult)
print("\n -------------------------------------------- \n")

'''La division de dos matrices es la multiplicacion de una matriz inversa
de la matriz divisora, y al mismo tiempo exige que la matriz divisora sea
una matriz cuadrada y que su determinante sea distinto de cero'''

print("DIVISION")
inverseArray = np.linalg.inv(array1)
divisionResult = np.dot(array2, inverseArray)
print(divisionResult)
print("\n -------------------------------------------- \n")