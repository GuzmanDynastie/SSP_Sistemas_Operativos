import numpy as np

'''
a = np.array([1,2,3,5,8,4])
print(np.sort(a))

b = np.arange(4)
c = np.arange(2,9,2)
d = np.linspace(0,10,num=5)
print(b)
print(c)
print(d)

e = np.concatenate((b,c))
print(e)

#Para agregar valores a numpy primero se necesita agregar una lista 
lista = [1,2,3,4]
f = np.array(lista)
print(lista)

print(f)
print(f.shape)
print(f.size)
print(f.ndim) #Numero de ejes

g = f.reshape(2,2)
print(g)
print(f[1:])
print(f[:2])
print(f[-2])

h = np.array([[1,2],[3,4]])
i = np.array([[1,2],[3,4]])
print(h)
print(h+i)
print(h-i)
print(h*i)
print(h/i)
'''

j = np.array([1,2,3,4])
print(j.sum())

k = np.array([[1,1],[2,2]])
print(k.sum(axis=0))
print(k.sum(axis=1))

