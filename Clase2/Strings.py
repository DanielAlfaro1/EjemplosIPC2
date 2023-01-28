#Acceso por medio de índice en string
Fruta = 'manzana' #Fruta = ['m', 'a', 'n', 'z'...]
letra = Fruta[5]
print(letra)

print("El While")
#Uso de iteración con string
indice = 0
while indice < len(Fruta):
    letra = Fruta[indice]
    print(letra)
    indice = indice + 1 # indice++ | indice += 1

print("El for")
for i in range(len(Fruta)):
    print(Fruta[i])

#Impresión segmentada
Frase = 'Monty Python'
print(Frase[0:5])
#Salida: Monty
print(Frase[3:12])
#Salida: Python
print(Frase[3:])
#Salida: ty Python
print(Frase[:4])
#Salida: Mont

Pokemons = [137, 88, 95, 77, 153, 140]
#los primeros 3 números son nuestros pokemons
#los últimos 3 números son los pokemons del rival
Pokemons[1] = 99
MisPokemons = Pokemons[:3]
PokemonsRival = Pokemons[3:]

print('Mis Pokemons:')
for i in range(len(MisPokemons)):
    print('\t',MisPokemons[i])

print('Pokemons del Rival')
for i in range(len(PokemonsRival)):
    print('\t', PokemonsRival[i])

MiFavorito = "Ponyta"
#MiFavorito[2] = 'x' NO SE PUEDE HACER