import random

print("Jogo: Adivinhe o Numero!")

numero = random.randint(1, 10)
escolha = int(input("Escolha um número de 1 a 10: "))

if numero == escolha:
    print (f"Você acertou, o {numero} foi o escolhido")    
else:
    print (f"Você errou, o {numero} era o escolhido")
                