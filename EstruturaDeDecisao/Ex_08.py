# 8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato
    ## Assim como nos exercícios anteriores, poderia ser realizado utilizando o método min(). Vou deixar o exemplo comentado.

preco1 = float(input("Digite o valor do primeiro produto: "))  
preco2 = float(input("Digite o valor do segundo produto: "))
preco3 = float(input("Digite o valor do terceiro produto: "))
menor_preco = 0


# print(f'O produto sugerido é : {min(preco1,preco2,preco3)}')


if preco1 == preco2 == preco3:
    print("Os preço são todos iguais, compre o produto que mais gostou.")
else:

    if preco1 <= preco2 and preco1 <= preco3:
        menor_preco = preco1
        print(f'O primeiro produto é a melhor opção com o custo de R$ {menor_preco:.2f}.')
    elif preco2 <= preco1 and preco2 <= preco3:
        menor_preco = preco2
        print(f'O segundo produto é a melhor opção com o custo de R$ {menor_preco:.2f}.')
    elif preco3 <= preco2 and preco3 <= preco1:
        menor_preco = preco3
        print(f'O terceiro produto é a melhor opção com o custo de R$ {menor_preco:.2f}.')