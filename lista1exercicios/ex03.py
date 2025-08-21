la = float(input("Insira o valor do lado a do triângulo: "))
lb = float(input("Insira o valor do lado b do triângulo: "))
lc = float(input("Insira o valor do lado c do triângulo: "))

if (la==lb and lb==lc):
    print("O triângulo é equilátero")
elif (la!=lb and lb!=lc and la!=lc):
    print("O triângulo é escaleno")
else:
    print("O triângulo é isósceles")

calcarea = (la + lb + lc)/2

print("A área do triângulo é: ", calcarea)