entrada = input("Digite números separados por vírgula (ex: 10,5,8,3,15): ")

# Divide a string nas vírgulas, remove espaços e converte para float
numeros_str = entrada.split(',')
numeros = [float(num.strip()) for num in numeros_str if num.strip() != '']

# Verifica se pelo menos um número foi digitado
if len(numeros) == 0:
    print("Erro: Nenhum número foi digitado!")
else:
    # Usa as funções max() e min() para encontrar maior e menor
    maior = max(numeros)
    menor = min(numeros)
    
    # Exibe os resultados
    print(f"\nForam digitados {len(numeros)} número(s):")
    print(f"Números: {numeros}")
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
