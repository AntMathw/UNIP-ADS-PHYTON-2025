class Carteira:
    def __init__(self, proprietario, saldo_inicial=0):
        # Atributos (Características)
        self.proprietario = proprietario
        self.saldo = saldo_inicial
        self.cartoes = []

    # Métodos (Ações)
    def adicionar_dinheiro(self, valor):
        self.saldo += valor
        print(f"R$ {valor} adicionados! Novo saldo: R$ {self.saldo}")

    def pagar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Pagamento de R$ {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o pagamento.")

    def adicionar_cartao(self, nome_cartao):
        self.cartoes.append(nome_cartao)
        print(f"Cartão '{nome_cartao}' guardado na carteira.")

    def resumo(self):
        print(f"\n--- Carteira de {self.proprietario} ---")
        print(f"Saldo atual: R$ {self.saldo}")
        print(f"Cartões: {', '.join(self.cartoes) if self.cartoes else 'Nenhum'}")

# --- Usando o objeto na prática ---

# 1. Criamos (instanciamos) o objeto
minha_carteira = Carteira("Alex", 50.00)

# 2. Chamamos os métodos
minha_carteira.adicionar_cartao("Visa Débito")
minha_carteira.adicionar_dinheiro(100)
minha_carteira.pagar(30)
minha_carteira.resumo()