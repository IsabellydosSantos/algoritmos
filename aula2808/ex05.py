import math
cateto1 = float(input("Digite um valor para o cateto a: "))
cateto2 = float(input("Digite um valor para o cateto b: "))
hipotenusa = math.sqrt(cateto1*cateto1 + cateto2*cateto2)
print(f"Os catetos s~ao {cateto1} e {cateto2}!")
print(f"A hipotenusa ´e {hipotenusa:0.2f}.")