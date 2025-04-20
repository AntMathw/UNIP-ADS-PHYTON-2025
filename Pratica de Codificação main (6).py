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





