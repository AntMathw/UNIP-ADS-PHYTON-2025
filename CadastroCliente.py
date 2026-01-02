import time

print('-=-'*15)
print('CADASTRO DE USUÁRIO')
print('-=-'*15)
time.sleep(1) # Diminui um pouco para não ficar muito lento nos testes

print('Olá usuário, então vamos começar o seu cadastro!')
print('=-='*15)
time.sleep(1)

print('Primeiramente gostaria de saber seu nome e sobrenome!')
print('=-='*15)
time.sleep(1)

# CORREÇÃO 1: Validação do nome dentro do Loop
while True:
    nome = input('Digite seu primeiro nome: ')
    
    # Verifica se está vazio
    if not nome.strip():
        print('Nome inválido, o campo não pode ficar vazio!')
    else:
        # Se deu certo, formata e QUEBRA o loop (sai dele)
        n2 = nome.strip().capitalize()
        break 

sobrenome = input('Digite seu sobrenome: ')
s2 = sobrenome.strip().capitalize()

time.sleep(1)
print('Certo! Agora gostaria de saber sua idade e seu CPF')

# Tratamento de erro simples para idade (caso digitem letras)
try:
    idade = int(input('Digite sua idade: '))
except ValueError:
    print("Idade inválida. Considerando 0.")
    idade = 0

# CORREÇÃO 2: CPF como string para não perder zeros a esquerda
cpf = input('Digite seu CPF (apenas números): ')

print('Carregando cadastro...')
time.sleep(3)
print('-'*30)
print(f'Seu nome é {n2} {s2}')
print(f'Atualmente possui {idade} anos')
print(f'Portador do CPF {cpf}')
print('-'*30)

# CORREÇÃO 3: Lógica da CNH
# Removemos o int(), pois a resposta é letra (S ou N)
# .upper() transforma em maiúscula para aceitar tanto 's' quanto 'S'
cnh = input('O usuário possui CNH (Carteira Nacional de Habilitação)? [S/N]: ').strip().upper()

if cnh == 'S':
    print('Você possui CNH, e o código registrado é 786546884')
elif cnh == 'N':
    print('Você não possui CNH')
else:
    print('Opção inválida (Digite apenas S ou N).')
