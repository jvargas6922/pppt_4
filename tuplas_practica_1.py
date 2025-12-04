"""
¿En qué consistirá la Demo?
Vamos a simular un sistema que guarda coordenadas geográficas usando tuplas para asegurar que no se
modifiquen accidentalmente.
1- Crear una tupla con las coordenadas de una ciudad (listo)
2- Mostrar las coordenadas por pantalla (listo)
3- Acceder al valor de latitud y longitud por índice (listo)
4- Intentar modificar la tupla (y provocar un error) (listo)
5- Reemplazar la tupla completa si es necesario (no un solo valor)(listo)
6- Usar tuplas dentro de una lista para múltiples registros (listo)
7- Iterar sobre la lista de tuplas y mostrar cada ciudad (listo)
8- Imprimir mensajes como: "La ciudad está ubicada en (lat, long)" (listo)
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


#Usar tuplas dentro de una lista para múltiples registros
ciudades_coordenadas = [
    ("Santiago", -33.45694, -70.64827),
    ("Buenos Aires", -34.6037, -58.3816),
    ("Lima", -12.0464, -77.0428),
    ("Bogotá", 4.7110, -74.0721)
]

# print(ciudades_coordenadas)
# print(ciudades_coordenadas[0])

print("------------------")
print(ciudades_coordenadas[3])
print("------------------")

#Iterar sobre la lista de tuplas y mostrar cada ciudad
for ciudad in ciudades_coordenadas:
    nombre_ciudad = ciudad[0]
    latitud_ciudad = ciudad[1]
    longitud_ciudad = ciudad[2]
    print(f"La ciudad de {nombre_ciudad} está ubicada en ({latitud_ciudad}, {longitud_ciudad})")