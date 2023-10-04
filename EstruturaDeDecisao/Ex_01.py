# 01- Faça um Programa que peça dois números e imprima o maior deles.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 == num2:
    print(F'Os números são iguais.')
elif num1 > num2:
    print(f'O número digitado primeiro {num1} é o maior em relação ao segundo número {num2}')
else:
    print(f'O segundo número {num2} é o maior em relação ao primeiro número {num1}')