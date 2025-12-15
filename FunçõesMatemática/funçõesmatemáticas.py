#Tipos primitivos see

valor = float(input('Digite um valor: '))
n = float(input('Digite um valor real: '))

soma = valor + n
print('A some entre {} e {} é {}'.format(valor, n, soma))

valor2 = float(input('Digite um numero real: '))
n2 = float(input('Digite outro valor: '))

divisão = valor2 / n2

print('A divisão entre {} e {} é {}'.format(valor2, n2, divisão))

num1 = float(input('Digite um valor real: '))
num2 = float(input('Digite outro numero real: '))

multiplicação = num1 * num2

print('A multiplicação entre {} e {} é {}'.format(num1, num2, multiplicação))


#Operaores Artiméticos

num = int(input('Digite um valor: '))
num2 = 2

valor = num + 2
valor2 = num - 2
valor3 = num * 2
valor4 = num / 2
valor5 = num ** 2
valor6 = num // 2
valor7 = num % 2

print('Os valores são \n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(valor, valor2, valor3, valor4, valor5, valor6, valor7))

#TODOS OS TIPOS PRIMITIVOS

# ----------------------------------------------------
# 1. Tipos Numéricos (Numéricos)
# ----------------------------------------------------

# Inteiro (int): Números inteiros positivos, negativos ou zero.
idade = 30
print(f"1. Inteiro (int): {idade} (Tipo: {type(idade)})")

# Ponto Flutuante (float): Números reais com casas decimais.
preco_produto = 49.99
print(f"2. Ponto Flutuante (float): {preco_produto} (Tipo: {type(preco_produto)})")

# Número Complexo (complex): Números na forma a + bj.
coordenada_z = 3 + 4j
print(f"3. Número Complexo (complex): {coordenada_z} (Tipo: {type(coordenada_z)})")

print("-" * 30)

# ----------------------------------------------------
# 2. Tipo Booleano (bool)
# ----------------------------------------------------

# Booleano (bool): Representa valores de verdade: True (Verdadeiro) ou False (Falso).
esta_ativo = True
print(f"4. Booleano (bool): {esta_ativo} (Tipo: {type(esta_ativo)})")

print("-" * 30)

# ----------------------------------------------------
# 3. Tipo Sequência (str)
# ----------------------------------------------------

# String (str): Sequência imutável de caracteres (texto).
nome_usuario = "Engenharia de Software Ágil"
print(f"5. String (str): '{nome_usuario}' (Tipo: {type(nome_usuario)})")

print("-" * 30)

# ----------------------------------------------------
# 4. Tipos de Coleção (Estruturas de Dados Fundamentais)
# Nota: Embora não sejam 'primitivos' em todas as linguagens,
# são essenciais em Python.
# ----------------------------------------------------

# Lista (list): Coleção ordenada, mutável (pode ser alterada) e que permite duplicatas.
lista_habilidades = ["Python", "Scrum", 3, "TDD"]
print(f"6. Lista (list): {lista_habilidades} (Tipo: {type(lista_habilidades)})")

# Tupla (tuple): Coleção ordenada, IMUTÁVEL (não pode ser alterada) e que permite duplicatas.
coordenadas = (10.5, 20.3)
print(f"7. Tupla (tuple): {coordenadas} (Tipo: {type(coordenadas)})")

# Conjunto (set): Coleção não ordenada, mutável e que NÃO permite elementos duplicados.
tecnologias_unicas = {"Python", "Java", "Scrum", "Python"} # "Python" só aparecerá uma vez
print(f"8. Conjunto (set): {tecnologias_unicas} (Tipo: {type(tecnologias_unicas)})")

# Dicionário (dict): Coleção não ordenada de pares chave-valor. Mutável.
dados_projeto = {
    "id": 101,
    "status": "Em andamento",
    "prioridade": "Alta"
}
print(f"9. Dicionário (dict): {dados_projeto} (Tipo: {type(dados_projeto)})")

print("-" * 30)

# ----------------------------------------------------
# 5. Outro Tipo Básico
# ----------------------------------------------------

# NoneType (None): Um tipo especial que representa a ausência de valor.
valor_nulo = None
print(f"10. Ausência de Valor (NoneType): {valor_nulo} (Tipo: {type(valor_nulo)})")

import math

def calcular_volume_esfera(raio: float) -> float:
    """
    Calcula o volume de uma esfera dado o seu raio.

    Args:
        raio (float): O raio da esfera. Deve ser um número não negativo.

    Returns:
        float: O volume da esfera.
    """
    
    # 1. Checagem de valor de entrada (opcional, mas boa prática)
    if raio < 0:
        raise ValueError("O raio deve ser um número não negativo.")

    # 2. Implementação da fórmula: (4/3) * pi * r^3
    # math.pi fornece o valor de Pi
    # O operador ** é usado para potenciação (r**3 = r³)
    
    volume = (4 / 3) * math.pi * (raio ** 3)
    
    return volume

# --- Exemplos de Uso ---

# Exemplo 1: Raio = 5
raio_1 = 5
volume_1 = calcular_volume_esfera(raio_1)
print(f"O volume de uma esfera com raio {raio_1} é **{volume_1:.2f}**") # Resultado arredondado para 2 casas decimais

# Exemplo 2: Raio = 10
raio_2 = 10
volume_2 = calcular_volume_esfera(raio_2)
print(f"O volume de uma esfera com raio {raio_2} é **{volume_2:.2f}**")

# Exemplo 3: Raio = 1.5
raio_3 = 1.5
volume_3 = calcular_volume_esfera(raio_3)
print(f"O volume de uma esfera com raio {raio_3} é **{volume_3:.2f}**")

import math

numero = 49
resultado = math.sqrt(numero)

print(f"A raiz quadrada de {numero} é {resultado}")

def soma_flexivel(*numeros, fator_escala=1):
    """
    Calcula a soma de uma quantidade arbitrária de números e
    multiplica o resultado por um fator de escala opcional.

    Args:
        *numeros (float ou int): Os números que serão somados.
        fator_escala (float ou int, opcional): Fator para multiplicar
                                                o resultado final. Padrão é 1.

    Returns:
        float: O resultado da soma multiplicado pelo fator de escala.
    """
    # 1. Verificar se há números para somar
    if not numeros:
        return 0

    # 2. Calcular a soma de todos os números
    soma_total = sum(numeros)

    # 3. Aplicar o fator de escala (multiplicação)
    resultado_final = soma_total * fator_escala

    return resultado_final

# --- Exemplos de Uso ---

# Exemplo 1: Soma de 3 números simples (fator padrão = 1)
print("--- Exemplo 1 ---")
resultado1 = soma_flexivel(5, 10, 2)
print(f"Soma de (5, 10, 2): {resultado1}")
# Saída esperada: 17

# Exemplo 2: Soma de 5 números com fator de escala 2
print("\n--- Exemplo 2 ---")
resultado2 = soma_flexivel(1, 2, 3, 4, 5, fator_escala=2)
# Soma (1+2+3+4+5) = 15. Multiplica por 2 = 30
print(f"Soma de (1, 2, 3, 4, 5) * 2: {resultado2}")
# Saída esperada: 30

# Exemplo 3: Soma de números com vírgula (floats) e fator de escala decimal
print("\n--- Exemplo 3 ---")
resultado3 = soma_flexivel(0.5, 1.5, 3.0, fator_escala=1.1)
# Soma (0.5+1.5+3.0) = 5.0. Multiplica por 1.1 = 5.5
print(f"Soma de (0.5, 1.5, 3.0) * 1.1: {resultado3}")
# Saída esperada: 5.5

# Exemplo 4: Chamada sem argumentos (retorna 0)
print("\n--- Exemplo 4 ---")
resultado4 = soma_flexivel()
print(f"Soma sem números: {resultado4}")
# Saída esperada: 0