#lê dois valores inteiros x e y e troca os valores
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

print(f"Valores originais: x = {x}, y = {y}")

#troca os valores
#exemplo: x=2 e y=10
#depois da troca: x=10 e y=2
x, y = y, x

print(f"Valores trocados: x = {x}, y = {y}")

