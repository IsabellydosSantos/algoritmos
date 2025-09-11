n = int(input("Insira a quantidade de elementos da lista: "))
lista = []
for i in range(n):
  lista.append(int(input(f"Insira números da lista: ")))

x = int(input("Qual o número procurado? "))

if x in lista:
    print(f"O número {x} está na lista")
else:
    print(f"O número {x} não está na lista")