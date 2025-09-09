# Calcula o mdc dos números m e n

print("=== CALCULADORA DE MDC (Máximo Divisor Comum) ===")

# Passo 1: Pedir os dois números
print("\nDigite dois números para calcular o MDC:")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

# Fazemos cópias para mostrar o processo
a = num1
b = num2

# Troca automática se necessário (sempre a >= b)
if a < b:
    a, b = b, a  # Troca os valores

print(f"\nCalculando MDC({a}, {b})...")
print("Usando o Algoritmo de Euclides:")
print("-" * 40)

# Passo 2: Mostrar o processo passo a passo
passo = 1
while b != 0:
    print(f"Passo {passo}:")
    print(f"MDC({a}, {b})")
    
    # Calcula o resto da divisão
    resto = a % b
    print(f"{a} ÷ {b} = {a // b} com resto {resto}")
    
    # Prepara para o próximo passo
    a, b = b, resto
    
    if b != 0:  # Só mostra se não for o último passo
        print(f"Próximo: MDC({a}, {b})")
    print("-" * 20)
    passo += 1

# Passo 3: Mostrar o resultado
print(f"Resultado final: ")
print(f"MDC({num1}, {num2}) = {a}")

