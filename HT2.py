#Ejercicio 1
n=int(input("Introduce la altura del triangulo (Número entero positivo):"))
for i in range(n):
    for j in range(i+1):
        print("*" , end="")
    print("")
#-------------
#Ejercicio 2
#-------------
numero=int(input("Ingresa un numero entero (Positivo )"))
#condicion para que sea numero entero positivos 
while numero<0:      
     print(">>Error, (Debe ser un número entero Positivo ):")
     numero=int(input("Ingresa un numero entero (Positivo ):"))
for i in range(numero, -1, -1):#se define el rango 
    print(i, end=", ")
#-------------
#Ejercicio 3
#-------------


y=int(input("Ingresa un numero entero (Positivo )"))
#condicion para que sea numero entero positivos 
while y<0:      
     print(">>Error, (Debe ser un número entero Positivo ):")
     y=int(input("Ingresa un numero entero (Positivo ):"))


numero= int(input("¿Qué número quieres saber si es primo? "))
valor= range(2,numero)
contador = 0
for n in valor:
  if numero % n == 0:
    contador +=1
    print("divisor:", n)
if contador>0:
  print("El número no es primo" )
else:
  print("El nÚmero es primo")
