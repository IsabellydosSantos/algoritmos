print("A primeira sequência inserida precisa ser menor que a segunda")
n = input("Insira uma sequência de números inteiros separados por espaço: ")
lista1 = [int(x) for x in n.split()]
m = input("Insira uma sequência de números inteiros separados por espaço: ")
lista2 = [int(x) for x in m.split()]

ln = len(lista1)
lm = len(lista2)
if ln > lm:
    print("A primeira sequência inserida deve ser menor que a segunda")

contador = 0
for i in range(lm - ln + 1):
    if lista2[i:i+ln] == lista1:
        contador += 1

print(f"A primeira sequência ocorre {contador} vezes na segunda sequência")