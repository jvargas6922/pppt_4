""" 
    Acceso y modificacion de datos en un lista.
"""

tareas = ["comprar leche", "enviar correo", "terminar informe"]
# print(tareas[0])
# print(tareas[1])
# print(tareas[2])
""" 
    Modificar un elemento de la lista
    Estructura:
        1- Acceder a la posicion del elemento en mi lista que quiero modificar
        2- Asignar el nuevo valor a esa posicion
    tareas[1] = "enviar Whatsapp"
"""
tareas[1] = "enviar Whatsapp"
# print(tareas[1])
# Uso del append "agregar un elemento a nuestra lista al final"
"""
append estructura:
    1- Nombre de la lista
    2- palabra reservada append
    3- valor a agregar entre parentesis
    tareas.append("valor a agregar")
""" 
tareas.append("pagar cuentas")
# print(tareas)

tareas.append("pasear el perro")
tareas.append("ir al supermercado")
tareas.append("leer un libro")
tareas.append("lavar la ropa")
tareas.append("preparar el almuerzo")
tareas.append("tomar un break")
# print(tareas)
# print(tareas[4])

# uso de insert "agregar un elemento en una posicion especifica"
"""
estrcurtura insert:
    1- Nombre de la lista
    2- palabra reservada insert
    3- posicion donde quiero agregar el nuevo elemento
    tareas.insert(1, "valor a agregar")

"""
tareas.insert(5, "bañarme")
# print(tareas)

# uso del metodo pop "eliminar un elemento de la lista por su posicion"
"""
estructura pop:
    1- Nombre de la lista
    2- palabra reservada pop
    3- posicion del elemento a eliminar entre parentesis
    tareas.pop(2)
"""
# eliminar el elemento de mi lista en la posicion 8
tareas.pop(8)
# print("1---------------------")
# print(tareas)

# uso del metodo remove "eliminar un elemento de la lista por su valor"
"""
estructura remove:
    1- Nombre de la lista
    2- palabra reservada remove
    3- valor del elemento a eliminar entre parentesis
    tareas.remove("valor a eliminar")
"""
tareas.remove("comprar leche")
# print("2---------------------")
# print(tareas) 

"""
    queremos eliminar elementos masivos en una lista
"""
# elemento_a_eliminar = 
# print("3---------------------")

cantidad_elemetos = len(tareas)
print(cantidad_elemetos)
"""
estructura bucle for:
    1- palabra reservada for
    2- variable temporal que almacenara cada elemento de la lista
    3- palabra reservada in
    4- nombre de la lista
    for variable in lista:
        bloque de codigo

        for elemento in tareas:
    print(elemento)
"""
print(tareas)

tareas_seleccionadas = []
for e, j in enumerate(tareas, 1):
    # print(f"{e}. {j}")
    if e > 5:
        # tareas_seleccionadas.append(j)
        # print(j)
        tareas.pop()# 6, 7, 8, 9
        # # tareas.pop(e)
        # # tareas.remove(j)
        # print("------------------------------------------------------")
        # print(f"Eliminacion en vuelta {e} lista actualizada: {tareas}")

print("4---------------------")
print(tareas)
# print(tareas_seleccionadas)

numeros = [1,2,3,4]
for i in range(len(numeros) - 2):
    numeros.pop()
    # print(numeros)

print(numeros)
    
"""
Casuistica:
 tareas [1,2,3,4,5,7,8,9] = 9 iterador = 6
 tareas [1,2,3,4,5,6,8,9] = 8 iterador = 7
 tareas [1,2,3,4,5,6,9] = 7
 tareas [1,2,3,4,5,6] = 6 
 tareas [1,2,3,4,5] = 5

"""
    