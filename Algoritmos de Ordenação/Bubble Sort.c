# Bubble sort

numeros = [5, 3, 8, 4, 2]

print('Vetor Original: ', numeros)

for i in range(len(numeros)-1):
    for j in range(len(numeros)-1-i):
        if numeros[j]>numeros[j+1]:
            numeros[j],numeros[j+1]=numeros[j+1],numeros[j]

print('Vetor ordenado: ', numeros)

