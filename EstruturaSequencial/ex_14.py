# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
peso = float(input("Bom dia João, qual foi o quilo do peixe pescado hoje ? "))
excesso = peso -50
multa = excesso * 4
print(f'O peixe tem um peso de {peso}, já o excesso de quilos foram {excesso} por isso o valor da multa é de  {multa}')


'''Utilizando estruturas condicionais, o programa irá ficar mais adequado, evitando erros (como por exemplo em caso de numeros menores de 50 em relação ao peso), porém esses exercício é para estruturas sequenciais. Acredito que a resposta acima é mais adequada para ocasião.

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'O peixe tem um peso de {peso}, já o excesso de quilos foram de {excesso} kgs e o valor da multa a ser paga será de R$ {multa:.2f}')
else:
    print(f'Seu peixe não tem cobrança extra João, tenha um bom dia.')'''
