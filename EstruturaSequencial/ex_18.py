# 18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input("Digite o tamanho do arquivo : "))
velocidade_net = float(input("Qual é a velocidad da sua internet ? "))
download = ((tamanho * 8) / velocidade_net) /60
print(f'Levará cerca de  {download} min o seu download')