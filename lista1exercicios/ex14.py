#lê três números e imprime o maior e o menor deles

entrada = input("Digite três números separados por vírgula (ex: 10,5,8): ")

#divide a string nas vírgulas e converte cada parte em número float
numeros_str = entrada.split(',')
numeros = [float(num.strip()) for num in numeros_str]

#verifica se foram digitados exatamente três números
if len(numeros) != 3:
    print("Erro: Você deve digitar exatamente três números")
else:
    #usa as funções max() e min() para encontrar maior e menor
    maior = max(numeros)
    menor = min(numeros)
    
    #exibe os resultados
    print(f"\nEntre os números {numeros[0]}, {numeros[1]} e {numeros[2]}:")
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")

