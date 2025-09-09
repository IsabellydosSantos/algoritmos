#lê a sequência com quantos números o usuário inserir, sem limite, e informa se está em ordem crescente ou não 
entrada = input("Digite números separados por vírgula: ")

#divide a string de entrada em uma lista de strings usando vírgula como separador
numeros_str = entrada.split(',')

#converte cada string da lista em número decimal (float)
numeros = [float(num) for num in numeros_str]

#variável que indica se a sequência está ordenada (inicialmente assumimos que está)
ordenada = True

#percorre a lista comparando cada número com o próximo
#range(len(numeros) - 1) garante que não haverão mais comparações que necessário
#"len" lê a quantidade de números no conjunto (numeros)
for i in range(len(numeros) - 1):
    #se encontrar um número maior que o próximo, a sequência não está ordenada
    if numeros[i] > numeros[i + 1]:
        ordenada = False
        break  #imterrompe o loop antecipadamente

if ordenada:
    print("A sequência está ordenada de forma crescente.")
else:
    print("A sequência não está ordenada de forma crescente.")


