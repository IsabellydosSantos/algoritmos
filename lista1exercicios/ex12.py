# Solicita ao usuário o número total de elementos da sequência
n = int(input("Digite a quantidade de números: "))

# Inicializa a variável que armazenará a soma dos números pares
soma_pares = 0

print(f"Digite os {n} números:")

# Loop que repete 'n' vezes para receber cada número da sequência
for i in range(n):
    # Lê cada número inteiro da sequência
    numero = int(input(f"Número {i + 1}: "))
    
    # Verifica se o número é par (resto da divisão por 2 é igual a 0)
    if numero % 2 == 0:
        # Se for par, adiciona o número à soma total
        soma_pares += numero

# Exibe o resultado final da soma dos números pares
print(f"A soma dos números pares é: {soma_pares}")
