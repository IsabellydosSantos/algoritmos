n = int(input("Digite um número inteiro positivo: "))

print(f"Os {n} primeiros números ímpares são:")
for i in range(n):
    numero_impar = 2 * i + 1
    print(numero_impar, end=" ")
