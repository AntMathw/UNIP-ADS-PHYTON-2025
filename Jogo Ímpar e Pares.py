import random

def jogar_par_ou_impar():
    """
    Inicia o jogo de Par ou Ímpar. O jogador escolhe par ou ímpar e um número,
    e o computador faz o mesmo. O vencedor é determinado pela soma dos números.
    """
    print("--- Jogo de Par ou Ímpar ---")
    
    # O jogador escolhe par ou ímpar
    escolha_jogador = input("Você escolhe PAR ou ÍMPAR? ").strip().upper()
    while escolha_jogador not in ["PAR", "ÍMPAR"]:
        print("Opção inválida. Por favor, escolha 'PAR' ou 'ÍMPAR'.")
        escolha_jogador = input("Você escolhe PAR ou ÍMPAR? ").strip().upper()

    # O computador escolhe a opção oposta
    if escolha_jogador == "PAR":
        escolha_computador = "ÍMPAR"
    else:
        escolha_computador = "PAR"

    print(f"Você escolheu {escolha_jogador}. O computador escolheu {escolha_computador}.")

    # O jogador e o computador escolhem um número
    try:
        numero_jogador = int(input("Escolha um número (0-5): "))
        if not 0 <= numero_jogador <= 5:
            print("Número inválido. O computador irá escolher um número por você.")
            numero_jogador = random.randint(0, 5)
    except ValueError:
        print("Entrada inválida. O computador irá escolher um número por você.")
        numero_jogador = random.randint(0, 5)

    numero_computador = random.randint(0, 5)

    print(f"Você jogou {numero_jogador}.")
    print(f"O computador jogou {numero_computador}.")

    # Calcula a soma e verifica se é par ou ímpar
    soma = numero_jogador + numero_computador
    print(f"A soma é {soma}.")
    
    if soma % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "ÍMPAR"
    
    print(f"O resultado da soma é {resultado}.")

    # Determina o vencedor
    if resultado == escolha_jogador:
        print("Você venceu! Parabéns!")
    else:
        print("O computador venceu. Tente novamente!")

# Inicia o jogo
jogar_par_ou_impar()
