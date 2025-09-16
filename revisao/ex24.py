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

contador = 0
for numero in lista1:
    if numero in lista2:
        contador += 1
    print(f"{numero} aparece em ambas listas")

print(f"As listas tem {contador} números em comum")
