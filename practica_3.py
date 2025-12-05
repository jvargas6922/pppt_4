"""
Sistema de gestión de estudiantes (listas + tuplas)
Contexto: 🙌
Una institución educativa necesita registrar y consultar información de sus estudiantes. Cada estudiante
tiene un nombre, una edad y una ciudad de residencia. Se requiere un sistema básico para almacenar los
datos, listarlos, buscar estudiantes por ciudad y obtener estadísticas.
Consigna: ✍
● Desarrollar un programa que permita: 
● Registrar múltiples estudiantes representados por tuplas dentro de una lista.(listo)
● Mostrar todos los registros con formato legible. (listo)
● Permitir consultar cuántos estudiantes son de una ciudad específica.(listo)
● Mostrar la edad promedio de los estudiantes registrados. (listo)
"""

"""
Entrada:
    input: nombre, edad, ciudad (varias veces hasta que el usuario decida parar)

Proceso:
    - Almacenar cada estudiante como una tupla (nombre, edad, ciudad) en una lista.
    - Mostrar todos los estudiantes con formato legible.
    - Contar y mostrar cuántos estudiantes son de una ciudad específica.
    - Calcular y mostrar la edad promedio de los estudiantes registrados.

Salida:
    - Lista de estudiantes con formato legible.
    - Número de estudiantes de una ciudad específica.
    - Edad promedio de los estudiantes.

"""

estudiantes = []
while True:
    # datos del estudiante
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    edad_estudiante = input("Ingrese la edad del estudiante: ")
    ciudad_estudiante = input("Ingrese la ciudad de residencia del estudiante: ")

    # validaciones de los campos

    # crear tupla de los datos del estudiante
    estudiante = (nombre_estudiante, int(edad_estudiante), ciudad_estudiante)
    # agregar la tupla a la lista de estudiantes
    estudiantes.append(estudiante)
    operacion = input("¿Desea agregar otro estudiante? (s/n): ")
    if operacion.lower() == 'n':
        break

# Mostrar todos los registros de los estudiantes
print(f"Estudiantes registrados: {estudiantes}")

for estudiante in estudiantes:
    print(f"nombre: {estudiante[0]} | edad: {estudiante[1]} | ciudad: {estudiante[2]}")


print("----- Consulta por ciudad -----")
conjunto_estudiantes = set(estudiantes)
print(conjunto_estudiantes)

input_ciudad = input("Ingrese la ciudad para consultar estudiantes: ")
ciudad_ingresada =[]
for estudiante in estudiantes:
    if estudiante[2] == input_ciudad:
        ciudad_ingresada.append(estudiante)

print(f" Cantidad de estudiantes en la ciudad ingresada: {len(ciudad_ingresada)}")

edad_estudiantes = []
for estudiante in estudiantes:
    edad_estudiantes.append(estudiante[1])

edad_promedio =  round(sum(edad_estudiantes) / len(edad_estudiantes))
print(f"La edad promedio de los estudiantes es: {edad_promedio}")


"""
[
    ('Joffred', 39, 'Santiago'),
    ('Daniela', 36, 'Santiago'), 
    ('Alejandro', 33, 'Macul'), 
    ('Oscar', 44, 'Cerrillos'), 
    ('Raul ', 57, 'San Joaquin')
]
"""

