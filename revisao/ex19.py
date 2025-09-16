n = int(input("Insira um número inteiro positivo: "))
resultado = 0
for num in range(1,n+1):
    if num % 2 == 0:
      print(f"+{num}")
      resultado += num
    else:
      print(f"-{num}")
      resultado -= num

print("Resultado Final: ", resultado)