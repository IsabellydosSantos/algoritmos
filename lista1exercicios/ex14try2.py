#lê quantos números o usuário inserir, sem limites, e imprime o maior e o menor deles

entrada = input("Digite números separados por vírgula (ex: 10,5,8,3,15): ")

#divide a string nas vírgulas, remove espaços e converte para float
numeros_str = entrada.split(',')
numeros = [float(num.strip()) for num in numeros_str if num.strip() != '']

#verifica se pelo menos um número foi digitado
if len(numeros) == 0:
    print("Erro: Nenhum número foi digitado!")
else:
    #usa as funções max() e min() para encontrar maior e menor
    maior = max(numeros)
    menor = min(numeros)
    
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
