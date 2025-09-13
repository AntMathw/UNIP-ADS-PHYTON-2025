import json

def main():
    """
    Cria uma lista de dicionários e a salva em um arquivo JSON.
    """
    # 1. Criar a lista
    # Esta lista é composta por dicionários, que são ideais para representar
    # objetos com pares de chave-valor.
    pessoas = [
        {"nome": "Maria", "idade": 30, "cidade": "São Paulo"},
        {"nome": "João", "idade": 25, "cidade": "Rio de Janeiro"},
        {"nome": "Ana", "idade": 35, "cidade": "Belo Horizonte"}
    ]

    # 2. Exportar a lista para um arquivo JSON
    # 'w' significa 'write' (escrever) e 'json.dump' converte a lista para JSON
    # e a escreve no arquivo. O 'indent' deixa o arquivo JSON mais legível.
    nome_arquivo = "pessoas.json"
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
        json.dump(pessoas, arquivo_json, indent=4, ensure_ascii=False)
    
    print(f"Lista exportada com sucesso para '{nome_arquivo}'.")

# 3. Chamar a função main
# Esta estrutura garante que a função 'main' seja executada apenas
# quando o script é chamado diretamente.
if __name__ == "__main__":
    main()