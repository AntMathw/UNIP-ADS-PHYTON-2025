import time
import sys

def main():
    print('-=-' * 15)
    print('CADASTRO DE USUÁRIO')
    print('-=-' * 15)
    time.sleep(1) 

    print('Olá usuário, então vamos começar o seu cadastro!')
    print('=-=' * 15)
    time.sleep(1)

    print('Primeiramente gostaria de saber seu nome e sobrenome!')
    print('=-=' * 15)
    time.sleep(1)

    while True:
        nome = input('Digite seu primeiro nome: ')
        if not nome.strip():
            print('Nome inválido, o campo não pode ficar vazio!')
        else:
            n2 = nome.strip().capitalize()
            break 

    sobrenome = input('Digite seu sobrenome: ')
    s2 = sobrenome.strip().capitalize()

    time.sleep(1)
    print('Certo! Agora gostaria de saber sua idade e seu CPF')

    while True:
        try:
            idade_input = input('Digite sua idade: ')
            idade = int(idade_input)
            break
        except ValueError:
            print("Idade inválida. Por favor, digite um número.")

    cpf = input('Digite seu CPF (apenas números): ')

    print('Carregando cadastro...')
    time.sleep(2)
    print('-' * 30)
    print(f'Seu nome é {n2} {s2}')
    print(f'Atualmente possui {idade} anos')
    print(f'Portador do CPF {cpf}')
    print('-' * 30)

    cnh = input('O usuário possui CNH (Carteira Nacional de Habilitação)? [S/N]: ').strip().upper()

    if cnh == 'S':
        print('Você possui CNH, e o código registrado é 786546884')
    elif cnh == 'N':
        print('Você não possui CNH')
    else:
        print('Opção inválida (Considerado como N).')

    print('-' * 30)
    print('SEU CADASTRO ESTÁ SENDO PROCESSADO AGUARDE...')
    time.sleep(2)
    print('INFORMAÇÕES CORRETAS!')
    time.sleep(1)

    while True:
        continuar = input('GOSTARIA DE CONTINUAR O CADASTRO? [S/N] ').strip().upper()

        if continuar in ['N', 'NAO', 'NÃO']:
            print('CADASTRO CANCELADO PELO USUÁRIO!!!')
            sys.exit() 
        elif continuar in ['S', 'SIM', '']:
            print('CERTO! ENTÃO CONTINUAREMOS SEU CADASTRO')
            break 
        else:
            print('Opção inválida! Digite S para Sim ou N para Não.')

    print('-~-' * 30)
    print('Agora iniciaremos o cadastro em nosso sistema! ')
    print('-~-' * 30)

    while True:
        verificacao = input('Digite seu email pessoal: ')
        
        if not verificacao.strip():
            print('Email inválido o campo está vazio')
            continue
        elif '@' not in verificacao:
            print('Email inválido, faltando o caractere "@"')
            continue
        
        ver = verificacao.strip().lower()
        confirmar = input(f'Seu email é {ver} está correto? S/N: ').strip().upper()
        
        if confirmar in ['S', 'SIM']:
             print('Enviaremos um código de verificação para o seu email')
             break
        else:
             print('Preencha o campo novamente')
             continue

    print("\n--- CADASTRO FINALIZADO COM SUCESSO ---")

if __name__ == "__main__":
    main()
