"""
Se requiere solicitar al usuario  diez calificaciones de su curso de AWS re/start
Luego de esto es necesario mostrar la media de todas estas calificaciones.
Si la media de las notas (promedio de notas) es mayor que 70 puntos mostrar el mensaje : FELICIDADES! APROBASTE. :)
Si la media es inferior a 70 entonces mostrar : RECUERDA ENCENDER LA CAMARA :(
"""

lista = []


print(f"el resultado es {lista}")

n = int(input("cuantas notas deseas pedir"))

for posicion in [0,n]:
    nota = input(f"Favor ingrese la nota {posicion} : ")
    lista.append(int(nota))
    
promedio = sum(lista)/len(lista)
print(promedio)