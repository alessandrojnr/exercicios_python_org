# 2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input('Digite um número : '))

if num == 0:
    print('Zero é considerado um número NEUTRO.')
elif num < 0:
    print("O número digitado é negativo.")
else:
    print("O número digitado é positivo.")