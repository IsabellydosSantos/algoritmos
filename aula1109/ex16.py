lista = input("Insira uma lista de números inteiros separados por vírgula: ")
num = [int(x) for x in lista.split(',')]

i = 0
while i < len(num):
    if num[i] % 2 == 0:
        num.pop(i)
    else:
        i += 1

print("Lista sem números pares: ", num)