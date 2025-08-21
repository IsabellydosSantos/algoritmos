unitemp = str(input("Insira se a temperatura é em Celsius ou Fahrenheit (F ou C): ")).upper()
temp = float(input("Insira a temperatura: "))

if unitemp == "F":
    convC = (5/9) * (temp-32)
    roundedC = round(convC, 2)
    print("A temperatura {} F em Celsius é {} C".format(temp, convC))
elif unitemp == "C":
    convF = (temp * 9/5) + 32
    roundedF = round(convF,2)
    print("A temperatura {} C em Fahrenheit é {} F".format(temp, convF))
