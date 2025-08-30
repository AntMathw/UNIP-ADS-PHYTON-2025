# Dicionário que vai guardar os produtos e suas quantidades
estoque = {}

def entrada(produto, quantidade):

    if produto in estoque:
        estoque[produto] += quantidade
    else:
        estoque[produto] = quantidade
    print(f"Entrada: {quantidade}x {produto} (Total: {estoque[produto]})")

def saida(produto, quantidade):

    if produto in estoque and estoque[produto] >= quantidade:
        estoque[produto] -= quantidade
        print(f"Saída: {quantidade}x {produto} (Restante: {estoque[produto]})")
    else:
        print(f"Erro: estoque insuficiente de {produto}!")

def mostrar_estoque():
    """Mostra todos os produtos e quantidades"""
    print("\n📦 Estoque atual:")
    if not estoque:
        print("Vazio")
    else:
        for produto, qtd in estoque.items():
            print(f"- {produto}: {qtd}")


while True:
    print("\n1 - Entrada de produto")
    print("2 - Saída de produto")
    print("3 - Mostrar estoque")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        qtd = int(input("Quantidade: "))
        entrada(nome, qtd)
    elif opcao == "2":
        nome = input("Nome do produto: ")
        qtd = int(input("Quantidade: "))
        saida(nome, qtd)
    elif opcao == "3":
        mostrar_estoque()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
