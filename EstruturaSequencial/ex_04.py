# 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota_1 = float(input("Por favor, digite a nota do primeiro bimestre : "))
nota_2 = float(input("Por favor, digite a nota do segundo bimestre : "))
nota_3 = float(input("Por favor, digite a nota do terceiro bimeste : "))
nota_4 = float(input("Por favor, digite a nota do quarto bimestre : "))
media = (nota_1 + nota_2 + nota_3 + nota_4)/4
print(f'A média do aluno foi de {media:.2f} durante o ano')
