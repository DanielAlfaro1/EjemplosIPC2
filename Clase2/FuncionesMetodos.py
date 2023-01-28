#Funciones nativas
lista = [1, 2, 3, 4, 5]
lista.append(1)
print(len(lista))

import random

print("que es random?",random.random())
for i in range(10):
    x = random.random()
    print(x)

#Creación de método (no retorno)
def No_Repito(numero):
    print('Yo no repito dos veces')
    if (int(numero) % 2 == 0) :
        print('Que dijo?')
        print('No repito 2 veces')

No_Repito(int(random.random()*10))

#Creación de función con retorno
def Suma_De_Tres(num1, num2, num3):
    if num1 > 2:
        return str(num1 + num2 + num3)
    elif num2 == 3 :
        return 10
    else:
        return True
    
    

print(Suma_De_Tres(1,2,3), type(Suma_De_Tres(1,2,3)))