#9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

temp_fahrenheit = int(input("Digite a temperatura que está marcando em Fahrenheit : "))
temp_celsius = 5*((temp_fahrenheit-32)/9)
print(f'A conversão dessa temperatura para graus Celsius é de {int(temp_celsius)}º.')