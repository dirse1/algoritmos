import random       

print("Jogo Jokenpo!")

opcoes = ["Pedra", "Papel", "Tesoura"]

jogada = str(input("Escolha entre Pedra, Papel ou Tesoura: ").capitalize())
op2 = random.choice(opcoes)

if op2 == jogada:
    print ("Empate")
    
elif op2 == "Papel" and jogada == "Pedra":
    print("Vitória!")
    print(f"{op2} vs {jogada}")
elif op2 == "Papel" and jogada == "Tesoura":
    print("Derrota!")
    print("f{op2} vs {jogada}")
elif op2 == "Pedra" and jogada == "Papel":
    print("Derrota!")
    print(f"{op2} vs {jogada}")
elif op2 == "Pedra" and jogada == "Tesoura":
    print("Vitória!")
    print(f"{op2} vs {jogada}")
elif op2 == "Tesoura" and jogada == "Pedra":
    print("Derrota!")
    print(f"{op2} vs {jogada}")
elif op2 == "Tesoura" and jogada == "Papel":
    print("Vitória!")
    print(f"{op2} vs {jogada}")
