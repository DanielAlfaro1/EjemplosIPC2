from Ordenamiento.Lista import Lista

ListaTDANumeros = Lista()
ListaTDANumeros2 = Lista()
ListaNumeros = []

print("Primero ingresemos los números en desorden")

import random
import time

for _ in range(10):
    print(random.random())
    x = int(random.random()*100)
    ListaNumeros.append(x)
    ListaTDANumeros.Insertar(x, "Num"+str(x))
    ListaTDANumeros2.Insertar(x,"Num"+str(x))
    time.sleep(2)

print(ListaNumeros)
print(ListaTDANumeros.Impimir())

print("Primero ordenamos la lista nativa")
for _ in range(len(ListaNumeros)):
    for j in range(len(ListaNumeros)):
        copia = ListaNumeros[j]
        if (j+1 < len(ListaNumeros) and ListaNumeros[j+1] < copia):
            #Ordenamos
            ListaNumeros[j] = ListaNumeros[j+1]
            ListaNumeros[j+1] = copia

print(ListaNumeros)

print("Ordenamos ahora la lista TDA")
ListaTDANumeros.Ordenar1()
print(ListaTDANumeros.Impimir())

print("Ordenamos la otra lista")
ListaTDANumeros2.Ordenar2()
print(ListaTDANumeros2.Impimir())
