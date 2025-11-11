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
