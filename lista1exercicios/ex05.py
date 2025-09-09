#faz a conversão de Celsius para Fahrenheit e vice versa

unitemp = str(input("Insira se a temperatura é em Celsius ou Fahrenheit (F ou C): ")).upper()
temp = float(input("Insira a temperatura: "))

if unitemp == "F": #converte a temperatura de Fahrenheit para Celsius 
    convC = (5/9) * (temp-32) #fórmula de conversão 
    roundedC = round(convC, 2) #arredonda o valor final para duas casas decimais após a vírgula 
    print("A temperatura {} F em Celsius é {}° C".format(temp, roundedC))
elif unitemp == "C": #converte a temperatura de Celsius para Fahrenheit
    convF = (temp * 9/5) + 32 #fórmula de conversão
    roundedF = round(convF, 2) #arredonda o valor final para duas casas decimais após a vírgula 
    print("A temperatura {}° C em Fahrenheit é {} F".format(temp, roundedF))

