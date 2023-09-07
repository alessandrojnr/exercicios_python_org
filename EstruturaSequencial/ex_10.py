# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = (C *9/5)+32

temp_celsius = int(input("Digite a temperatura em graus Celsius : "))
temp_fahrenheit = (temp_celsius*9/5)+32
print(f'A temperatura convertida em graus Celsius para Fahreinheit é de {int(temp_fahrenheit)} Fº')