# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num_1 = int(input('Digite um número inteiro: '))
num_2 = int(input("Digite outro número inteiro: "))
num_real = float(input("Digite um número real: "))

total_1 = (num_1*2) * (num_2/2)
print(f"O produto do dobro do primeiro com a metade do segundo é : {total_1} ")

total_2 = (num_1*3) + num_real
print(f'A soma do triplo do primeiro com o terceiro é de : {total_2}')

total_3 = num_real**3
print(f'A o terceiro elevado ao cubo é {total_3}')
