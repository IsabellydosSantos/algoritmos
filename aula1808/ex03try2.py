n1 = int(input("Informe um valor inteiro: "))
n2 = int(input("Informe um valor inteiro: "))

ok1 = (n1%2==1) and (n2%2==0)
ok2 = (n1%2==0) and (n2%2==1)
ok = (ok1 or ok2)
print(ok)