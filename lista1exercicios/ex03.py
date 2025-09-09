#lê o valor dos três lados de um triângulo, classifica o tipo e calcula a área 

#coleta os valores dos lados do triângulo 
la = float(input("Insira o valor do lado a do triângulo: "))
lb = float(input("Insira o valor do lado b do triângulo: "))
lc = float(input("Insira o valor do lado c do triângulo: "))

#classsifica o tipo do triângulo de acordo com seus lados
if (la==lb and lb==lc): #se todos os lados forem iguais
    print("O triângulo é equilátero")
elif (la!=lb and lb!=lc and la!=lc): #se todos os lados forem diferentes
    print("O triângulo é escaleno")
else: #se não tem todos os lados iguais e nem todos os lados diferentes
    print("O triângulo é isósceles")

#Calcula a área
calcarea = (la + lb + lc)/2


print("A área do triângulo é: ", calcarea)
