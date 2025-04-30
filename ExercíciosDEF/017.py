#Frase se é um palindromo

import sys

def palindromo(string):

    texto_processado = re.sub(r'[^a-zA-Z0-9]', '', string.lower())
    size = (len(string))
    if size == 0:
        return False
    for i in range(0, size // 2):
        if string[i] != string[size - i - 1]:
            return False
        return True

def main():
    frase = input('Digite uma frase: ')
    if palindromo(frase):
        print('Sua frase em palindromo {}'.format(frase))
    else:
        print('Não é um palindromo')



if __name__ == '__main__':
    main()






