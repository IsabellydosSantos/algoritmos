n = int(input("Digite um número inteiro positivo: "))

print(f"Os {n} primeiros números ímpares são:")

# Loop que repete 'n' vezes (de 0 até n-1)
for i in range(n):
    # Fórmula matemática para gerar números ímpares:
    numero_impar = 2 * i + 1
    
    # Imprime o número ímpar na mesma linha, separado por espaço
    # end=" " → substitui a quebra de linha padrão por espaço
    print(numero_impar, end=" ")
