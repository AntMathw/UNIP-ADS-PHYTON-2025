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

## Dados a serem escritos no arquivo
dados_para_escrever = [
    "ID:101;Nome:Alice;Cidade:Sao Paulo",
    "ID:102;Nome:Bruno;Cidade:Rio de Janeiro",
    "ID:103;Nome:Carla;Cidade:Belo Horizonte"
]
nome_arquivo = 'dados_processamento.txt'

# --- 1. MANIPULAÇÃO DE ARQUIVOS: Escrita/Criação (Modo 'w') ---
print("### 1. ESCREVENDO NO ARQUIVO ###")
try:
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for linha in dados_para_escrever:
            # Escreve cada item de dados_para_escrever, adicionando uma quebra de linha
            arquivo.write(linha + '\n')
    print(f"✅ Arquivo '{nome_arquivo}' criado e escrito com sucesso.\n")
except IOError as e:
    print(f"❌ Erro ao escrever no arquivo: {e}")
    # Encerra o script se a escrita falhar
    exit()

# --- 2. MANIPULAÇÃO DE ARQUIVOS E STRINGS: Leitura e Processamento ---
print("### 2. LENDO E PROCESSANDO STRINGS DO ARQUIVO ###")
print("-" * 40)
print(f"{'ID':<5} | {'NOME EM MAIÚSCULAS':<25} | {'CIDADE PROCESSADA':<20}")
print("-" * 40)

try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        
        # Leitura linha por linha (ideal para arquivos grandes)
        for linha_bruta in arquivo:
            # --- Manipulação de Strings 1: Limpeza ---
            # Remove quebras de linha e espaços em branco desnecessários
            linha_limpa = linha_bruta.strip() 
            
            # Pula linhas vazias, se houver
            if not linha_limpa:
                continue
                
            # --- Manipulação de Strings 2: Divisão (split) ---
            # Divide a linha em partes usando o ';' como delimitador
            campos = linha_limpa.split(';')

            dados_processados = {}
            for campo in campos:
                # Divide cada campo em chave e valor usando ':'
                chave_valor = campo.split(':')
                if len(chave_valor) == 2:
                    chave = chave_valor[0]
                    valor = chave_valor[1]
                    dados_processados[chave] = valor.strip()
            
            # --- Manipulação de Strings 3: Uso de Métodos e f-Strings ---
            if 'ID' in dados_processados and 'Nome' in dados_processados and 'Cidade' in dados_processados:
                
                # Aplica o método .upper() ao nome
                nome_maiusculo = dados_processados['Nome'].upper()
                
                # Exemplo de f-string para formatar a saída
                saida_formatada = f"{dados_processados['ID']:<5} | {nome_maiusculo:<25} | {dados_processados['Cidade']:<20}"
                
                print(saida_formatada)

    print("-" * 40)
    print("\n✅ Processamento concluído.")
    
except FileNotFoundError:
    print(f"\n❌ Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
except IOError as e:
    print(f"\n❌ Erro ao ler o arquivo: {e}")
