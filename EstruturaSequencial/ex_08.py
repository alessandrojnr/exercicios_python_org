# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
ganho_hora = float(input("Quanto você ganha por hora trabalhada ? "))
numero_hora = int(input("Quantas horas você trabalha por mês ? "))
salario = ganho_hora * numero_hora
print(f'Seu salário mensal é de R$ {salario:.2f}')