"""
¿En qué consistirá la Demo?
Vamos a simular un sistema que guarda coordenadas geográficas usando tuplas para asegurar que no se
modifiquen accidentalmente.
1- Crear una tupla con las coordenadas de una ciudad (listo)
2- Mostrar las coordenadas por pantalla (listo)
3- Acceder al valor de latitud y longitud por índice (listo)
4- Intentar modificar la tupla (y provocar un error) (listo)
5- Reemplazar la tupla completa si es necesario (no un solo valor)(listo)
6- Usar tuplas dentro de una lista para múltiples registros
7- Iterar sobre la lista de tuplas y mostrar cada ciudad
8- Imprimir mensajes como: "La ciudad está ubicada en (lat, long)"
"""
#Crear una tupla con las coordenadas de una ciudad 
#coordenadas_santiago =("33°28'43´´S","70°37′56″O")
coordenadas_santiago =(-33.45694,-70.64827)

# Mostrar las coordenadas por pantalla
print("Coordenadas de Santiago:", coordenadas_santiago)

#Acceder al valor de latitud y longitud por índice
latitud = coordenadas_santiago[0]
longitud = coordenadas_santiago[1]
print(f"Latitud: {latitud}, Longitud: {longitud}")

#Intentar modificar la tupla (y provocar un error)
# coordenadas_santiago.pop(1)

#Reemplazar la tupla completa si es necesario (no un solo valor)
coordenadas_santiago = (-34.45694, -71.64827)
print("Nuevas coordenadas de Santiago:", coordenadas_santiago)
