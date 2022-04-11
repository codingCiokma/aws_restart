#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34,
#y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
#Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

#1. Registro el valor que la persona ingrese
numero = input("Favor Ingresar el numero de telefono en el siguiente formato prefijo-número-extension:\n")

#2. Separo el valor mediante el caracter guion(-), esto me va a devolver una lista
arrayNumber = numero.split("-")

for item in arrayNumber:
    print("componente ", item)

#imprimo el numero sin el prefijo ni la extension
if len(arrayNumber) == 3:
    print(f"El resultado obtenido / El numero final  es : {arrayNumber[1]}")
else:
    print("Oops el valor que ingresaste no cumple con el requisto prefijo-número-extension")
    
#
