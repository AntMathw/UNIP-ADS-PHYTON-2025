#Lista em formato de FILA com append, pop e del
#FIFO (First In First Out)

def main():

    fila = []
    print(f'Fila vazia {fila}') se

    fila.append(3)
    print(fila)
    fila.append(7)
    print(fila)
    fila.append(2)
    print(fila)
    fila.append(0)
    print(fila)
    fila.pop(0)
    print(fila)

    fila.append(11)

    del fila[0:4]
    print(f'Fila sem elementos {fila}')

if __name__ == "__main__":
    main()

# Inicializando a Fila
fila = []

# --- 1. ENQUEUE (Enfileirar) ---
# Adiciona elementos no final da fila
print("--- Enfileirando (Adicionando) ---")
fila.append("João")
print(f"Fila atual: {fila}") # ['João']

fila.append("Maria")
print(f"Fila atual: {fila}") # ['João', 'Maria']

fila.append("Pedro")
print(f"Fila atual: {fila}") # ['João', 'Maria', 'Pedro']

# --- 2. DEQUEUE (Desenfileirar) ---
# Remove o elemento do INÍCIO da fila (FIFO)

print("\n--- Desenfileirando (Removendo) ---")
proximo_a_ser_atendido = fila.pop(0) # pop(0) remove o primeiro elemento
print(f"Pessoa atendida (saiu da fila): {proximo_a_ser_atendido}") # João
print(f"Fila atual: {fila}") # ['Maria', 'Pedro']

proximo_a_ser_atendido = fila.pop(0)
print(f"Pessoa atendida (saiu da fila): {proximo_a_ser_atendido}") # Maria
print(f"Fila atual: {fila}") # ['Pedro']

# --- 3. PEEK (Verificar o Próximo) ---
# Vê o próximo elemento sem removê-lo
print("\n--- Verificando o Próximo (Peek) ---")
if fila:
    proximo_na_frente = fila[0]
    print(f"Próximo na fila para ser atendido: {proximo_na_frente}") # Pedro
print(f"Fila atual: {fila}") # ['Pedro'] (Não foi removido)

from collections import deque

# 1. Criação da Fila
# 'deque' é uma lista otimizada para inserção e remoção rápida em ambas as extremidades.
fila_de_pedidos = deque()

print(f"Fila inicial criada: {list(fila_de_pedidos)}")
print("-" * 30)

# 2. Adicionando itens na Fila (Enqueue - Adicionar à direita/final)
print("📦 Adicionando pedidos...")
fila_de_pedidos.append("Pedido 1: Café Expresso")
fila_de_pedidos.append("Pedido 2: Latte")
fila_de_pedidos.append("Pedido 3: Cappuccino")

print(f"Fila após adições: {list(fila_de_pedidos)}")
print("-" * 30)

# 3. Verificando o tamanho
print(f"Tamanho atual da fila: **{len(fila_de_pedidos)}**")
print("-" * 30)

# 4. Removendo itens da Fila (Dequeue - Remover da esquerda/início - FIFO)
print("✅ Processando pedidos (FIFO - First In, First Out)...")

# O primeiro item a entrar na fila é o primeiro a ser removido
pedido_processado = fila_de_pedidos.popleft() 
print(f"Pedido processado: **{pedido_processado}**")

pedido_processado = fila_de_pedidos.popleft()
print(f"Pedido processado: **{pedido_processado}**")

print(f"Fila após processamento: {list(fila_de_pedidos)}")
print("-" * 30)

# 5. Adicionando mais um item para demonstrar o funcionamento contínuo
fila_de_pedidos.append("Pedido 4: Chá Gelado")
print(f"Fila atualizada: {list(fila_de_pedidos)}")

# 6. Processando o item restante
if fila_de_pedidos:
    pedido_processado = fila_de_pedidos.popleft()
    print(f"Pedido processado: **{pedido_processado}**")
    
if fila_de_pedidos:
    pedido_processado = fila_de_pedidos.popleft()
    print(f"Pedido processado: **{pedido_processado}**")

