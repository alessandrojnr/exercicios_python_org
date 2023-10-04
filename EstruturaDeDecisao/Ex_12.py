# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    # Desconto do IR:
    # Salário Bruto até 900 (inclusive) - isento
    # Salário Bruto até 1500 (inclusive) - desconto de 5%
    # Salário Bruto até 2500 (inclusive) - desconto de 10%
    # Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
horas_trabalhada = int(input("Quantidade de horas trabalhadas no mês : "))
valor_hora = float(input("Qual o valor hora trabalhada : "))

salario_bruto = horas_trabalhada *valor_hora
ir = descontos = salario_liquido = 0
sindicato = 0.03
inss = 0.1
fgts = 0.11

if salario_bruto < 900:
    ir = 0
elif salario_bruto < 1500:
    ir = 0.05
elif salario_bruto < 2500:
    ir = 0.1
else:
    ir = 0.2

sindicato = salario_bruto * sindicato
inss = salario_bruto * inss
imposto = salario_bruto * ir
fgts = salario_bruto * fgts
descontos = sindicato + inss + imposto
salario_liquido = salario_bruto - descontos

print(f"""
\t\t - Salário Bruto : ({horas_trabalhada} * {valor_hora}) \t\t : R$ {salario_bruto:.2f} 
\t\t (-) IR ({ir*100} %) \t\t\t : R$ {imposto:.2f} 
\t\t (-) INSS ( 10 %) \t\t\t : R$ {inss:.2f}
\t\t FGTS (11 %)    \t\t\t : R$ {fgts:.2f}
\t\t Total de descontos \t\t\t : R$ {descontos:.2f}
\t\t Salário Líquido \t\t\t : R$ {salario_liquido:.2f}""")