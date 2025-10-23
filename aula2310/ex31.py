n = int(input("Insira um número inteiro: "))
pokedex = {}

for i in range(n):
    print(f"{i+1}° Pokémon: ")

    nome = input("Nome do Pokémon: ")
    tipo = input("Tipo do Pokémon: ")
    ataque = int(input("Força de ataque: "))

    pokedex[nome] = {
        'Nome': nome,
        'Tipo': tipo,
        'Ataque': ataque
    }

poke_fogo = {}
for nome, info in pokedex.items():
    if info['Tipo'].lower() == "fogo":
        poke_fogo[nome] = info['Ataque']

if not poke_fogo:
    print("Não há Pokémons do tipo fogo na lista")

maior_ataque = 0
for info in poke_fogo.values():
    if info['Ataque'] > maior_ataque:
        maior_ataque = info

mais_forte = 0
for info in poke_fogo.values():
    if info['Ataque'] == maior_ataque:
        mais_forte.append(info)

print(pokedex)
print(f"Maior força de ataque entre pokémons tipo fogo: {maior_ataque}")
print(f"Pokémon(s) mais forte(s) tipo fogo: ")

for pokemon in mais_forte:
    print(f"{pokemon['Nome']} (Ataque: {pokemon['Ataque']})")