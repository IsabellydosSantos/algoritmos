n = int(input("Digite um número inteiro positivo: "))

print(f"Números ímpares até {n}:")
# Começa no 1 e vai pulando de 2 em 2
for i in range(1, n + 1, 2):
    print(i, end=" ")
