# 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# Esse exercício poderiamos utilizar a bilioteca math para representar o valor exato de PI.

# import math 

raio = int(input("Digite o raio do círculo : "))
area = 3.14*(raio**2)
print(f'A area do círculo é de {area:.2f} mm')

# area2 = math.pi*(raio**2)
# print(f'Ou podemos utilizar pi ao inves de arrendendondar conforme resposta anterior, o resultado seria de {area2}')