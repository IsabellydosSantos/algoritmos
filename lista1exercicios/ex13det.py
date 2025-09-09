# Recebe um número e o converte para sua base binária mostrando o passo a passo

print("=== CONVERSOR DECIMAL PARA BINÁRIO ===")

# Passo 1: Pedir o número decimal
numero_decimal = int(input("Digite um número inteiro: "))
original = numero_decimal  # Guardamos uma cópia para mostrar depois

# Passo 2: Explicar o processo
print(f"\nVamos converter {original} para binário!")
print("Método: Divisões sucessivas por 2")
print("Cada resto será um dígito binário")
print("-" * 40)

# Passo 3: Mostrar cada divisão
restos = []  # Lista para guardar os restos (dígitos binários)

contador = 1
while numero_decimal > 0:
    # Mostra a divisão atual
    print(f"Passo {contador}:")
    print(f"{numero_decimal} ÷ 2 = {numero_decimal // 2} resto {numero_decimal % 2}")
    
    # Calcula resto e quociente
    resto = numero_decimal % 2
    numero_decimal = numero_decimal // 2
    
    # Guarda o resto (dígito binário)
    restos.append(resto)
    print(f"Dígito binário: {resto}")
    print("-" * 20)
    contador += 1

# Passo 4: Explicar que precisamos inverter os restos
print("\nAgora vamos ler os restos de baixo para cima:")
print("Restos coletados:", restos)
print("Invertendo a ordem: ")

# Inverte a lista de restos
binario_invertido = restos[::-1]
print("Ordem correta:", binario_invertido)

# Passo 5: Juntar todos os dígitos
numero_binario = ''.join(str(digito) for digito in binario_invertido)

# Passo 6: Mostrar o resultado final
print("\n" + "=" * 50)
print(f"RESULTADO FINAL:")
print(f"Decimal: {original}")
print(f"Binário: {numero_binario}")
print("=" * 50)

# Caso especial para número 0
if original == 0:
    print("O número 0 em binário é: 0")
