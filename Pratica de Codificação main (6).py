#Soma de dois numeros 
num = int(input('Escreva o primeiro numero'))
num2 = int(input('Escreva o segundo numero'))
soma = num + num2
print(f'O resultado é {soma}')

#Divisão de um numero e multiplicação
n = float(input('Escreva o primeiro valor'))
n2 = float(input('Escreva o segundo valor'))
n3 = float(input('Escreva o terceiro valor'))
r = n / n2 * n3

print(f'O resultado dessa conta {r} é')

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



