valor_casa = float(input("Informe o valor da casa que deseja comprar (R$): "))
sal = float(input("Informe o valor do seu salário (R$): "))
anos = int(input("Informe a quantidade de anos a pagar: "))

meses = anos * 12
prest = valor_casa / meses
porcent = sal * 0.3

if prest > porcent:
  print("O empréstimo não pode ser aprovado")
else:
  print("O empréstimo foi aprovado")
