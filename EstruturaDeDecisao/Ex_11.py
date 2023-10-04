# 11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    # salários até R$ 280,00 (incluindo) : aumento de 20%
    # salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    # salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    # salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    # o salário antes do reajuste;
    # o percentual de aumento aplicado;
    # o valor do aumento;
    # o novo salário, após o aumento.

salario = float(input("Digite o salário atual do colaborador : "))
aumento = 0


if salario < 280:
    aumento = 0.2
elif salario < 700:
    aumento = 0.15
elif salario < 1500:
    aumento = 0.1
else:
    aumento = 0.05

novo_salario = (salario*aumento) + salario

print('-'*70)
print("""\t\t--- ORGANIZAÇÕES TABAJARAS ---
      
    Novo aumento de salário para nossos colaboradores :  """)
print(f'''
    - O salário antes do ajuste era de : R$ {salario:.2f}
    - Com um aumento de {aumento*100} %
    - Representando um valor de R$ {salario*aumento:.2f} de acréscimo
    - O novo salário é de R$ {novo_salario:.2f}''')
print('-'*70)
