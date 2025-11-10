#conjuntos o sets
"""
{}
Realizar operacion conjuntos
No son ordenados
pero si son mutables
no permite datos duplicados
"""

conjunto = set() #crear conjunto vacio
set1 ={1,2,3,4,5,5}
set2 = {5,8,9}
print(set1)
print(set1.union(set2)) #unir dos conjuntos
print(set1.intersection(set2)) #interseccion entre dos conjuntos
print(set1.difference(set2)) #diferencia entre dos conjuntos
print(set2.difference(set1)) #diferencia entre dos conjuntos

#metodos de conjuntos
set1.add(10) # agrega elemento
set1.remove(1) #elimina elemento
print(set1)
set1.clear() #elimina todos los elementos
print(set1)