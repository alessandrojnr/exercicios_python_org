# 6 - Faça um Programa que leia três números e mostre o maior deles.
# Poderiamos utilizar um método MAX(), mas não estariamos utilizando a estrutura de decisão, o exemplo com MAX vai estar comentado dentro do exercício.

num1 = int(input("Digite o primeiro número: "))  
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
maior = 0

# print(f'O maior dos números digitados foi : {max(num1,num2,num3)}')
if num1 == num2 == num3:
    print("Os números são todos iguais.")

elif num1 > num2 and num1 > num3:
    maior = num1
    print(f'O maior número foi {maior}')
elif num2 > num1 and num2 > num3:
    maior = num2
    print(f'O maior número foi {maior}')
else:
    maior = num3
    print(f'O maior número foi {maior}')


