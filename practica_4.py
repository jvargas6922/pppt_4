"""
Comparador de catálogos de diseño (sets)
Contexto: 🙌
Una agencia de diseño gráfico está integrando productos de dos catálogos distintos. Necesitan identificar
los colores que se repiten, los únicos de cada catálogo y todos los colores disponibles sin duplicados.
Además, desean poder agregar y quitar colores según decisiones del equipo creativo.
Consigna: ✍
Construir un programa que:
● Compare dos listas de colores y elimine duplicados.(listo)
● Informe qué colores están en ambos catálogos.(listo)
● Determine qué colores son exclusivos de cada uno. (listo)
● Permita agregar un nuevo color al catálogo A y eliminar uno del catálogo B.
● Presente todos los resultados de manera clara.
"""

"""
Entrada:
 - crear lista_a y crear_lista_b con colores de ejemplo 
Proceso:
- convertir la lista en un set(para poder sacar los duplicados)
- hacer operaciones de conjuntos para obtener los resultados entre los conjuntos
Salida:
    - mostrar los resultados de las operaciones realizadas
"""

# Creacion de lista de colores
lista_colores_a =["amarillo", "verde", "rojo", "azul", "lila", "cafe", "naranja", "verde", "violeta", "celeste", "blanco"]
lista_colores_b = ["negro", "rosado", "gris", "celeste", "morado", "negro", "burdeo", "naranja"]
print("Listas originales:")
print("Lista de colores A:", lista_colores_a)
print("Lista de colores B:", lista_colores_b)


print("\nProcesando los catálogos de colores...")
# crear conjuntos de colores a partir de las listas
catalogo_colores_a = set(lista_colores_a)
catalogo_colores_b = set(lista_colores_b)
print("Catalogo de colores sin duplicados:")
print("Catalogo colores A:", catalogo_colores_a)
print("Catalogo colores B:", catalogo_colores_b)

print("\nColores comunes en ambos catálogos...")
#Informe qué colores están en ambos catálogos
colores_catalogos_comunes = catalogo_colores_a.intersection(catalogo_colores_b)
print("\nColores comunes en ambos catálogos:", colores_catalogos_comunes)


#Determine qué colores son exclusivos de cada uno.
print("\nColores exclusivos de cada catálogo...")
exclusivo_catalogo_a = catalogo_colores_a.difference(catalogo_colores_b)
exclusivo_catalogo_b = catalogo_colores_b.difference(catalogo_colores_a)
print("\nColores exclusivos del catálogo A:", exclusivo_catalogo_a)
print("Colores exclusivos del catálogo B:", exclusivo_catalogo_b)

#Permita agregar un nuevo color al catálogo A y eliminar uno del catálogo B.
print("\nModificando los catálogos de colores...")
print(f"Catalogo A {catalogo_colores_a}")
nuevo_color = input("Ingrese un nuevo color para agregar al catálogo A: ")
catalogo_colores_a.add(nuevo_color)
print(f"Catalogo (A) Modificado {catalogo_colores_a}")

# Eliminar un color del catálogo B
print(f"Catalogo B {catalogo_colores_b}")
color_a_eliminar = input("Ingrese un color para eliminar del catálogo B: ")
catalogo_colores_b.remove(color_a_eliminar)
print(f"Catalogo (B) Modificado {catalogo_colores_b}")