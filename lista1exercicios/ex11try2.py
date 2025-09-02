n = int(input("Digite um número inteiro positivo: "))

# Mostra até qual número será a busca por ímpares
print(f"Números ímpares até {n}:")

# Loop que percorre os números de 1 até n, pulando de 2 em 2
# range(início, fim, passo) → gera: 1, 3, 5, 7, ... até n ou o último ímpar antes de n
for i in range(1, n + 1, 2):
    # Imprime cada número ímpar na mesma linha, separado por espaço
    # end=" " → substitui a quebra de linha padrão por espaço
    print(i, end=" ")
