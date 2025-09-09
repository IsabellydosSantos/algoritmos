#recebe um número n, depois lê uma sequência de n números e informa se está em ordem crescente ou não 

n = int(input("Digite um número inteiro: ")) 
entrada = input(f"Digite {n} números separados por vírgula: ")

#divide a string de entrada em uma lista de strings usando vírgula como separador
numeros_str = entrada.split(',')

if len(numeros_str) != n: #indica erro se o usuário digitar mais números que o estipulado
    print(f"Erro: Você deve digitar exatamente {n} números")
else:
    try: 
#converte cada string da lista em número decimal (float)
numeros = [float(num) for num in numeros_str]

#variável que indica se a sequência está ordenada (inicialmente assumimos que está)
ordenada = True

#percorre a lista comparando cada número com o próximo
#range(len(numeros) - 1) garante que não haverão mais comparações que o necessário
#"len" lê a quantidade de números no conjunto (numeros)
for i in range(len(numeros) - 1):
    #se encontrar um número maior que o próximo, a sequência não está ordenada
    if numeros[i] > numeros[i + 1]:
        ordenada = False
        break  # Interrompe o loop antecipadamente

if ordenada:
    print("A sequência está ordenada de forma crescente.")
else:
    print("A sequência não está ordenada de forma crescente.")

except ValueError: #indica erro se o usuário digitar algo que não seja um número 
        print("Erro: Certifique-se de digitar apenas números válidos")
