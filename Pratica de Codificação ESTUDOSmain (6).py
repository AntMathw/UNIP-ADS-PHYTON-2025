#Velocidade média
import sys
    
def calculaVelocidadeMedia(distancia, tempo):
    return distancia / tempo
    
def main():
    d = float(input('Valor da distancia: '))
    t = float(input('Valor do tempo: '))
    velocidademedia = calculaVelocidadeMedia(d, t)
    print(f'A velocidade média {velocidademedia} é: ')
    
if __name__=="__main__":
    main()
    
#Saber se um numero e positivo, negativo ou igual a 0
n = int(input('Digite o primeiro valor'));

if n > 0:
    print('O valor e positivo')
if n < 0:
    print('O valor e negativo')
if n == 0:
    print('O valor é igual a zero')

#Numero antecessor e sucessor
n = int(input('Digite um valor'))
num1 = n - 1
num2 = n + 1
print('Analisando o numero {}, o seu antecessor é {}, o seu sucessor é {}'.format(n, num1, num2))

#Numero antecessor e sucessor 2.0
n = int(input('Digite um valor'))
print('Analisando o numero {}, o seu antecessor é {}, o seu sucessor é {}'.format(n, (n-1), (n+1)))

#Dobro Triplo e Raiz Quadrada
n = float(input('Digite um valor'))
print('\nO dobro do numéro é {} , \nseu triplo é {} \ne a raiz quadrada é {}'.format((n * 2), (n * 3), (n ** (1/2))))

#Dobro Triplo e Raiz Quadrada 2.0
n = float(input('Digite um valor'))
num1 = n * 2 
num2 = n * 3
num3 = n ** (1/2)
print('O dobro do número {}'.format(num1))
print('O triplo do número {}'.format(num2))
print('A raiz quadrada é {}'.format(num3))

#Média aritmética

nt = float(input('Nota da primeira prova da NP1'))
nt2 = float(input('Nota da segunda prova da NP2'))
print('Somando a primeira prova {}, e a segunda {}, a média do aluno é {}'.format(nt, nt2, (nt + nt2)/2 ))

#Média aritmética2.0

nt = float(input('Nota da primeira prova da NP1'))
nt2 = float(input('Nota da segunda prova da NP2'))
m = (nt + nt2) /2 
print('A nota da primeira prova {}, e da segunda {}, a média do aluno foi {}'.format(nt, nt2, m))

#Unidade de medida
m = float(input('Numero em metros'))
km = m  / 1000
hc = m / 100
dc = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('\n{}quilometros, \n{}hectometro, \n{}decametro, \n{}decimetro, \n{}centimetro, \n{}milimetro'.format(km, hc, dc, dm, cm, mm))

#unidade de Media 2.0
medida = float(input('Valor em metros'))
print('\n{}Quilometros \n{}Hectometro \n{}decametro \n{}decimetro \n{}centimetro \n{}milimetro'.format((medida / 1000), (medida / 100), (medida / 10), (medida * 10), (medida * 100), (medida * 1000)))

#Calculo de Porcentagem AUMENTO
nome = float(input('Digite o salário do funcionário, R$'))
valor = nome + (nome * 15 / 100)
print('O salário do funcionário é {:.2f}, com 15% de desconto, seu salário atual é {:.2f}'.format(nome, valor))

#Calculo de porcentagem AUMENTO 2.0
nome = float(input('Digite o salário do funcionário, R$'))
print('O salário do funcionário é {:.2f}, com 15% de desconto, seu salário atual é {:.2f}'.format(nome, (nome + (nome * 15 / 100))))

#Porcentagem com DESCONTO
nome = float(input('Digite o salário do funcionário, R$'))
valor = nome - (nome * 5 / 100)
print('O salário do funcionário é {:.2f}, com 5% de desconto, atual ele recebe {:.2f}'.format(nome, valor))

#Porcentagem com DESCONTO 2.0
nome = float(input('Digite o salário do seu funcionário, R$'))
print('O salário do funcionário é {:.2f}, com 5% de desconto, atualmente ele recebe {:.2f}'.format(nome, (nome - (nome * 5 / 100))))

