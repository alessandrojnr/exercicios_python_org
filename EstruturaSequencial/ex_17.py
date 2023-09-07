# 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#   Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#    - comprar apenas latas de 18 litros;
#    - comprar apenas galões de 3,6 litros;
#    - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math

pedido = float(input("Qual e o tamanho em m² que irão ser pintada ? "))

LITRO = 6
LATAS = 18
GALOES = 3.6
PREÇO_LATA = 80
PREÇO_GALOES = 25

quantidade_litro = pedido/LITRO
quantidade_lata = round(quantidade_litro / LATAS + 0.5 )
quantidade_galoes = round(quantidade_litro / GALOES +0.5)

quantidade_litro_acrescimo = pedido/LITRO * 1.1
mistura_latas = quantidade_litro_acrescimo//LATAS
mistura_galoes = round((quantidade_litro_acrescimo - mistura_latas*LATAS) / GALOES + 0.5)

total_lata = quantidade_lata * PREÇO_LATA
total_galoes = quantidade_galoes * PREÇO_GALOES

print()
print(f'Em latas, serão {quantidade_lata} com o preço de R$ {total_lata:.2f}')
print(f'Em galões, serão {quantidade_galoes} com custo de R$ {total_galoes:.2f}')
print()
print(f'Para evitar desperdício, conforme solcitado. Vamos utilizar nessa venda latas e galões, além de acrescer 10 % de folga .')
print(f'Logo temos {mistura_latas} quantidade de latas + {mistura_galoes} quantidade de galões.\nJá a soma da compra fica hein R$ {(PREÇO_LATA*mistura_latas) + (PREÇO_GALOES*mistura_galoes):.2f}')
