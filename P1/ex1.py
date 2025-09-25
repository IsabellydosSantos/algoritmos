n = int(input("Insira um número inteiro positivo: "))

soma = 0
for i in range(1,n+1):
  soma += i / (n-i+1)

print("O resultado da soma é: ", soma)