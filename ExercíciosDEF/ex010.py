#Fatorial de um número

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



