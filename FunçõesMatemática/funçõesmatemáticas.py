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

# -*- coding: utf-8 -*-

class SubtratorComplexo:
    """
    Implementa um algoritmo customizado para subtrair dois números inteiros
    positivos representados como strings, simulando a operação "dígito por dígito"
    com lógica de empréstimo (borrow).
    """

    def _valida_entrada(self, num_str):
        """Valida se a string contém apenas dígitos."""
        if not num_str.isdigit():
            raise ValueError(f"O valor '{num_str}' deve conter apenas dígitos numéricos.")
        return num_str.lstrip('0') or '0'

    def _subtrair_logica(self, maior_str, menor_str):
        """
        Executa a subtração dígito por dígito (maior - menor).
        Ambos os números são garantidos como positivos e o maior já está na frente.
        """
        resultado = []
        emprestimo = 0 # O borrow
        
        # Inverte as strings para iterar dos dígitos menos significativos (unidades)
        maior_rev = maior_str[::-1]
        menor_rev = menor_str[::-1]
        
        len_maior = len(maior_str)
        len_menor = len(menor_str)

        for i in range(len_maior):
            # Obtém o dígito atual do número maior e subtrai o empréstimo
            digito_maior = int(maior_rev[i]) - emprestimo
            
            # Obtém o dígito do número menor (ou 0 se o menor já terminou)
            digito_menor = int(menor_rev[i]) if i < len_menor else 0
            
            # Reseta o empréstimo para a próxima iteração
            emprestimo = 0

            # Verifica se é necessário um empréstimo
            if digito_maior < digito_menor:
                emprestimo = 1
                # Empréstimo: adiciona 10 ao dígito atual
                digito_maior += 10
            
            # Calcula o resultado do dígito e adiciona à lista
            diferenca = digito_maior - digito_menor
            resultado.append(str(diferenca))

        # Reverte o resultado e remove zeros à esquerda
        resultado_final = "".join(resultado[::-1]).lstrip('0')
        
        # Se o resultado for uma string vazia (ex: 10 - 10), retorna "0"
        return resultado_final or "0"

    def subtrair(self, num1_str, num2_str):
        """
        Função principal que gerencia a subtração, validando entradas e magnitudes.
        """
        print(f"\n--- Processando Subtração Complexa ---")
        
        try:
            # 1. Validação e remoção de zeros à esquerda
            val1 = self._valida_entrada(num1_str)
            val2 = self._valida_entrada(num2_str)
            
            # 2. Converte para inteiro (apenas para comparação de magnitude)
            num1 = int(val1)
            num2 = int(val2)
            
            # 3. Determina a magnitude e o sinal
            e_negativo = False
            
            if num1 >= num2:
                maior_str = val1
                menor_str = val2
            else:
                maior_str = val2
                menor_str = val1
                e_negativo = True # O resultado deve ser negativo
                
            # 4. Executa a lógica de subtração customizada
            resultado = self._subtrair_logica(maior_str, menor_str)
            
            # 5. Adiciona o sinal se necessário
            if e_negativo and resultado != '0':
                resultado = "-" + resultado
            
            return resultado

        except ValueError as e:
            return f"ERRO na entrada: {e}"
        except Exception as e:
            return f"ERRO inesperado: {e}"

# --- Exemplo de Uso ---

def main():
    subtrator = SubtratorComplexo()
    
    # Exemplo 1: Subtração padrão
    n1_ex1 = "987654321"
    n2_ex1 = "123456789"
    res1 = subtrator.subtrair(n1_ex1, n2_ex1)
    print(f"Subtração: {n1_ex1} - {n2_ex1} = {res1}")

    # Exemplo 2: O resultado é negativo (o algoritmo inverte e adiciona o sinal)
    n1_ex2 = "100"
    n2_ex2 = "1000"
    res2 = subtrator.subtrair(n1_ex2, n2_ex2)
    print(f"Subtração: {n1_ex2} - {n2_ex2} = {res2}")
    
    # Exemplo 3: Subtração com múltiplos empréstimos
    n1_ex3 = "100000"
    n2_ex3 = "1"
    res3 = subtrator.subtrair(n1_ex3, n2_ex3)
    print(f"Subtração: {n1_ex3} - {n2_ex3} = {res3}")
    
    # Exemplo 4: Entrada com erro (não-dígitos)
    n1_ex4 = "123A"
    n2_ex4 = "100"
    res4 = subtrator.subtrair(n1_ex4, n2_ex4)
    print(f"Subtração: {n1_ex4} - {n2_ex4} = {res4}")

