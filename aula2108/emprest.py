idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário mensal: "))
historico_inadimplente = input("Você tem histório de inadimplência? (sim/não): ").strip().lower() #LOWER DEIXA TUDO EM MINUSCULO STRIP remove espacos em branco da resposta
inadim = historico_inadimplente == "sim"

elegivel = (idade >= 18) and (salario >= 2500.00) and not inadim

if elegivel:
    print("Você é elegível para receber o empréstimo.")
else:
    print("Você não é elegível para receber o empréstimo.")