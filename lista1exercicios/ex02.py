x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

print(f"Valores originais: x = {x}, y = {y}")

x, y = y, x

print(f"Valores trocados: x = {x}, y = {y}")