# Ponto de entrada
if __name__ == "__main__":
    main()

class SomadorComplexo:
    """
    Implementa um algoritmo customizado para somar dois números inteiros
    positivos representados como strings, simulando a operação "dígito por dígito"
    com lógica de transporte (carry).
    """

    def _valida_entrada(self, num_str):
        """Valida se a string contém apenas dígitos."""
        if not num_str.isdigit():
            raise ValueError(f"O valor '{num_str}' deve conter apenas dígitos numéricos.")
        # Retorna a string sem zeros à esquerda, ou '0' se for zero puro
        return num_str.lstrip('0') or '0'

    def _somar_logica(self, num1_str, num2_str):
        """
        Executa a adição dígito por dígito, gerenciando o carry (vai um).
        """
        resultado = []
        transporte = 0  # O carry (vai um)
        
        # Inverte as strings para iterar dos dígitos menos significativos (unidades)
        n1_rev = num1_str[::-1]
        n2_rev = num2_str[::-1]
        
        len_n1 = len(num1_str)
        len_n2 = len(num2_str)
        max_len = max(len_n1, len_n2)

        for i in range(max_len):
            # Obtém o dígito atual de num1 (ou 0 se num1 for mais curto)
            digito1 = int(n1_rev[i]) if i < len_n1 else 0
            
            # Obtém o dígito atual de num2 (ou 0 se num2 for mais curto)
            digito2 = int(n2_rev[i]) if i < len_n2 else 0
            
            # Soma os dígitos atuais mais o transporte anterior
            soma = digito1 + digito2 + transporte
            
            # O novo dígito do resultado é o resto da divisão por 10
            novo_digito = soma % 10
            
            # O novo transporte (carry) é o quociente da divisão por 10
            transporte = soma // 10
            
            # Adiciona o novo dígito à lista de resultados
            resultado.append(str(novo_digito))

        # Se houver um transporte restante após o último loop (ex: 99 + 1 = 100)
        if transporte > 0:
            resultado.append(str(transporte))

        # Reverte o resultado para a ordem correta
        resultado_final = "".join(resultado[::-1])
        
        # Como as entradas são validadas como positivas, não precisamos nos preocupar com zeros à esquerda no final,
        # a menos que ambos os números fossem "0", mas '0' é garantido.
        return resultado_final

    def somar(self, num1_str, num2_str):
        """
        Função principal que gerencia a adição, validando entradas.
        """
        print(f"\n--- Processando Adição Complexa ---")
        
        try:
            # 1. Validação e remoção de zeros à esquerda
            val1 = self._valida_entrada(num1_str)
            val2 = self._valida_entrada(num2_str)
            
            # 2. Executa a lógica de adição customizada
            resultado = self._somar_logica(val1, val2)
            
            return resultado

        except ValueError as e:
            return f"ERRO na entrada: {e}"
        except Exception as e:
            return f"ERRO inesperado: {e}"

# --- Exemplo de Uso ---

def main():
    somador = SomadorComplexo()
    
    # Exemplo 1: Adição simples
    n1_ex1 = "12345"
    n2_ex1 = "6789"
    res1 = somador.somar(n1_ex1, n2_ex1)
    print(f"Adição: {n1_ex1} + {n2_ex1} = {res1}")

    # Exemplo 2: Adição com carry (vai um) na última posição
    n1_ex2 = "99"
    n2_ex2 = "1"
    res2 = somador.somar(n1_ex2, n2_ex2)
    print(f"Adição: {n1_ex2} + {n2_ex2} = {res2}")
    
    # Exemplo 3: Adição de números muito grandes (demonstrando precisão)
    n1_ex3 = "1234567890123456789012345"
    n2_ex3 = "9876543210987654321098765"
    res3 = somador.somar(n1_ex3, n2_ex3)
    print(f"Adição: {n1_ex3} + {n2_ex3} = {res3}")
    
    # Exemplo 4: Entrada com erro (não-dígitos)
    n1_ex4 = "456B"
    n2_ex4 = "100"
    res4 = somador.somar(n1_ex4, n2_ex4)
    print(f"Adição: {n1_ex4} + {n2_ex4} = {res4}")

# Ponto de entrada
if __name__ == "__main__":
    main()

import math

# Definindo o número
numero = 49

# Calculando a raiz
resultado = math.sqrt(numero)

print(f"A raiz quadrada de {numero} é {resultado}")