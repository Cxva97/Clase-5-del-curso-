#feedbakc while
#for
# variables estructuradas

"""
Feedback
condicionales para guiar al codigo en varios camninos en la toma de desiciones
bucles es utilizar el codigo de una manera repetitiva basada a una condicion"""

numero = 0
while numero <=10 :
    print("hola", numero)
    numero = numero +1

while numero < 100 :
    print(numero)
    numero += 1
    if numero == 50:
        print("se rompe el bucle")
        break

#menu
opcion = ""
while opcion != "3": #opcion sea diferente de 3
  print("es mi menu")
  opcion= input("ingrese la opcion deseada, 3 para salir")

#acumulador
numero = 8
numero += 1 # 8 + 1 = 9
numero -= 1 # 8 - 1 = 7

#For es el bucle mas utilizado por su robustez => PARA

for numero in range(1,10):
    print(numero)

#For es el bucle mas utilizado por su robustez => PARA

#range(inicia, final, espaciado)
for numero in range(1,10):
    print(numero)

for variable in range (1,21,2):
    print(variable)

for numero in range (100,0,-1):
    print(numero)

texto = "hola como estas"
for letra in texto:
    print(letra)

#problemas de logica
#tabla de multiplicar

"""
1x1=1
1x2=2"""

numero = int(input("ingrese un numero para ver su tabla de multiplicar: "))
for valor in range (1,11):
    print(f"{numero} x {valor} = {numero * valor}")

#fizz buzz
# pedir al usuario que ingrese un numero del 1 al 100
#si multiplico de 3 imprima fizz
#si multiplico de 5 imprima buzz
#si multiplico de 3 y 5 imprima fizzbuzz

numero= int(input("ingrese un numero del 1 al 100: "))
for valor in range(1, numero + 1):
    if valor % 3 == 0 and valor % 5 == 0:
        print("fizz buzz", end=",")
    elif valor % 3 == 0:
        print("fizz", end=",")
    elif valor % 5 == 0:
        print("buzz", end=",")
    else:
        print(valor) 

#variables estructuradas
# una variable que permite almacenar multiples info
#1. listas => vectores, array
"""
1. ordenadas
2. mutables
3. se escriben con corchetes []
"""
lista1 =["Cesar", "28 años", 450.50 , True,1,1,2,2]
print(len(lista1))
#como trabajar con cada elemento
print(lista1[3])
# como trabajar con todos los elementos a la vez
for item in lista1:
    print(item)
# metodos o herramientas especiales
lista1.append("nuevo dato")   #agrega un elemento al final de la lista
print(lista1)
lista1.pop() #elimina el ultimo elemento de la lista
print(lista1)
print(lista1.count("Cesar")) #contar coincidencias de un elemento
lista1.insert(2,"Adios") #agrega un elemento a una posicion exacta
print(lista1)
lista1.remove(2) #elimina la primera coincidencia del elemento
print(lista1)

#modificar un valor
lista1[0] = "Xavier"
print(lista1)

#crear una lista de frutas por consola
frutas= [] #lista vacia
for i in range(3): #iterar o repetir el codigo 3 veces
    fruta= input("ingrese la fruta: ")
    frutas.append(fruta)
    print(frutas)

#ingres por consola su nombre, edad, hobbie
#agregar eso a la lista persona y luego mostrar la informacion con un print

persona =[]
for i in range (3):
    if i==0:
        print("ingrese su nombre: ")
        nombre = input()
        persona.append(nombre)
    elif i==1:
        print("ingrese su edad: ")
        edad = input()
        persona.append(edad)
    else:
        print("ingrese su hobbie: ")
        hobbie= input()
        persona.append(hobbie)
        print(persona)


persona=[]
formulario = ["Nombre","edad","hobbie"]
for x in range(len(formulario)):
    llenarformulario=input(f"Ingrese {formulario[x]}: ")
    persona.append(llenarformulario)
print(persona)

persona = []
persona.append(input('Ingrese un nombre:'))
persona.append(input('Ingrese su edad:'))
persona.append(input('Ingrese un hobbie:'))
print('el nombre de la persona es',persona[0],'su edad es',persona[1],'su hoobie es', persona[2]) 

#crear un histograma
# lista=  [1,1,2,2,1,5,4,5,5,4,3,3,3]
"""
1: ***
2: **
3: ***
4: **
5: ***
"""

lista=  [1,1,2,2,1,5,4,5,5,4,3,3,3]
histograma = {}
for numero in lista:
    if numero in histograma:
        histograma[numero] += "*"
    else:
        histograma[numero] = "*" 
for clave, valor in histograma.items():
    print(f"{clave}: {valor}")  

lista=  [1,1,1,1,1,2,2,1,5,4,5,5,4,3,3,3]
for numero in range(1,6):
    print (f"{numero}: {"*"*lista.count(numero)}")

# Lista de datos
lista = [1, 1, 2, 2, 1, 5, 4, 5, 5, 4, 3, 3, 3]

# Crear un conjunto de números únicos para recorrerlos en orden
numeros = sorted(set(lista))

# Crear el histograma
for numero in numeros:
    cantidad = lista.count(numero)
    print(f"{numero}: {'*' * cantidad}")

"""
set(lista): Obtiene los números únicos de la lista.

sorted(): Ordena los números para que el histograma quede ordenado de menor a mayor.

lista.count(numero): Cuenta cuántas veces aparece cada número.

'*' * cantidad: Genera una cadena de asteriscos según la cantidad contada."""

"""obtener el numero mas grande la siguiente funciones"""
lista=[100,2,50,95,205,20]
mayor = lista[0]
for i in lista:
    if i > mayor:
        mayor = i
print("el numero mayor es:", mayor)

#tuplas
#()
#no son mutables pero si ordenadas

tupla= (1,2,2,5,"Cesar")
print(tupla[1])

#metodos especiales
print(tupla.count(2)) #contar coincidencias de un elemento
print(tupla.index("Cesar")) #da la posicion de un elemento