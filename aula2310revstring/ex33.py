data = input("Digite uma data no formato dd/mm/aaaa: ").split('/')

if len(data) != 3:
    print("Formato inválido. Use dd/mm/aaaa")
else:
    try:
        dia, mes, ano = map(int, data)
        
        meses = {
            1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
            5: "maio", 6: "junho", 7: "julho", 8: "agosto",
            9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
        }
        
        if mes not in meses:
            print("Mês inválido. Digite um valor entre 1 e 12.")
        elif dia < 1 or dia > 31:
            print("Dia inválido. Digite um valor entre 1 e 31.")
        else:
            mes_extenso = meses[mes]
            data_convertida = f"{dia} de {mes_extenso} de {ano}"
            print(f"Data convertida: {data_convertida}")
            
    except ValueError:
        print("Inválido. Certifique-se de digitar números válidos.")
