#Comentarios de una línea
'''Comentarios
de
mas
de 
una
linea'''

#Tipos de variables

a = 999999                           #Variable de tipo int
caracter1 = 'a'
caracter2 = "a"
b = "dos"                       #Variable de tipo string
c = 25.00005                        #Variable de tipo float
d = True                        #Variable de tipo booleana veradera
e = False                       #Variable de tipo booleana falsa
f = [a, b, c, d, e, 1, "holi"]  #Variable de tipo lista

#Sentencia Para imprimir
print("hola mundo"+str(int("12")+int(2)))

print(type(1))
print(type(e))
print(type(d))
print(int(d),int(e))
if type(d) == bool:
    print("iguales")
else:
    print("no iguales")

#Imprimir los tipos de variable y su valor
print(type(a),a,"Esta es la a.","hola mundito :"+str(300))
print(type(b),b)
print(type(c),c)
print(type(d),d)
print(type(e),e)
print(type(f),f)

print(21.1 + False)
print(ord("a"))
letra = "z"
if ord(letra) >= 97 and ord(letra) <= 122:
    print("letra minuscula")
else:
    print("LETRA MAYÚSCULA")

z = None
print(type(z))


#Se pueden cambiar los valores de una variable
g = 1
print(type(g), g)
g = 'valor texto'
print(type(g), g)

a = 1
print(a+58)     #Suma
print(a-3)      #Resta
print(a*15)     #Multiplicación
a = 59
print(a/6)     #División
print("Division truncada", a//6)    #División truncada
print("Divison truncada con casteo", int(a/6))
a = 3
b = 2
print(a**b)     #Potencia
print(8%2)      #Modular
a=13
print(a%2==1)

#f = [a, b, c, d, e, 1, "holi"]  #Variable de tipo lista
#Imprimir la liasta de valores y su tipo de valor en cada elemento
print([(x, type(x)) for x in f])