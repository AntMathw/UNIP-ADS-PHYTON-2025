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
