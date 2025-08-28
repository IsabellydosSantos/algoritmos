from datetime import datetime
print("Primeira data")
data1 = int(input("Insira a primeira data (DD/MM/AAAA): "))

print("Segunda data")
data2 = int(input("Insira a primeira data (DD/MM/AAAA): "))

try:
    data_objeto1 = datetime.strptime(data1, '%d/%m/%Y')
    data_objeto2 = datetime.strptime(data2, '%d/%m/%Y')
except ValueError:
    print("Data inválida inserida")
if data1 < data2:
    print(f"{data1} aconteceu antes de {data2}")
else:
    print(f"{data2} aconteceu antes de {data1}")