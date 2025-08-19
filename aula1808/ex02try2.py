hora_inicial = 14  
horas_adicionais = 51
hora_final = (hora_inicial + horas_adicionais) % 24

print(f"O alarme irá tocar às {hora_final}:00 horas")
