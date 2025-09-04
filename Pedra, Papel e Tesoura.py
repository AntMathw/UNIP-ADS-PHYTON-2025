import random

def boas_vindas():
    print("Bem-vindo ao jogo Pedra, Papel ou Tesoura!")
    print("Você vai jogar contra o computador.")
    print("Escolha: Pedra, Papel ou Tesoura\n")

def obter_escolha_jogador():
    escolha = input("Sua escolha: ").strip().lower()
    while escolha not in ["pedra", "papel", "tesoura"]:
        print("Escolha inválida. Tente novamente.")
        escolha = input("Escolha entre Pedra, Papel ou Tesoura: ").strip().lower()
    return escolha

def gerar_escolha_computador():
    return random.choice(["pedra", "papel", "tesoura"])

def determinar_vencedor(jogador, computador):
    print(f"\nVocê escolheu: {jogador}")
    print(f"O computador escolheu: {computador}\n")

    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Você venceu!")
    else:
        print("Você perdeu!")

def jogar():
    boas_vindas()
    jogador = obter_escolha_jogador()
    computador = gerar_escolha_computador()
    determinar_vencedor(jogador, computador)

# Início do jogo
jogar()
