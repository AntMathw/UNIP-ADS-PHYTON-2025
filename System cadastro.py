#MATERIAL DE ESTUDOS EM FASE DE DESENVOLVIMENTO...

import time
import sys

def main():
    # --- Cabeçalho Visual ---
    # Usa multiplicação de strings para criar linhas decorativas
    print('-=-' * 15)
    print('CADASTRO DE USUÁRIO')
    print('-=-' * 15)
    time.sleep(1) # Pausa a execução por 1 segundo para melhorar a leitura

    print('Olá usuário, então vamos começar o seu cadastro!')
    print('=-=' * 15)
    time.sleep(1)

    print('Primeiramente gostaria de saber seu nome e sobrenome!')
    print('=-=' * 15)
    time.sleep(1)

    # --- Validação do Primeiro Nome ---
    # O while True cria um loop infinito que só para (break) quando o dado é válido
    while True:
        nome = input('Digite seu primeiro nome: ')
        # .strip() remove espaços em branco acidentais antes e depois do texto
        if not nome.strip():
            print('Nome inválido, o campo não pode ficar vazio!')
        else:
            # .capitalize() garante que a primeira letra seja maiúscula e o resto minúscula
            n2 = nome.strip().capitalize()
            break 

    # --- Entrada do Sobrenome ---
    sobrenome = input('Digite seu sobrenome: ')
    s2 = sobrenome.strip().capitalize()

    time.sleep(1)
    print('Certo! Agora gostaria de saber sua idade e seu CPF')

    # --- Tratamento de Erros na Idade ---
    while True:
        try:
            idade_input = input('Digite sua idade: ')
            # Tenta converter o texto para número inteiro (int)
            idade = int(idade_input)
            break
        except ValueError:
            # Se a conversão falhar (ex: digitar letras), o código não trava e mostra esta mensagem
            print("Idade inválida. Por favor, digite um número.")

    # --- Entrada de CPF ---
    cpf = input('Digite seu CPF (apenas números): ')

    print('Carregando cadastro...')
    time.sleep(2)
    print('-' * 30)
    # f-strings permitem inserir variáveis diretamente dentro do texto entre chaves {}
    print(f'Seu nome é {n2} {s2}')
    print(f'Atualmente possui {idade} anos')
    print(f'Portador do CPF {cpf}')
    print('-' * 30)

    # --- Verificação de CNH ---
    # .upper() transforma a resposta em maiúscula para aceitar tanto 's' quanto 'S'
    cnh = input('O usuário possui CNH (Carteira Nacional de Habilitação)? [S/N]: ').strip().upper()

    if cnh == 'S':
        print('Você possui CNH, e o código registrado é 786546884')
    elif cnh == 'N':
        print('Você não possui CNH')
    else:
        # Caso o usuário digite qualquer coisa diferente de S ou N
        print('Opção inválida (Considerado como N).')

    print('-' * 30)
    print('SEU CADASTRO ESTÁ SENDO PROCESSADO AGUARDE...')
    time.sleep(2)
    print('INFORMAÇÕES CORRETAS!')
    time.sleep(1)

    # --- Opção de Continuidade ou Saída ---
    while True:
        continuar = input('GOSTARIA DE CONTINUAR O CADASTRO? [S/N] ').strip().upper()

        # Verifica se a entrada está na lista de opções negativas
        if continuar in ['N', 'NAO', 'NÃO']:
            print('CADASTRO CANCELADO PELO USUÁRIO!!!')
            sys.exit() # Encerra o programa imediatamente
        # Se for S, Sim ou vazio (apenas Enter), o loop quebra e o programa segue
        elif continuar in ['S', 'SIM', '']:
            print('CERTO! ENTÃO CONTINUAREMOS SEU CADASTRO')
            break 
        else:
            print('Opção inválida! Digite S para Sim ou N para Não.')

    print('-~-' * 30)
    print('Agora iniciaremos o cadastro em nosso sistema! ')
    print('-~-' * 30)

    # --- Validação de E-mail com Lógica de Pertencimento ---
    while True:
        verificacao = input('Digite seu email pessoal: ')
        
        if not verificacao.strip():
            print('Email inválido o campo está vazio')
            continue # Volta para o início do loop atual
        elif '@' not in verificacao:
            # Verifica se o caractere especial @ existe na string digitada
            print('Email inválido, faltando o caractere "@"')
            continue
        
        # .lower() garante que o email fique todo em minúsculas (padrão de sistemas)
        ver = verificacao.strip().lower()
        confirmar = input(f'Seu email é {ver} está correto? S/N: ').strip().upper()
        
        if confirmar in ['S', 'SIM']:
             print('Enviaremos um código de verificação para o seu email')
             break
        else:
             print('Preencha o campo novamente')
             continue

    print("\n--- CADASTRO FINALIZADO COM SUCESSO ---")

# Boilerplate padrão do Python para garantir que a função main() só rode se o script for executado diretamente
if __name__ == "__main__":
    main()