#Conversor de Graus Celsius para Fahrenheit
c = float(input('Digite o valor de Grau C^'))
f = (c * 1.8) + 32
print('O graus em C é {}, convertido para fahrenheit é {}'.format(c, f))

#Conversor de Graus Celsius para Fahrenheit 2.0
c = float(input('Digite um valor de Graus C^'))
print('O graus em C é {}, convertido para fahrenheit é {}'.format(c, (c * (9/5) + 32)))

#Aluguel de automóveis
dias = int(input('Quantos dias você alugará esse carro?'))
km = float(input('Quantos Km você rodou com o carro?'))
print('O total a pagar é R${:.2f}'.format((dias * 60.00) + (km * 0.15)))

#Aluguel de automóveis
dias = int(input('Quantos dias será alugado?'))
km = float(input('Quantos Km você rodará com o carro?'))
pagamento = (dias * 60) + (km * 0.15)
print('O total a pagar é R${:.2f}'.format(pagamento))

#Codificação para ler um número real em valor inteiro
from math import trunc

num = float(input('Digite um valor'))
valor = trunc(num)
#Primeira Forma de ler um numero real para inteiro
print('O numero real é {}, e seu valor inteiro é {}'.format(num, valor))
#Segunda forma para ler um numero real para inteiro
print('O numero real é {}, e seu valor inteiro é {}'.format(num, (trunc(num))))

#Teorema de Pitagores, CATETO OPOSTO, CATETO ADJACENTE e valor da HIPOTENUSA
from math import sqrt, pow
cateto1 = int(input('Digite o valor do Cateto Oposto'))
cateto2 = int(input('Digite o valor do Cateto Adjacente '))
soma = pow(cateto1, 2) + pow(cateto2, 2) 
print('A soma dos cateto é{}, a hipotenusa do triângulo é {:.2f}'.format((soma),(sqrt(soma))))

#Outra forma de Calcular o Teorema de Pitagoras, CATETO OPOSTO, CATETO ADJACENTE e valor da HIPOTENUSA
import math 

cateto_op = float(input('Comprimento do cateto oposto'))
cateto_ad = float(input('Comprimento do cateto adjacente'))
hipotenusa = math.hypot(cateto_op, cateto_ad)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))

#Calculo do Seno, Cosseno e Tangente
from math import sin, cos, tan, radians

angulo = float(input('Descreve o angulo que deseja: '))
angulo_radiano =  radians(angulo)
seno = sin(angulo_radiano)
cosseno = cos(angulo_radiano)
tangente = tan(angulo_radiano)
print('O angulo de {} \nseno é {:.2f} \ncosseno é {:.2f} \ntangente {:.2f}'.format(angulo, seno, cosseno, tangente))

#Calculo do Seno, Cosseno e Tangente de outra forma
import math

