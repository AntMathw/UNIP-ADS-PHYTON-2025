#Contagem regressiva para ano novo

import time

for i in range(10 , 0 , -1):
    print(i)
    sleep(1)
print('FELIZ ANO NOVO!!!')

#Saber se um número e par ou ímpar

for par in range(2, 52, 2):
    if par % 2 == 0:
        print(par, end=' ')
print('ACABOU')

#Soma entre números ímpares

cont = 0
soma = 0
for impar in range(3, 501, 3):
    if impar % 2 == 1:
        cont += impar
        soma += 1

print('A soma é {} e o numero de valores é {}'.format(soma, cont, end=' '))

#Tabuada de um número

num = int(input('Digite um número e veja sua tabuada: '))
for vezes in range(1, 11):
    final = num * vezes
    print('{} x {} = {}'.format(num, vezes, final))

#Soma de apenas números pares

soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input('Digite um valor: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('A soma dos numeros pares é {}, e possui {} pares'.format(soma, cont))

#Progressão aritmética

print('=' * 35)
print('TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('=' * 35)

primeiro = int(input('Digite o pimeiro termo: '))
razao = int(input('Digite a razão: '))

for i in range(0 , 10):
    print(primeiro + (razao * i), end=' => ')
print('FIM')

#Identificando um número primo

num = int(input('Digite um número: '))
total = 0

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[34m', end='')
        total += 1

    else:
        print('\033[m', end='')
    print('{} '.format(i), end='')
if total == 2:
    print('\n\033[mÉ um número primo.')
else:
    print('\n\033[mEsté número não é primo.')

#Identificador de um palíndromo

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
j = ''.join(palavras)
inv = ''
for letra in range(len(j) - 1, - 1, - 1):
    inv += j[letra]
if inv == j:
    print('É políndromo.')
else:
    print('Não é políndromo.')

#Classificação de um maioridades

from datetime import date

menor = 0
maior = 0

for idade in range(0, 7):
  nascimento = int(input('Digite o ano de nascimento: '))
    idade2 = date.today().year - nascimento
    if idade2 >= 18:
        maior += 1
    else:
        menor += 1
print('De 7 pessoas {} são jovens e {} pessoas são mais velhos'.format(menor, maior))

#Maior e menor peso da sequência

menor = 0
maior = 0

for p in range(1, 6):
  peso = float(input('Digite o peso da {} pessoa'.format(p)))
 
  if p == 1:
    peso = maior
    peso = menor
  else:
    if peso > maior:
      peso = maior
    if peso < menor:
      peso = menor

print('Das 5 pessoas, o maior peso é {}KG e o menor peso é {}KG'.format(maior, menor)

#Média de idade, o nome do mais velho e nº de mulheres com menos de 20 anos

somaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulheres = 0

for p in range(1, 5):
    print('==' * 14)
    nome = str(input('Digite o nome da {}ª pessoa: '.format(p))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(p)))
    sexo = str(input('Digite o sexo da {}ª pessoa: [M/F] '.format(p))).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulheres += 1
media = somaidade / 4

print('A média de idade das 4 pessoas é de {} anos.'.format(media))
print('A idade do homem mais velho é de {} e o seu nome é {}.'.format(maioridadehomem, nomevelho))
if totalmulheres >= 2:
    print('No total, existem {} mulheres com menos de 20 anos.'.format(totalmulheres))
elif totalmulheres == 1:
    print('No total, existe {} mulher com menos de 20 anos.'.format(totalmulheres))
else:
    print('No total, existem {} mulheres com menos de 20 anos.'.format(totalmulheres))
  
