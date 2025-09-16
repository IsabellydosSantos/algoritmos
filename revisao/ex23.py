n = int(input("Insira a quantidade de elementos da lista: "))
lista = []
for i in range(n):
    num = int(input(f"Digite o {i+1} número da lista: "))
    lista.append(num)

soma = sum(lista)

print("A soma dos elementos da lista é igual a: ", soma)