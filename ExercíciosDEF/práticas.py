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

# Definindo a função que recebe dois números e retorna a soma deles
def somar(a, b):
    return a + b

# Chamando a função e imprimindo o resultado
resultado = somar(5, 3)
print("A soma é:", resultado)

def main():
    """
    Função principal onde a execução do seu programa começa.
    """
    # 1. Defina uma variável
    mensagem = "Olá do meu script Python!"

    # 2. Imprima a variável
    print(mensagem)

    # 3. Chame outras funções (se houver)
    resultado = calcular_algo(5, 3)
    print(f"O resultado do cálculo é: {resultado}")


def calcular_algo(a, b):
    """
    Uma função auxiliar que realiza alguma operação.
    """
    return a + b


# Bloco de execução principal
if __name__ == "__main__":
    main()