print(f"Fila no final: {list(fila_de_pedidos)}")

from collections import deque

class FilaDeAtendimento:
    def __init__(self):
        # Inicializa a fila usando deque para alta performance
        self.fila = deque()

    def entrar(self, nome):
        """Adiciona uma pessoa ao final da fila (Enqueue)"""
        self.fila.append(nome)
        print(f"-> {nome} entrou na fila.")

    def atender(self):
        """Remove e retorna a primeira pessoa da fila (Dequeue)"""
        if not self.esta_vazia():
            pessoa = self.fila.popleft() # popleft remove do início
            print(f"✅ Atendendo agora: {pessoa}")
            return pessoa
        else:
            print("⚠️ A fila está vazia! Ninguém para atender.")
            return None

    def proximo_da_vez(self):
        """Mostra quem é o primeiro sem remover (Peek)"""
        if not self.esta_vazia():
            return self.fila[0]
        return "Ninguém"

    def tamanho(self):
        """Retorna o número de pessoas na fila"""
        return len(self.fila)

    def esta_vazia(self):
        """Verifica se a fila está vazia"""
        return len(self.fila) == 0

    def mostrar_fila(self):
        """Exibe o estado atual da fila"""
        print(f"📋 Fila atual: {list(self.fila)}")

# --- Testando o Programa ---

if __name__ == "__main__":
    # 1. Criar a fila
    minha_fila = FilaDeAtendimento()
    print("--- Início do Expediente ---\n")

    # 2. Pessoas chegando (Enqueue)
    minha_fila.entrar("Ana")
    minha_fila.entrar("Carlos")
    minha_fila.entrar("Beatriz")
    
    print()
    minha_fila.mostrar_fila()
    print(f"Total na fila: {minha_fila.tamanho()}")
    print("-" * 30)

    # 3. Atendendo o primeiro (Dequeue - deve ser a Ana)
    minha_fila.atender()
    
    # 4. Verificando quem é o próximo
    print(f"O próximo da vez é: {minha_fila.proximo_da_vez()}")
    print("-" * 30)

    # 5. Atendendo o restante
    minha_fila.atender()
    minha_fila.atender()
    
    # 6. Tentando atender com fila vazia
    minha_fila.atender()

from collections import deque

class FilaFIFO:
    def __init__(self):
        # Inicializa a fila usando deque para alta performance
        self._dados = deque()

    def entrar(self, item):
        """Adiciona um item ao final da fila (Enqueue)"""
        self._dados.append(item)
        print(f"Entrou: {item}")

    def sair(self):
        """Remove e retorna o item do início da fila (Dequeue)"""
        if self.vazia():
            return "A fila está vazia!"
        
        item = self._dados.popleft() # popleft é o segredo do FIFO eficiente
        print(f"Saiu: {item}")
        return item

    def ver_primeiro(self):
        """Olha o primeiro da fila sem remover (Peek)"""
        if self.vazia():
            return None
        return self._dados[0]

    def vazia(self):
        """Verifica se a fila está vazia"""
        return len(self._dados) == 0

    def tamanho(self):
        """Retorna o tamanho da fila"""
        return len(self._dados)

    def __str__(self):
        return f"Estado atual da fila: {list(self._dados)}"

# --- Testando a Fila ---

# 1. Criar a fila
minha_fila = FilaFIFO()

# 2. Adicionar elementos (O primeiro é "Documento A")
minha_fila.entrar("Documento A")
minha_fila.entrar("Documento B")
minha_fila.entrar("Documento C")

print("-" * 20)
print(minha_fila) # Mostra: ['Documento A', 'Documento B', 'Documento C']
print("-" * 20)

# 3. Remover elementos (Deve remover "Documento A" primeiro)
minha_fila.sair() 
print(minha_fila) # Mostra: ['Documento B', 'Documento C']

# 4. Verificar o próximo
print(f"Próximo da fila: {minha_fila.ver_primeiro()}")