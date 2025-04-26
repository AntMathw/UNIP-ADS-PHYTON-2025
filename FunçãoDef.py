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

#Calculo da Formula de Fibonacci

a1 = 0
a2 = 1
n = int(input('Digite o número de termos: '))
cont = 3
print('{} {}'.format(a1, a2), end=' ')
while cont <= n:
    a3 = a2 + a1
    print('{}'.format(a3), end=' ')
    cont += 1
    a1 = a2
    a2 = a3

