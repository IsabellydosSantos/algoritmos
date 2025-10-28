def testa_primo(n):
    primo = True
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            primo = False
            break
    return primo


n = int(input("Entre com um número inteiro positivo: "))

if testa_primo(n):
    print("Primo")
else:
    print("Composto")
