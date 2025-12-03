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

#Exemplo de PILHA

# A lista 'minha_pilha' funcionará como nossa estrutura de pilha.
# O "topo" da pilha é o final da lista.
minha_pilha = []

# -----------------------------------------------------------------
# 1. Operação PUSH (Empilhar/Adicionar)
# Usamos o método append() para adicionar um item no topo da pilha.
# -----------------------------------------------------------------
print("--- PUSH (Adicionar) ---")
minha_pilha.append("Página 1: Início")
print(f"Pilha: {minha_pilha}")

minha_pilha.append("Página 2: Produtos")
print(f"Pilha: {minha_pilha}")

minha_pilha.append("Página 3: Checkout")
# "Página 3" é o último a entrar, está no TOPO da pilha.
print(f"Pilha: {minha_pilha}")

print("-" * 30)

# -----------------------------------------------------------------
# 2. Operação PEEK (Espiar/Ver o Topo)
# Vê o elemento do topo sem removê-lo.
# -----------------------------------------------------------------
if minha_pilha:
    topo_atual = minha_pilha[-1] # Acessa o último elemento (o topo)
    print(f"Elemento no Topo (PEEK): {topo_atual}")
    print(f"Pilha APÓS PEEK: {minha_pilha}") # O tamanho da pilha não mudou

print("-" * 30)

# -----------------------------------------------------------------
# 3. Operação POP (Desempilhar/Remover)
# Usamos o método pop() para remover e retornar o item do topo (LIFO).
# -----------------------------------------------------------------
print("--- POP (Remover) ---")
if minha_pilha:
    # Remove e retorna o último elemento adicionado ("Página 3")
    item_removido = minha_pilha.pop()
    print(f"POP: Removido '{item_removido}'. (Voltando para a página anterior)")
    print(f"Pilha atual: {minha_pilha}")

if minha_pilha:
    # Remove e retorna o novo elemento do topo ("Página 2")
    item_removido = minha_pilha.pop()
    print(f"POP: Removido '{item_removido}'. (Voltando para a página anterior)")
    print(f"Pilha atual: {minha_pilha}")

print("-" * 30)

# -----------------------------------------------------------------
# 4. Verificação de Pilha Vazia (isEmpty)
# -----------------------------------------------------------------
# A pilha está vazia?
print(f"A pilha está vazia? {'Sim' if not minha_pilha else 'Não'}")

# Esvaziando o último item
if minha_pilha:
    minha_pilha.pop()
    print(f"Pilha após esvaziar: {minha_pilha}")

print(f"A pilha está vazia? {'Sim' if not minha_pilha else 'Não'}")

# 1. Criação da Pilha como uma Lista
pilha = []

# 2. Operação PUSH (Empilhar): Adicionando elementos
print("--- PUSH (Empilhar) ---")
pilha.append(10)
pilha.append(20)
pilha.append(30)
print(f"Pilha atual após PUSH: {pilha}")  # Saída: [10, 20, 30]

# 3. Operação PEEK (Ver o Topo): Acessando o último elemento
if pilha:
    topo = pilha[-1]
    print(f"\n--- PEEK (Ver Topo) ---")
    print(f"Elemento no topo (sem remover): {topo}") # Saída: 30
    print(f"Pilha após PEEK: {pilha}") # Saída: [10, 20, 30]

# 4. Operação POP (Desempilhar): Removendo elementos
print(f"\n--- POP (Desempilhar) ---")
item_removido_1 = pilha.pop()
print(f"Item removido (POP): {item_removido_1}") # Saída: 30
print(f"Pilha atual: {pilha}") # Saída: [10, 20]

item_removido_2 = pilha.pop()
print(f"Item removido (POP): {item_removido_2}") # Saída: 20
print(f"Pilha atual: {pilha}") # Saída: [10]

# 5. Operação IS EMPTY (Verificar se está vazia)
print(f"\n--- IS EMPTY (Verificar Vazia) ---")
print(f"A pilha está vazia? {len(pilha) == 0}") # Saída: False

pilha.pop() # Remove o último elemento (10)
print(f"Pilha após último POP: {pilha}") # Saída: []
print(f"A pilha está vazia? {len(pilha) == 0}") # Saída: True

# Tentar POP em uma pilha vazia causará um erro (IndexError)
# item_errado = pilha.pop()
