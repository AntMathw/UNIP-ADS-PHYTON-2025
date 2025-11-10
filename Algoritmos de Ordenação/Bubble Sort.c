# Bubble sort

numeros = [5, 3, 8, 4, 2]

print('Vetor Original: ', numeros)

for i in range(len(numeros)-1):
    for j in range(len(numeros)-1-i):
        if numeros[j]>numeros[j+1]:
            numeros[j],numeros[j+1]=numeros[j+1],numeros[j]

print('Vetor ordenado: ', numeros)

# Bubble sort em DEF

def bubble_sort(lista):
    """
    Implementa o algoritmo Bubble Sort de forma simples.
    Ordena a lista em ordem crescente.
    """
    n = len(lista)

    
    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    # A função modifica a lista original (in-place)
    return lista


# --- Demonstração ---

# Lista desordenada para teste
numeros = [64, 34, 25, 12, 22, 11, 90]

print(f"Lista original: {numeros}")

# Chama a função para ordenar
lista_ordenada = bubble_sort(numeros)

print(f"Lista ordenada: {lista_ordenada}")

def merge_sort(lista):
    """
    Implementa o algoritmo de ordenação Merge Sort (Dividir e Conquistar).
    """
    # 1. CASO BASE (Parada da recursão)
    # Se a lista tiver 0 ou 1 elemento, ela já está ordenada.
    if len(lista) <= 1:
        return lista
    
    # 2. DIVIDIR (Divide a lista em duas metades)
    meio = len(lista) // 2
    metade_esquerda = lista[:meio]
    metade_direita = lista[meio:]
    
    # 3. CONQUISTAR (Chama o merge_sort recursivamente)
    # Recursão acontece aqui: ordena cada metade.
    metade_esquerda_ordenada = merge_sort(metade_esquerda)
    metade_direita_ordenada = merge_sort(metade_direita)
    
    # 4. COMBINAR/MERGE (Intercala as duas metades ordenadas)
    return merge(metade_esquerda_ordenada, metade_direita_ordenada)

def merge(esquerda, direita):
    """
    Função auxiliar que intercala (merge) duas listas já ordenadas.
    """
    resultado = []
    i = j = 0  # i para a lista esquerda, j para a lista direita
    
    # Enquanto houver elementos nas duas listas:
    while i < len(esquerda) and j < len(direita):
        # Compara os menores elementos das duas listas
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
            
    # Adiciona os elementos restantes (apenas um dos loops rodará)
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado

# --- EXEMPLO DE USO ---

dados_para_ordenar = [12, 11, 13, 5, 6, 7]

print(f"Lista original: {dados_para_ordenar}")

# Chamada principal do algoritmo
lista_ordenada = merge_sort(dados_para_ordenar)

print(f"Lista ordenada (Merge Sort): {lista_ordenada}")

# Outro exemplo
dados_grandes = [90, 45, 2, 78, 10, 50, 3, 22, 1]
print(f"\nLista grande original: {dados_grandes}")
print(f"Lista grande ordenada: {merge_sort(dados_grandes)}")

def bubble_sort(lista):
    n = len(lista)

    # Laço externo: Percorre todos os elementos da lista (n-1 vezes)
    for i in range(n):
        # Flag para otimização: se nenhuma troca ocorrer, a lista está ordenada
        troca_ocorre = False

        # Laço interno: Percorre a lista de 0 a n-i-1
        # O '-i' é porque os últimos 'i' elementos já estão ordenados e não precisam ser verificados
        for j in range(0, n - i - 1):
            
            # Comparação de elementos adjacentes
            if lista[j] > lista[j + 1]:
                # Troca de elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                troca_ocorre = True
        
        # Otimização: Se nenhuma troca ocorreu nesta passagem, a lista está ordenada
        if not troca_ocorre:
            break
    
    return lista

# Exemplo de uso:
dados = [64, 34, 25, 12, 22, 11, 90]
lista_ordenada = bubble_sort(dados)
print(f"Lista ordenada: {lista_ordenada}")
