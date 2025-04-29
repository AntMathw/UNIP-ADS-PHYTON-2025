#Soma de dois numeros(DEF FUCTION)

def soma(num1, num2):
    return num1 + num2

def main():
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite segundo valor: '))
    print('A soma entre {} e {} é {}'.format(num1, num2, soma(num1, num2)))

if __name__ == '__main__':
    main()

#Média de duas provas (DEF FUCTION)

def calculo_media(np1, np2):
    return (np1 + np2) / 2

def main():
    np1 = float(input('Valor da primeira prova: '))
    np2 = float(input('Valor da segunda prova: '))
    print('A nota entre {} e {} a média {}'.format(np1, np2, calculo_media(np1, np2)))


if __name__ == '__main__':
    main()

#Par ou Impar(DEF FUNCTION)

def impar_par(num1):
    return num1 % 2 == 0


def main():
    num1 = int(input('Digite um valor: '))
    if impar_par(num1):
        print('Par')
    else:
        print('Impar'.format(num1 % 3 == 0))



if __name__ == '__main__':
    main()

#Maior número entre dois

def maior_menor(num1, num2):
    return num1 > num2 or num2 > num1

def main():
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))
    if num1 > num2:
        print('O primeiro valor é maior: {}'.format(num1))
    elif num1 == num2:
        print('Os numeros são igual ')
    elif num2 > num1:
        print('O segundo valor é maior: {}'.format(num2))



if __name__ == '__main__':
    main()



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

def fibonacci_recursive(n):
    
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

num_terms = 10
for i in range(num_terms):
    print(fibonacci_recursive(i), end=" ")

#Numeros primos

def encontrar_primo(numero):


  if numero <= 1:
    return False
  if numero <= 3:
    return True
  if numero % 2 == 0 or numero % 3 == 0:
    return False
  i = 5
  while i * i <= numero:
    if numero % i == 0 or numero % (i + 2) == 0:
      return False
    i += 6
  return True

def main():
  numero = int(input('Digite um valor: '))

  if encontrar_primo(numero):
    print("{} é um número primo.".format(encontrar_primo(numero)))
  else:
    print("{} não é um número primo.".format(encontrar_primo(numero)))

if __name__ == '__main__':
  main()



