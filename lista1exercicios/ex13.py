#recebe um número e o converte em sua base binária 

numero_decimal = int(input("Digite um número inteiro decimal: "))

#armazena o número original para exibição posterior
numero_original = numero_decimal

#se o número for 0, seu binário é 0
if numero_decimal == 0:
    print(f"O número 0 em binário é: 0")
else:
    #lista para armazenar os dígitos binários (restos das divisões)
    digitos_binarios = []
    
    #converte o número decimal para binário usando divisões sucessivas por 2
    while numero_decimal > 0:
        #calcula o resto da divisão por 2 (0 ou 1)
        resto = numero_decimal % 2
        #adiciona o resto à lista de dígitos binários
        digitos_binarios.append(str(resto))
        #divide o número por 2 (divisão inteira)
        numero_decimal = numero_decimal // 2
    
    #inverte a lista porque os restos foram coletados do último para o primeiro
    numero_binario = ''.join(digitos_binarios[::-1])
    
    print(f"O número {numero_original} em binário é: {numero_binario}")

