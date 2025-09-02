sal = float(input("Insira o valor de seu salário (R$) : "))

if sal < 1000.00:
    print("Não há impostos a pagar")
elif 1000.00 <= sal <= 3000.00:
    calc = sal * 0.2
    print(f"Você deve pagar R${calc} reais de imposto.")
else:
    calcm = sal * 0.35
    print(f"Você deve pagar R${calcm} reais de imposto.")
