"""
Tuplas en Python
Una tupla es una estructura de datos ordenada e inmutable. Se utiliza cuando queremos almacenar datos
que no deben cambiar a lo largo del tiempo.
🔧 Características clave:
● Se define con paréntesis: ()
● Accesible por índice como las listas
● Ocupa menos memoria y es más rápida que una lista
● Muy útil para datos constantes (como coordenadas)
"""
"""
Diferencias entre listas y tuplas:
- Listas:
  ● Definidas con corchetes: []
  ● Mutables (pueden cambiar)
  ● Más lentas y ocupan más memoria
- Tuplas:
  ● Definidas con paréntesis: ()
  ● Inmutables (no pueden cambiar)
  ● Más rápidas y ocupan menos memoria

"""

coordenadas_1 = [10.0, 20.0]
coordenadas = (10.0, 20.0)
persona = ("Ana", 25, "Argentina")

# acceder a los datos de mi tupla vs lista
# lista
# acceder a los valores
print(coordenadas_1[1])
# modificar el valor
coordenadas_1[1] = 21.0

# tupla
# acceder a los valores
print(coordenadas[1])
# modificar el valor (esto generará un error)
# coordenadas[1] = 21.0

# Ejemplo practico de una tupla
"""
uso real de una tupla para resolver un problema
    Genera un contexto de un problema que se resuelva con una tupla
"""
coordenadas_direccion = (40.12, 70.15, "oeste")
print(f"La direccion de la casa es latitud:{coordenadas_direccion[0]} longitud:{coordenadas_direccion[1]} dirección:{coordenadas_direccion[2]}")