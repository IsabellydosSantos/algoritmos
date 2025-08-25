# Lê a sequência de 5 números separados por vírgula
entrada = input("Digite 5 números separados por vírgula: ")

# Converte a string em uma lista de números
numeros_str = entrada.split(',')
numeros = [float(num) for num in numeros_str]

# Verifica se a sequência está em ordem crescente
ordenada = True
for i in range(len(numeros) - 1):
    if numeros[i] > numeros[i + 1]:
        ordenada = False
        break

# Exibe o resultado
if ordenada:
    print("A sequência está ordenada de forma crescente.")
else:
    print("A sequência NÃO está ordenada de forma crescente.")
