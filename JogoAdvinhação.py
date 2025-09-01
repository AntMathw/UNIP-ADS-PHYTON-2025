import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 5)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação!")
    print("Estou pensando em um número entre 1 e 5.")

    while True:
        chute = input("Qual é o seu chute? ")
        try:
            chute = int(chute)
        except ValueError:
            print("Por favor, digite um número!")
            continue

        if chute < 1 or chute > 5:
            print("O número deve estar entre 1 e 5!")
            continue

        tentativas += 1

        if chute == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif chute < numero_secreto:
            print("Um pouco mais...")
        else:
            print("Um pouco menos...")

    jogar_novamente = input("Quer jogar novamente? (s/n) ")
    if jogar_novamente.lower() == "s":
        jogo_adivinhacao()

jogo_adivinhacao()