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

# -*- coding: utf-8 -*-
# Importa o módulo 'sys' para permitir sair do programa.
import sys

# Variável global (a estrutura de dados principal) que armazena todas as tarefas.
# Em aplicações maiores, isto estaria dentro de uma classe.
tarefas = []

def mostrar_menu():
    """
    Exibe o menu de opções para o usuário.
    """
    print("\n" + "="*30)
    print("  GERENCIADOR DE TAREFAS")
    print("="*30)
    print("[1] Adicionar Nova Tarefa")
    print("[2] Ver Lista de Tarefas")
    print("[3] Marcar Tarefa como Concluída (Remover)")
    print("[4] Sair do Programa")
    print("="*30)
    
def adicionar_tarefa(descricao):
    """
    Adiciona uma nova tarefa à lista.
    Args:
        descricao (str): A descrição textual da tarefa a ser adicionada.
    """
    # Verifica se a descrição não está vazia
    if descricao:
        tarefas.append(descricao)
        print(f"\n✅ Tarefa adicionada: '{descricao}'")
    else:
        print("\n❌ A descrição da tarefa não pode estar vazia.")

def mostrar_tarefas():
    """
    Exibe todas as tarefas pendentes com seu número de índice.
    """
    if not tarefas:
        print("\n📝 Sua lista de tarefas está vazia. Que bom!")
        return

    print("\n--- LISTA DE TAREFAS PENDENTES ---")
    # Usa 'enumerate' para obter o índice (i) e o valor (tarefa)
    for i, tarefa in enumerate(tarefas):
        # O índice para o usuário é (i + 1) para ser mais amigável
        print(f"[{i + 1}] {tarefa}")
    print("---------------------------------")


def remover_tarefa(indice):
    """
    Remove uma tarefa da lista baseado no índice fornecido pelo usuário.
    Args:
        indice (int): O número da tarefa (começando em 1) a ser removida.
    """
    # O índice do usuário é 1-based, então convertemos para 0-based
    indice_real = indice - 1

    # Validação para garantir que o índice está dentro dos limites da lista
    if 0 <= indice_real < len(tarefas):
        # O método pop(indice) remove e retorna o elemento naquela posição
        tarefa_concluida = tarefas.pop(indice_real)
        print(f"\n🎉 Tarefa CONCLUÍDA e removida: '{tarefa_concluida}'")
    else:
        print(f"\n❌ Erro: Índice '{indice}' inválido. Verifique a lista novamente.")

def main():
    """
    Função principal que controla o fluxo do programa.
    """
    while True:
        mostrar_menu()
        
        # Pede a entrada do usuário e trata possíveis erros de digitação (ex: letras)
        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("\n⚠️ Entrada inválida. Por favor, digite um número de 1 a 4.")
            continue

        if escolha == 1:
            # Opção 1: Adicionar Tarefa
            nova_tarefa = input("Digite a descrição da nova tarefa: ")
            adicionar_tarefa(nova_tarefa.strip()) # strip() remove espaços em branco extras
        
        elif escolha == 2:
            # Opção 2: Ver Tarefas
            mostrar_tarefas()

        elif escolha == 3:
            # Opção 3: Remover Tarefa (Marcar como Concluída)
            mostrar_tarefas()
            try:
                if tarefas:
                    num_tarefa = int(input("Digite o NÚMERO da tarefa concluída para remover: "))
                    remover_tarefa(num_tarefa)
                else:
                    print("Não há tarefas para remover.")
            except ValueError:
                print("\n⚠️ Entrada inválida. Por favor, digite o número da tarefa.")

        elif escolha == 4:
            # Opção 4: Sair
            print("\n👋 Obrigado por usar o Gerenciador de Tarefas. Até mais!")
            sys.exit(0) # Sai do programa
        
        else:
            # Tratamento para números fora do menu (ex: 5, 0, etc.)
            print("\n❌ Opção não reconhecida. Por favor, escolha uma opção válida do menu.")
def dividir_conta():
    print("--- Calculadora de Racha Conta ---")

    try:
        # 1. Entradas do usuário
        valor_conta = float(input("Qual o valor total da conta? R$ "))
        porcentagem_garcom = int(input("Qual a % do garçom? (ex: 10, 12, 15): "))
        numero_pessoas = int(input("Quantas pessoas vão dividir? "))

        # 2. Multiplicação: Calcular o valor do serviço
        # Convertemos a porcentagem (ex: 10) para decimal (0.10) multiplicando
        valor_servico = valor_conta * (porcentagem_garcom / 100)
        
        # Somar tudo
        total_final = valor_conta + valor_servico

        # 3. Divisão: Calcular quanto cada um paga
        valor_por_pessoa = total_final / numero_pessoas

        # 4. Exibir resultados
        print("\n--- Resultado ---")
        print(f"Valor do serviço ({porcentagem_garcom}%): R$ {valor_servico:.2f}")
        print(f"Total com serviço: R$ {total_final:.2f}")
        print("-" * 30) # Multiplicação de strings (repete o traço 30 vezes)
        print(f"CADA UM PAGA: R$ {valor_por_pessoa:.2f}")

    except ZeroDivisionError:
        print("\nErro: O número de pessoas não pode ser zero!")
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos.")

# Executa o programa
if __name__ == "__main__":
    dividir_conta()

# Ponto de entrada do programa.
# Esta é a estrutura padrão para garantir que a função 'main' seja chamada apenas
# quando o arquivo for executado diretamente, e não quando for importado.
if __name__ == "__main__":
    main()

