#Calculo da Média
import sys


def calc_Media(prova1, prova2):
    return (prova1 + prova2) / 2.0

def main():
    prova1 = float(input('Digite a primeira nota: '))
    prova2 = float(input('Digite a segunda nota: '))
    media = calc_Media(prova1, prova2)
    print('A média do aluno foi {:.2f}'.format(media))

main()

#Somatório de dois valores

def soma(num1, num2):
    somatorio = num1 + num2
    return somatorio

def main():
    num1 = int(input('Digite um valor: '))
    num2 = int(input("Digite outro valor: "))
    resultado = soma(num1, num2)
    print(f'A soma entre {num1} + {num2} = {resultado}')

main()


