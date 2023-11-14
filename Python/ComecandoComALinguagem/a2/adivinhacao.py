print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

while True:
    chute = int(input("Digite o seu numero: "))
    print("Você digitou ", chute)
    if numero_secreto == chute:
        print("Você acertou")
        break
    elif chute > numero_secreto:
        print("Você errou pra mais")
    elif chute < numero_secreto:
        print("Você errou pra menos")
