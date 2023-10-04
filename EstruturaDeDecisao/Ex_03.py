# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = str(input("Digite F para feminino , ou M para masculino : ")).upper().strip()

if letra == "F":
    print("Você digitou F para feminino.")
elif letra == "M":
    print("Você digitou M para masculino.")
else:
    print("Sexo inválido.")