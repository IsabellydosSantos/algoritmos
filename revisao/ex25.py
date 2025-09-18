n = int(input("Insira a quantidade de elementos da lista 1: "))
lista1 = []
for i in range(n):
    num = int(input(f"Digite o {i+1} número da lista 1: "))
    lista1.append(num)

m = int(input("Insira a quantidade de elementos da lista 2: "))
lista2 = []
for i in range(m):
    num = int(input(f"Digite o {i+1} número da lista 2: "))
    lista2.append(num)

lista3 = lista1 + lista2
print(lista3)

lista3.sort()
print(lista3)

lista3.sort(reverse=True)
print(lista3)
