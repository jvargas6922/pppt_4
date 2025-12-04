"""
¿En qué consistirá la Demo?
Crearemos una pequeña aplicación de consola que permita gestionar una lista de tareas. Aplicaremos
operaciones básicas de listas como agregar, eliminar e iterar.
1- Crear una lista inicial con tareas (lista)
2- Mostrar todas las tareas actuales (lista)
3- Agregar una nueva tarea a la lista (lista)
4- Marcar una tarea como completada (eliminarla) (lista)
5- Recorrer e imprimir la lista de tareas con un for (lista)
6- Usar pop() para eliminar tareas por índice (lista)
7- Validar si la lista está vacía (lista)
8- Mostrar mensaje de cierre: "¡Todas las tareas completadas!" (lista)
"""
#1
tareas = ["caminar", "bañarnos", "comer"]
#2
print(f"Tareas {tareas}" )
#3
nueva_tarea = input("Ingrese una nueva tarea: ")
tareas.append(nueva_tarea)
print(f"Tareas actualizadas: {tareas}")
#4
tareas.pop()
print(f"Tareas actualizadas: {tareas}")
#5
for tarea in tareas:
    print(f"- {tarea}")
#6
for i in range(1, len(tareas)+1):
    eliminar_tarea = int(input(f"Ingrese el índice (1-{len(tareas)}) de la tarea a eliminar: "))
    tareas.pop(eliminar_tarea - 1)
    if len(tareas) == 0:
        print("¡Todas las tareas completadas!")
        break

    




