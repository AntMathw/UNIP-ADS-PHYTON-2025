import sys # Usado apenas para encerrar o programa suavemente em caso de erro

# --- Configuração de Cores (ANSI) ---
VERDE = '\033[1;32m'
VERMELHO = '\033[1;31m'
AZUL = '\033[1;34m'
AMARELO = '\033[1;33m'
RESET = '\033[m'

def analisar_emprestimo():
    print(f'{AZUL}-=' * 20)
    print(f'   🏦  SISTEMA DE ANÁLISE DE CRÉDITO  🏦')
    print(f'-=' * 20 + f'{RESET}')

    # 1. Entrada de Dados com Tratamento de Erro
    try:
        valor_casa = float(input('Qual o valor do imóvel? R$ '))
        salario = float(input('Qual o salário do comprador? R$ '))
        anos = int(input('Em quantos anos pretende pagar? '))

        if anos <= 0:
            print(f'\n{VERMELHO}Erro: O tempo de pagamento deve ser maior que zero.{RESET}')
            return # Sai da função

    except ValueError:
        print(f'\n{VERMELHO}Erro: Você digitou um texto em vez de número. Tente novamente.{RESET}')
        return # Sai da função

    # 2. Processamento (Cálculos)
    meses = anos * 12
    prestacao_mensal = valor_casa / meses
    
    # Regra do Banco: Limite de 30% do salário
    limite_aprovacao = salario * 0.30
    
    # Cálculo da porcentagem comprometida (para informação extra)
    porcentagem_comprometida = (prestacao_mensal / salario) * 100

    # 3. Exibição do Relatório
    print('\n' + '-'*40)
    print(f'RELATÓRIO DE FINANCIAMENTO')
    print('-'*40)
    print(f'Valor do Imóvel:   R$ {valor_casa:,.2f}')
    print(f'Prazo:             {anos} anos ({meses} meses)')
    print(f'Prestação Mensal:  R$ {prestacao_mensal:,.2f}')
    print(f'Seu Limite (30%):  R$ {limite_aprovacao:,.2f}')
    print(f'Renda Comprometida: {porcentagem_comprometida:.1f}%')
    print('-'*40)

    # 4. Decisão Final
    print(f'STATUS: ', end='')
    
    if prestacao_mensal <= limite_aprovacao:
        print(f'{VERDE}APROVADO ✅{RESET}')
        print(f'{AMARELO}Parabéns! O financiamento cabe no seu bolso.{RESET}')
    else:
        diferenca = prestacao_mensal - limite_aprovacao
        print(f'{VERMELHO}NEGADO ❌{RESET}')
        print(f'A parcela excede seu limite em R$ {diferenca:,.2f}.')
        print('Sugestão: Tente aumentar o número de anos.')

# Execução do programa
if __name__ == "__main__":
    analisar_emprestimo()
