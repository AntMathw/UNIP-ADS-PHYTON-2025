# Arquivo: manipulacao_string.py

# 1. Definição da String Base
texto_original = "Python é Incrível para manipulação de texto e dados."
print("--- String Original ---")
print(f"Texto: {texto_original}\n")

# 2. Obter o Comprimento (Tamanho) da String
comprimento = len(texto_original)
print("1. Comprimento da String:")
print(f"O texto tem {comprimento} caracteres.\n")

# 3. Conversão de Caixa (Maiúsculas e Minúsculas)
texto_maiusculo = texto_original.upper()
texto_minusculo = texto_original.lower()

print("2. Conversão de Caixa:")
print(f"Maiúsculas: {texto_maiusculo}")
print(f"Minúsculas: {texto_minusculo}\n")

# 4. Busca e Substituição de Substrings
# Substitui todas as ocorrências de "texto" por "strings"
texto_substituido = texto_original.replace("texto", "strings")

print("3. Substituição de Palavras:")
print(f"Após a substituição: {texto_substituido}\n")

# 5. Fatiamento (Slicing) - Pegando partes da String
# Pegar os primeiros 6 caracteres (do índice 0 até o 6, exclusivo)
primeira_palavra = texto_original[0:6] 
# Pegar a partir do 18º caractere até o final
resto_da_frase = texto_original[18:] 

print("4. Fatiamento (Slicing):")
print(f"Primeira palavra: '{primeira_palavra}'")
print(f"Resto da frase (a partir do índice 18): '{resto_da_frase}'\n")

# 6. Verificação de Conteúdo
# Verifica se a string começa ou termina com uma substring
comeca_com_python = texto_original.startswith("Python")
termina_com_dados = texto_original.endswith("dados.")

print("5. Verificação de Início/Fim:")
print(f"Começa com 'Python'? {comeca_com_python}")
print(f"Termina com 'dados.'? {termina_com_dados}\n")

# 7. Concatenação (Juntar Strings)
parte1 = "Aprendendo "
parte2 = "manipulação de strings "
parte3 = "em Python!"
texto_concatenado = parte1 + parte2 + parte3

print("6. Concatenação de Strings:")
print(f"Resultado: {texto_concatenado}")

