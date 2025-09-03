#Soma de dois numeros(DEF FUCTION)

def soma(num1, num2):
    return num1 + num2

def main():
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite segundo valor: '))
    print('A soma entre {} e {} é {}'.format(num1, num2, soma(num1, num2)))

if __name__ == '__main__':
    main()

#Média de duas provas (DEF FUCTION)

def calculo_media(np1, np2):
    return (np1 + np2) / 2

def main():
    np1 = float(input('Valor da primeira prova: '))
    np2 = float(input('Valor da segunda prova: '))
    print('A nota entre {} e {} a média {}'.format(np1, np2, calculo_media(np1, np2)))


if __name__ == '__main__':
    main()

#Par ou Impar(DEF FUNCTION)

def impar_par(num1):
    return num1 % 2 == 0


def main():
    num1 = int(input('Digite um valor: '))
    if impar_par(num1):
        print('Par')
    else:
        print('Impar'.format(num1 % 3 == 0))

#Contagem Regressiva(DEF FUNCTION)

def contagem(num):
    for i in range(9, 0, -1):
        print(i)

def main():
    numero = int(input('Digite um numero: '))
    contagem(numero)

if __name__ == '__main__':
    main()



if __name__ == '__main__':
    main()

#Maior número entre dois

def maior_menor(num1, num2):
    return num1 > num2 or num2 > num1

def main():
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))
    if num1 > num2:
        print('O primeiro valor é maior: {}'.format(num1))
    elif num1 == num2:
        print('Os numeros são igual ')
    elif num2 > num1:
        print('O segundo valor é maior: {}'.format(num2))



if __name__ == '__main__':
    main()

#Positivo, Negativo ou Nulo

import sys

def variacao_cont(num):
    if num == 0:
        return 0
    elif num > 0:
        return 1
    else:
        return -1

def main():
    numero = int(input('Digite um valor: '))
    v = variacao_cont(numero)
    if v == 0:
        print('O numero e nulo')
    elif v > 0:
        print('O numero é positivo')
    elif v < 0:
        print('O numero é negativo')



if __name__=='__main__':
    main()

#Tabuada em DEF

import sys

def tabuada(num):
    for i in range(1, 11):
        resultado = num * i
        print("{} x {} = {}".format(num, i, resultado))

def main():
    numero = int(input('Digite um número para ver a tabuada: '))
    tabuada(numero)


if __name__ == '__main__':
    main()



#Calculo da velocidade media
import sys

def calculaVelocidadeMedia(distancia, tempo):
    return distancia / tempo
    

def main():
    d = float(input("Informe a distancia para chegar no seu destino: "))
    t = int(input("Informe quantas horas você tem para chegar: "))
    velocidadeMedia = calculaVelocidadeMedia(d, t)
    print(f"A velocidade média para chegar no destino é {velocidadeMedia} Km por hora.")

if __name__=="__main__":
    main()

#Calculo do numero fatorial
import sys
import math

def valorFatorial(num):
    return math.factorial(valorFatorial)
    
def main():
    num = int(input('Digite um valor'))
    fatorial = math.factorial(num)
    print('O valor fatorial desse numero é: {}'.format(fatorial))

if __name__=='__main__':
    main()

#Sequencia de Fibonacci

def fibonacci_recursive(n):
    
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

num_terms = 10
for i in range(num_terms):
    print(fibonacci_recursive(i), end=" ")

#Numeros primos

def encontrar_primo(numero):


  if numero <= 1:
    return False
  if numero <= 3:
    return True
  if numero % 2 == 0 or numero % 3 == 0:
    return False
  i = 5
  while i * i <= numero:
    if numero % i == 0 or numero % (i + 2) == 0:
      return False
    i += 6
  return True

def main():
  numero = int(input('Digite um valor: '))

  if encontrar_primo(numero):
    print("{} é um número primo.".format(encontrar_primo(numero)))
  else:
    print("{} não é um número primo.".format(encontrar_primo(numero)))

if __name__ == '__main__':
  main()

#Tuplas em função DEF


def comidas():
    lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
    return lanche

def main():
    itens = comidas()
    for pos, item in enumerate(itens):
        print(f'Eu vou comer {itens}, na posição{pos}')

if __name__ == '__main__':
  main()

#Jogo de Pedra, Papel e Tesoura

import random


def main():
    opcoes = ['pedra', 'papel', 'tesoura']

    print("Vamos jogar Pedra, Papel e Tesoura!")
    escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()

    if escolha_usuario not in opcoes:
        print("Escolha inválida! Por favor, escolha pedra, papel ou tesoura.")
        return

    escolha_computador = random.choice(opcoes)
    print(f"O computador escolheu: {escolha_computador}")

    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
            (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
            (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        print("Você ganhou!")
    else:
        print("Você perdeu!")


if __name__ == "__main__":
    main()

#Ler nome do usuário e sua idade(JSON)

import json


def salvar_dados(nome, idade, arquivo='dados.json'):
    dados = {
        'nome': nome,
        'idade': idade
    }
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)
    print("✅ Dados salvos com sucesso!")

def carregar_dados(arquivo='dados.json'):
    try:
        with open(arquivo, 'r') as f:
            dados = json.load(f)
        print("Dados carregados:")
        print(f"Nome: {dados['nome']}")
        print(f"Idade: {dados['idade']}")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON.")


if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    
    salvar_dados(nome, idade)
    print("\nAgora vamos ler os dados salvos...\n")
    carregar_dados()

#Sensor de Temperatura

import random

def gerar_dados_sensor(qtd_leitura):
    dados_sensor = [round(random.uniform(15.0, 35.0),2) for  _ in range(qtd_leitura)]
    return dados_sensor

def principal():
    quantidade_leituras = 10000
    dados = gerar_dados_sensor(quantidade_leituras)
    print(f'Quantidade de leituras geradas: {dados[3:9999]} ')
    for i in range(0, 9):
        print(f'Leitura dos {dados[0:99]} numeros primeiros')


if __name__ == '__main__':
    principal()















