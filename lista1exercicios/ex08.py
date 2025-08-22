sal = float(input("Insira o valor de seu salário (R$) : "))

if sal < 1000.00:
  print("Não há impostos a pagar")
elif sal >= 1000.00 or sal <= 3000.00:
  calc = sal * 0.2 
  print("Você deve pagar R${} reais de imposto.").format(calc)
else:
  calc = sal * 0.35
  print("Você deve pagar R${} reais de imposto.").format(calc)
