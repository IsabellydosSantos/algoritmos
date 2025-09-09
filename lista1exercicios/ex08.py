#calcula o valor do imposto de renda do usuário

sal = float(input("Insira o valor de seu salário mensal (R$) : "))

if sal < 1000.00: #se o salário for menor que mil reais, o usuário nao paga imposto de renda
    print("Não há impostos a pagar")
elif 1000.00 <= sal <= 3000.00: #se for maior ou igual a mil ou menor ou igual a três mil, o usuário paga 20% de imposto 
    calc = sal * 0.2
    print(f"Você deve pagar R${calc} reais de imposto.")
else: #se o salário for maior que três mil, o usuário paga 35% de imposto de renda
    calcm = sal * 0.35
    print(f"Você deve pagar R${calcm} reais de imposto.")

