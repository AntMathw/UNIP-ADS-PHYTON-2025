#Lista em formato de Pilhas com INSERT, POP e DEL 
#LIFO (Last In First Out)

def main():
    
    pilha = []
    print(f'Pilha vazia {pilha}')

    pilha.insert(0,2)
    print(pilha)
    pilha.insert(1, 31)
    print(pilha)
    pilha.insert(2, 42)
    print(pilha)
    pilha.insert(3, 40)

    pilha.pop(0)
    print(pilha)

    del pilha[0: 2]
    print(pilha)

    pilha.insert(4, 90)
    print(pilha)

if __name__ == "__main__":
    main()


#Exemplo de prática do LIFO(Last In First Out)

# LIFO (Último a Entrar, Primeiro a Sair) usando Pilha
class Pilha:
    def __init__(self):
        self.pilha = []
    
    def empurrar(self, item):
        self.pilha.append(item)
        print(f"Item empurrado: {item}")
    
    def remover(self):
        if self.esta_vazia():
            return "Pilha está vazia"
        return self.pilha.pop()
    
    def topo(self):
        if self.esta_vazia():
            return "Pilha está vazia"
        return self.pilha[-1]
    
    def esta_vazia(self):
        return len(self.pilha) == 0
    
    def tamanho(self):
        return len(self.pilha)


# Este programa simula uma Pilha (Stack) usando uma lista em Python.
# A Pilha opera no modo LIFO (Last In, First Out).

# 1. Inicializa a lista que funcionará como a nossa pilha
pilha = []
# Constante para controlar o loop do menu
EXECUTANDO = True

def exibir_menu():
    """Exibe as opções do menu para o usuário."""
    print("\n--- Menu da Pilha ---")
    print("1. Empilhar (Push): Adicionar um elemento.")
    print("2. Desempilhar (Pop): Remover o último elemento.")
    print("3. Exibir Pilha e Topo (Peek).")
    print("4. Sair.")
    print("----------------------")

def empilhar():
    """Adiciona um elemento ao topo da pilha (Push)."""
    item = input("Digite o item para empilhar: ")
    # O método 'append' da lista adiciona o item ao final, simulando o topo da pilha.
    pilha.append(item)
    print(f"'{item}' foi empilhado.")

def desempilhar():
    """Remove o elemento do topo da pilha (Pop)."""
    if not pilha:
        # Verifica se a pilha está vazia antes de tentar remover.
        print("Erro: A pilha está vazia! Nada para desempilhar.")
    else:
        # O método 'pop()' da lista remove e retorna o último elemento (o topo).
        item_removido = pilha.pop()
        print(f"'{item_removido}' foi desempilhado (removido do topo).")

def exibir_pilha_e_topo():
    """Exibe o estado atual da pilha e qual é o elemento do topo (Peek)."""
    print("\nEstado atual da Pilha:")
    
    if not pilha:
        print("[ Pilha vazia ]")
        print("Topo (Peek): Nenhum")
    else:
        # Exibe a pilha completa
        print(pilha)
        # O topo é sempre o último elemento da lista
        topo = pilha[-1]
        print(f"Topo (Peek): '{topo}'")

# --- Loop Principal do Programa (usando 'while') ---

while EXECUTANDO:
    exibir_menu()
    
    # Captura a escolha do usuário
    escolha = input("Escolha uma opção (1-4): ")
    
    if escolha == '1':
        empilhar()
    elif escolha == '2':
        desempilhar()
    elif escolha == '3':
        exibir_pilha_e_topo()
    elif escolha == '4':
        # Altera a variável de controle para sair do loop
        EXECUTANDO = False
        print("\nPrograma encerrado. Até mais!")
    else:
        print("Opção inválida. Tente novamente.")
