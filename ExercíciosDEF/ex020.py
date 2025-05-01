#Calculo do Juros Composto

import sys

def juros_composto(valor_inicial, taxa_juros, tempo_meses):
    montante_final = valor_inicial * (1 + taxa_juros) ** tempo_meses
    return montante_final


def main():
    valor_inicial_usuario = float(input('Digite o seu valor: R$'))
    taxa_juros_percentual = int(input('Digite a taxa do juros: %'))
    tempo_meses = int(input('Digite o tempo em meses '))

    taxa_juros_decimal = taxa_juros_percentual / 100
    montante = juros_composto(valor_inicial_usuario, taxa_juros_decimal, tempo_meses)

    print('O montante final após {} meses será R${:.2f}'.format(tempo_meses, montante))


if __name__ == '__main__':
    main()
