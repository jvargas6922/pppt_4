"""
¿En qué consistirá la Demo?
Simularemos dos listas de usuarios de diferentes plataformas y usaremos sets para encontrar coincidencias,
diferencias y valores únicos.
1- Crear dos listas de usuarios con posibles repetidos (listo)
2- Convertir las listas en conjuntos para eliminar duplicados (listo)
3- Mostrar los usuarios únicos de cada plataforma(listo)
4- Calcular la intersección (usuarios en ambas plataformas) (listo)
5- Calcular la unión (todos los usuarios sin duplicados) (listo)
6- Calcular diferencia (usuarios solo en una plataforma) (listo)
7- Usar add() y remove() para modificar un set (listo)
8- Recorrer un set con for e imprimir los resultados (listo)
"""
#1- Crear dos listas de usuarios con posibles repetidos
usuarios_plataforma = ["alice", "bob", "charlie", "alice", "dave", "eve", "bob"]
usuarios_bootcamp = ["frank", "eve", "grace", "heidi", "charlie", "ivan", "frank"]
print("Usuarios Plataforma:", usuarios_plataforma)
print("Usuarios Bootcamp:", usuarios_bootcamp)

print("\n--- Conjuntos y Operaciones ---\n")
#2- Convertir las listas en conjuntos para eliminar duplicados
u_plataforma = set(usuarios_plataforma)
u_bootcamp = set(usuarios_bootcamp)

#3- Mostrar los usuarios únicos de cada plataforma
print("Usuarios Plataforma:", u_plataforma)
print("Usuarios Bootcamp:", u_bootcamp)

print("\n--- Intersección ---\n")
#4- Calcular la intersección (usuarios en ambas plataformas)
u_comunes = u_plataforma.intersection(u_bootcamp)
print("Usuarios en ambas plataformas:", u_comunes)

print("\n--- Unión ---\n")
#5- Calcular la unión (todos los usuarios sin duplicados)
u_totales = u_plataforma.union(u_bootcamp)
print("Todos los usuarios en plataformas:", u_totales)

print("\n--- Diferencia ---\n")
#6- Calcular diferencia (usuarios solo en una plataforma)
u_diferencia = u_plataforma.difference(u_bootcamp)
print("Usuarios solo en la plataforma:", u_diferencia)

"""
como ocupar un add() y un remove() para modificar un set
    estructura
    conjunto.add(elemento) => agrega un elemento al conjunto
    conjunto.remove(elemento) => elimina un elemento del conjunto
"""
# conjunto_1 = {"manzana", "banana", "cereza"}
# e_eliminado =  conjunto_1.remove("cereza")
# print(e_eliminado)
# print("Después de eliminar 'cereza':", conjunto_1)
# e_agregado = conjunto_1.add("naranja")
# e_agregado_2 = conjunto_1.add("mango")
# # print("Después de agregar 'naranja':", conjunto_1)
# print("Después de agregar 'mango':", conjunto_1)
# verduras = {"lechuga", "tomate", "pepino"}


print("\n--- add ---\n")
#7- Usar add() y remove() para modificar un set
u_plataforma.add("joffred")
print("Después de agregar 'joffred' a Plataforma:", u_plataforma)

print("\n--- remove ---\n")
u_plataforma.remove("joffred")
print("Después de eliminar 'joffred' de Plataforma:", u_plataforma)

#8- Recorrer un set con for e imprimir los resultados
print("\n--- Recorrer set de usuarios de Plataforma ---\n")
for usuario in u_plataforma:
    print("Usuario Plataforma:", usuario)