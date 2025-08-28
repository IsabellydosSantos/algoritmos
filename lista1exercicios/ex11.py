# Solicita ao usuário um número inteiro positivo e converte para int
n = int(input("Digite um número inteiro positivo: "))

# Exibe uma mensagem informativa usando f-string (formatação de string)
print(f"Os {n} primeiros números ímpares são:")

# Loop que repete 'n' vezes (de 0 até n-1)
for i in range(n):
    # Fórmula matemática para gerar números ímpares:
    # 2*i + 1 → gera: 1, 3, 5, 7, 9, ...
    numero_impar = 2 * i + 1
    
    # Imprime o número ímpar na mesma linha, separado por espaço
    # end=" " → substitui a quebra de linha padrão por espaço
    print(numero_impar, end=" ")
