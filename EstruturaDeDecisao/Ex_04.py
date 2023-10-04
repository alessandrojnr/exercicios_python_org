# 4- Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma letra: ")).lower().strip()
if letra in "aeiou":
    print("Você digitou uma vogal")

elif letra in "qwrtypsdfghjklçzxcvbnm":
    print("Você digitou uma consoante")

else:
    print("Você não digitou nem vogal nem consoante.")