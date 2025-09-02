entrada = input("Digite números separados por vírgula: ")

# Divide a string de entrada em uma lista de strings usando vírgula como separador
numeros_str = entrada.split(',')

# Converte cada string da lista em número decimal (float)
numeros = [float(num) for num in numeros_str]

# Variável que indica se a sequência está ordenada (inicialmente assumimos que está)
ordenada = True

# Percorre a lista comparando cada número com o próximo
# range(len(numeros) - 1) garante que não haverão mais comparações que necessário
for i in range(len(numeros) - 1):
    # Se encontrar um número maior que o próximo, a sequência não está ordenada
    if numeros[i] > numeros[i + 1]:
        ordenada = False
        break  # Interrompe o loop antecipadamente

if ordenada:
    print("A sequência está ordenada de forma crescente.")
else:
    print("A sequência não está ordenada de forma crescente.")
