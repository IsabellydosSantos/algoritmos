sexo = input("Insira se seu sexo é feminino ou masculino (F ou M): ").upper()
alt = float(input("Insira sua altura em metros (ex. 1.65): "))
peso = float(input("Insira seu peso atual em quilogramas (ex. 55.1): "))

if sexo == "F":
    calc = 62.1 * alt - 44.7
    print(f"Seu peso ideal é de: {calc:.2f}")
    if peso > calc:
        print("Você está acima do peso ideal")
    elif peso == calc:
        print("Você está no peso ideal")
    else:
        print("Você está abaixo do peso ideal")
elif sexo == "M":
    calc = 72.7 * alt - 58
    print(f"Seu peso ideal é de: {calc:.2f}")
    if peso > calc:
        print("Você está acima do peso ideal")
    elif peso == calc:
        print("Você está no peso ideal")
    else:
        print("Você está abaixo do peso ideal")