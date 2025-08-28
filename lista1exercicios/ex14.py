entrada = input("Digite três números separados por vírgula (ex: 10,5,8): ")

# Divide a string nas vírgulas e converte cada parte em número float
numeros_str = entrada.split(',')
numeros = [float(num.strip()) for num in numeros_str]

# Verifica se foram digitados exatamente três números
if len(numeros) != 3:
    print("Erro: Você deve digitar exatamente três números!")
    print(f"Você digitou {len(numeros)} número(s).")
else:
    # Usa as funções max() e min() para encontrar maior e menor
    maior = max(numeros)
    menor = min(numeros)
    
    # Exibe os resultados
    print(f"\nEntre os números {numeros[0]}, {numeros[1]} e {numeros[2]}:")
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
