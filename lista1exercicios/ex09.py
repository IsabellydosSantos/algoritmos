#faz a aprovação ou desaprovação de empréstimos

valor_casa = float(input("Informe o valor da casa que deseja comprar (R$): "))
sal = float(input("Informe o valor do seu salário (R$): "))
anos = int(input("Informe a quantidade de anos a pagar: "))

meses = anos * 12 #converte anos em meses
prest = valor_casa / meses #o valor da prestação é calculado dividindo o valor da casa pelos meses a pagar
porcent = sal * 0.3 #calcula 30% do salário 

if prest > porcent: #se o valor das prestação for maior que 30% do salário
  print("O empréstimo não pode ser aprovado")
else:
  print("O empréstimo foi aprovado")

