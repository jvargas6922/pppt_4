"""
Conjuntos en Python
Un set es una estructura de datos no ordenada y sin elementos duplicados. Ideal para trabajar con
colecciones únicas y operaciones matemáticas.
🔧 Características clave:
● Se define con llaves {} o con set()
● No permite elementos duplicados
● No se accede por índice (no tiene orden fijo)
● Soporta operaciones como unión, intersección, diferencia
"""
# estructura de un set
valores = {1, 2, 3, 4}
# print(valores)
duplicados = [1, 2, 2, 3, 4, 4]
valores_unicos = set(duplicados)
# print(valores_unicos)

tareas = ["pagar facturas", "estudiar", "hacer ejercicio", "pagar facturas", "leer"]
tareas_unicas = set(tareas)
# print(tareas_unicas)

"""
Operacion de union(se agregan los elementos de dos conjuntos)
    estructura
    variable_nueva = conjunto_1.union(conjunto_2)
"""
# conjunto_a = {1, 2, 3}
# conjunto_b = {3, 4, 5}

lista_1 = [1,2,2,2,2,2,3,4,5,4,4,5,5]
lista_2 = [4,5,6,7,8,8,8,9]
conjunto_lista_1 = set(lista_1)
conjunto_lista_2 = set(lista_2)
combinacion_conjuntos = conjunto_lista_1.union(conjunto_lista_2)
print(combinacion_conjuntos)

"""
Intersección(elementos comunes entre dos conjuntos)
    estructura
    variable_nueva = conjunto_1.intersection(conjunto_2)
"""
interseccion_conjuntos = conjunto_lista_1.intersection(conjunto_lista_2)
print(interseccion_conjuntos)

"""
Diferencia(elementos que están en el primer conjunto pero no en el segundo)
    estructura
    variable_nueva = conjunto_1.difference(conjunto_2)
"""

diferencia_conjuntos = conjunto_lista_1.difference(conjunto_lista_2)
print(diferencia_conjuntos)