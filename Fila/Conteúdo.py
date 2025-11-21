#Lista em formato de FILA com append, pop e del
#FIFO (First In First Out)

def main():

    fila = []
    print(f'Fila vazia {fila}')

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
