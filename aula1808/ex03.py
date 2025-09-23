n1 = int(input("Informe o primeiro valor inteiro: "))
n2 = int(input("Informe o segundo valor inteiro: "))

if n1 <= 0 or n2 <= 0:
    print("Inválido")
else:  
    if (n1 % 2) == (n2 % 2):
     print("False")  # Mesma paridade
    else:
     print("True")   # Paridades diferentes

