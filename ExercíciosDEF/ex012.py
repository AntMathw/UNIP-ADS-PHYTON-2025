#Numeros Primos

import sys

def ehPrimo(numero):
    if type(numero) != int:
        return False
    if numero <= 2:
        return True

    for i in range(2, numero):
        if numero % i == 0:
            return False

        return True

def main():

    valor = int(input('Digite um valor: '))
    if ehPrimo(valor):
        print('O numero {} é primo.'.format(valor))
    else:
        print('O numero {} não é primo.'.format(valor))





