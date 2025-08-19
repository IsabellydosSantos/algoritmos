n1 = int(input("Informe um valor inteiro: "))
res = n1 % 2
if (res > 0):
    n1 = "impar"
    print("impar")
else:
    n1 = "par"
    print("par")

'n2 = int(input("Informe um valor inteiro: "))'
res2 = n2 % 2
if (res2 > 0):
    n2 = "impar"
    print("impar")
else:
    n2 = "par"
    print("par")

if (n1 and n2 == "impar"):
    print("False")

elif (n1 and n2 == "par"):
    print("False")

else:
    print("True")