angulo = float(input('Digite o angulo que deseja'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo {} em seno é {:.2f}\nCosseno é {:.2f}\nTangente é {:.2f}'.format(angulo, seno, cosseno, tangente ))

#Exemplo de lista
import random

n1 = str(input('O primeiro aluno '))
n2 = str(input('Segundo aluno '))
n3 = str(input('Terceiro aluno '))
n4 = str(input('Quarto aluno '))
lista = [n1, n2, n3, n4]
print('A escolha do professor é: {}'.format(random.choice(lista)))

#Exemplo de lista 2.0
from random import choice

n1 = str(input('Primero Aluno '))
n2 = str(input('Segundo Aluno '))
n3 = str(input('Terceiro Aluno '))
n4 = str(input('Quarto aluno '))
lista = [n1, n2, n3, n4]
escolha = choice(lista)
print('O escolhido foi: {}'.format(escolha))

#Exeplo de lista de ordem randomica

from random import shuffle

n1 = str(input('Primeiro Aluno '))
n2 = str(input('Segundo Aluno '))
n3 = str(input('Terceiro Aluno '))
n4 = str(input('Quarto aluno '))
lista = [n1, n2, n3 ,n4]
shuffle(lista)
print('A ordem de apresentação séra: {}'.format(lista))

#Exeplo de lista de ordem randomica 2.0
import random

n1 = str(input('Primeiro aluno '))
n2 = str(input('Segundo aluno '))
n3 = str(input('Terceiro aluno '))
n4 = str(input('Quarto aluno '))
lista = [n1, n2, n3, n4]
print('A ordem dos alunos é: {}'.format(random.choice(lista)))

#Separando digitos de um número

numero = int(input('Informe um numero: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Analisando o numero: {} \nunidade {} \ndezena {} \ncentena {} \nmilhar {}'.format(numero, unidade, dezena, centena, milhar))

#Separando digitos de um número 2.0
numero = int(input('Informe um numero: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Analisando o numero: {}'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))

#Verificando primeiras letras do texto
cidade = str(input('Digite o nome da cidade: ')).upper().strip().split()
print('SANTO' in cidade[0])

#Verificando primeira e ultima ocorrência em uma string
nome = str(input('Digite o seu nome: ')).upper().strip().split()
print('SILVA' in nome)

#Manipulando texto
nome = str(input('Digite seu nome completo: '))
print('Seu nome em MAIUSCULO é {} \nSeu nome em minusculo é {}'.format(nome.upper(), nome.lower()))
print('Seu nome possui {}letras \nSeu primeiro nome {} possui {} letras'.format(len(nome) - nome.count(' '), nome.split()[0], len(nome.split()[0])))

#Manipulando string, quantas vezes aparece em primeiro e em último
frase = str(input('Digite uma frase: '))
print(frase.count('A'), frase.count('a'), frase.count('Ã'), frase.count('ã'))
print(frase.find('A'), frase.find('a'))
print(frase.rfind('a'), frase.rfind('A'))

#Lendo uma string em que se encontra em primeiro e ultimo
nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
print('Seu primero nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))

#Jogo de advinhação com IF e ELSE

from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em número de 0 a 5. TENTE ADVINHAR...'.format(computador))
print('-=-' * 20)
jogador = int(input('Em que numero pensei? '))
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    #print('PARABENS! Você me venceu!')
else:
    print('GANHEI! Eu escolhi o numero {} e nao {}'.format(computador, jogador))

#Radar Eletrônico
velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Você está dirigindo com segurança! Tenha um bom dia!')
else:
    print('MULTADO! Você execedeu o  limite de velocidade permitido que é de 80KM/hr\nVocê deve pagar um multa de R${}!'.format(multa))
    print('Tenha um bom dia!')

#Número impar ou par
numero = int(input('Informe um valor: '))
if numero % 2 == 0:
    print('O número é PAR')
else:
    print('Ele é ÍMPAR')

#Distância da viagem
viagem = float(input('Qual a distância da viagem? '))
print('Você está preste a fazer uma viagem de {:.1f}km'.format(viagem))
if viagem <= 200:
    print('O preço da sua passagem será de R${:.2f}'.format(viagem * 0.50))
else:
    print('O preço da sua passagem será de R${:.2f}'.format(viagem * 0.45))

#Calculo do Ano Bissexto
from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Seu ano {} é BISSEXTO'.format(ano))
else:
    print('Seu ano {} não é BISSEXTO'.format(ano))

#Menor e Maior Valor
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O maior valor digitado foi o {} e o menor {}.'.format(maior, menor))

#Aumento salário de acordo com o salário original
salario = float(input('Qual o salário do funcionário? R$ '))
if salario <= 1250:
    print('Quem ganhava R${}, passa a ganhar R$ {:.2f} agora'.format(salario, (salario * 1.15)))
elif salario > 1250:
    print('Quem ganhava R${}, passa a ganhar R$ {:.2f} agora'.format(salario, (salario * 1.10)))

#Saber se um traingulo existe
r1 = float(input('Digite primero segmento da reta'))
r2 = float(input('Digite o segundo segmento da reta'))
r3 = float(input('Digite o tercerio seggmento da reta'))
if r1 < r2 + r3 and r1 < r3 + r2 and r2 < r3 + r1:
    print('O triangulo existe')
else:
    print('O triangulo nao existe')


