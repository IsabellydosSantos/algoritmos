n = int(input("Insira um número inteiro positivo: "))

soma1 = sum(i**2 for i in range(1, n+1))
soma2 = sum(i**3 for i in range(1, n+1))
soma3 = sum(i**4 for i in range(1, n+1))
resultado = 2*soma1 + 3*soma2 + 4*soma3

print("O resultado da soma é igual a: ", resultado)
