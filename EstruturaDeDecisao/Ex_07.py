# 7 - Faça um Programa que leia três números e mostre o maior e o menor deles.
# Assim como no exercício anterior, podemos utilizar o max e o min para resolver, mas novamente não estaria entrando na estrutura de decisão.

num1 = int(input("Digite o primeiro número: "))  
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
maior = menor = 0

# print(f'O maior dos números digitados foi : {max(num1,num2,num3)}')
# print(f'O menor dos números digitados foi : {min(num1,num2,num3)}')


if num1 == num2 == num3:
    print("Os números são todos iguais.")
else:
    ## menor
    if num1 <= num2 and num1 <= num3:
        menor = num1
        print(f'O numéro {menor} foi o menor digitado.')
    elif num2 <= num1 and num2 <= num3:
        menor = num2
        print(f'O numéro {menor} foi o menor digitado.')
    elif num3 <= num2 and num3 <= num1:
        menor = num3
        print(f'O numéro {menor} foi o menor digitado.')

    ## maior
    if num1 > num2 and num1 > num3:
        maior = num1
        print(f'Já o maior número digitado foi {maior}.')
    elif num2 > num1 and num2 > num3:
        maior = num2
        print(f'Já o maior número digitado foi {maior}.')
    else:
        maior = num3
        print(f'Já o maior número digitado foi {maior}.')
