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
while opcion != "3":
  print("es mi menu")
  opcion= input("ingrese la opcion deseada, 3 para salir")