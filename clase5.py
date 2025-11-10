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