print("-------------------------------------------")
print("\n Marcos_Itzep")
#-------------------------------------
#Ejercicio 1
#-------------------------------------
x  =  input ( "Escribe tu contraseña:" )  #contraseña
entrada="contraseña"
if entrada == x.lower():
    print("La contaseña coincide")
    print("Bienvenido :v ")
else:
    print("La contraseña no coincide")
print("Su contraseña es: ",x)
#-------------------------------------
#Ejercicio 2
#-------------------------------------
nombre = input("¿Cómo te llamas? ")
genero = input("¿Cuál es tu sexo (M o H)? ")
if genero == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print("Tu grupo es " + grupo)