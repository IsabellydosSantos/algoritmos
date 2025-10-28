n = int(input("Entre com um número inteiro positivo: "))
primo = True
for divisor in range(2, int(n ** 0.5)+1):
    if n % divisor == 0:
        primo = False
        break
if primo:
    print("Primo")
else:
    print("Composto")