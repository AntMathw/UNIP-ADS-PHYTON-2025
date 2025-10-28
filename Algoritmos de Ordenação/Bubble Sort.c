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
