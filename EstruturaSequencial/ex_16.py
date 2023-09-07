# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

'''Esse programa, utilizei a função round para arredondar para cima a quantidade de latas, e para isso utilizei round(numero + 0.5), também utilizei apenas a estrutura sequêncial, conforme solicitado'''

pedido = float(input("Qual e o tamanho em m² que irão ser pintada ? "))
LITRO = 3
LATA = 18
quantidade_litro = pedido / LITRO
quantidade_lata = round(quantidade_litro / LATA + 0.5)
preço_total = quantidade_lata * 80

print(f'Para pintar a quantidade desejada, você irá utilizar {quantidade_litro:.2f} litro(s), sendo assim você precisa de {quantidade_lata} lata(s) de tinta, e o o montante da sua compra é de R$ {preço_total:.2f}')

