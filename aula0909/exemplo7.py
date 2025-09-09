n = int(input("Quantos números serão lidos? "))
lista = [ ]
for i in range(n):
    lista.append(int(input()))
x = int(input("Qual o número que deve ser removido? "))
while x in lista:
    lista.remove(x)
print(lista)