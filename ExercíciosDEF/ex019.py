#Contagem de vogais em uma Frase

import sys

def contagem_vogais(frase):

    string = str.lower(frase)
    result = 0
    vogais = 'aeiou'
    return sum(string.count(i) for i in vogais)

def main():
    frase = str(input('Digite uma frase: '))
    num_vogais = contagem_vogais(frase)
    if num_vogais > 0:
        print('A frase possui {} vogais'.format(num_vogais))
    else:
        print('A frase não possui vogais')



if __name__ == '__main__':
    main()
