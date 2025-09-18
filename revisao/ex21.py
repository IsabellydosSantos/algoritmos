n = int(input("Insira o tamanho dos catetos: "))
c = input("Entre com o caractere a se usado: ")

for i in range(1,n+1):
    print(" " * (n-1) + c * (2*i - 1))
