"""
Uso de listas
objetos = ["manzana", "banana", "cereza"]
"""

numeros =[  1,  2,  3,  4,  5, "hola", "hola", "mundo", [1,2,3], [11,22,33,True, False]]
#Indices => 0   1   2   3   4   5       6        7        8                 9
# como puedo acceder a los elementos dentro de mi lista
# se hace a travez del indice
# print(numeros[0])
# print(numeros[5])
# print(numeros[6] + " " + numeros[7])
# print(f"{numeros[6]} {numeros[7]}")
# print(numeros[8][1])
# print(numeros[9][3])
print(numeros)
for e in numeros:
    # print(e)
    if e == numeros[8]:
        print(e[1])
    if e == numeros[9]:
        print(e[3])
        # for i in e:
        #     print(f"   - {i}")
