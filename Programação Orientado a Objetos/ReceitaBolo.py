class Ingrediente:
    """
    Representa um ingrediente com nome e quantidade.
    Princípio POO: Encapsulamento de dados simples.
    """
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def __str__(self):
        """Método chamado ao usar print() no objeto Ingrediente."""
        return f"- {self.quantidade} de {self.nome}"

class ReceitaDeBolo:
    """
    Representa a receita completa de um bolo, gerenciando seus ingredientes e etapas.
    Princípio POO: Modelagem de um objeto complexo (a receita) com seus próprios
    dados (ingredientes) e comportamentos (métodos).
    """
    def __init__(self, nome_do_bolo):
        self.nome = nome_do_bolo
        self.ingredientes = []
        self.status = "Não Iniciado"

    def adicionar_ingrediente(self, nome, quantidade):
        """Adiciona um novo ingrediente à receita."""
        novo_ingrediente = Ingrediente(nome, quantidade)
        self.ingredientes.append(novo_ingrediente)
        print(f"✅ Adicionado: {novo_ingrediente.quantidade} de {novo_ingrediente.nome}.")

    def exibir_receita(self):
        """Exibe o nome do bolo e a lista completa de ingredientes."""
        print("\n" + "="*40)
        print(f"       RECEITA: {self.nome.upper()}")
        print("="*40)
        print("📝 INGREDIENTES NECESSÁRIOS:")
        if not self.ingredientes:
            print("(Nenhum ingrediente adicionado ainda.)")
        for ingrediente in self.ingredientes:
            print(ingrediente)
        print(f"\nStatus atual: {self.status}")
        print("="*40)

    def preparar_massa(self):
        """Simula a etapa de mistura dos ingredientes."""
        if self.status != "Não Iniciado":
            print(f"⚠️ A massa já está {self.status.lower()}.")
            return

        print("\n--- ETAPA 1: PREPARO DA MASSA ---")
        print("1. Bater os ingredientes úmidos (cenoura, ovos, óleo).")
        print("2. Misturar os secos (farinha, açúcar, fermento).")
        print("3. Juntar e misturar bem até a massa ficar homogênea.")
        self.status = "Pronto para Assar"
        print(f"🎉 MASSA PRONTA! Status: {self.status}")

    def assar(self, tempo_minutos, temperatura_celsius):
        """Simula a etapa de cozimento do bolo."""
        if self.status != "Pronto para Assar":
            print(f"❌ Não é possível assar. Status atual: {self.status}")
            return

        print("\n--- ETAPA 2: ASSAR ---")
        print(f"🔥 Assando o {self.nome} por {tempo_minutos} minutos a {temperatura_celsius}°C.")
        print("🕰️ Aguarde...")
        self.status = "Assado"
        print(f"🥳 BOLO ASSADO COM SUCESSO! Status: {self.status}")


# --- DEMONSTRAÇÃO DO USO EM POO ---

# 1. Instanciando o objeto 'bolo_de_cenoura' da classe 'ReceitaDeBolo'
bolo_de_cenoura = ReceitaDeBolo("Bolo de Cenoura com Cobertura de Chocolate")

# 2. Adicionando ingredientes (Interagindo com o objeto)
print("🏗️ Montando a lista de ingredientes...")
bolo_de_cenoura.adicionar_ingrediente("cenouras picadas", "3 unidades")
bolo_de_cenoura.adicionar_ingrediente("ovos grandes", "4")
bolo_de_cenoura.adicionar_ingrediente("óleo vegetal", "1 xícara")
bolo_de_cenoura.adicionar_ingrediente("açúcar", "2 xícaras")
bolo_de_cenoura.adicionar_ingrediente("farinha de trigo", "2 xícaras")
bolo_de_cenoura.adicionar_ingrediente("fermento em pó", "1 colher de sopa")

# 3. Exibindo o estado atual da receita
bolo_de_cenoura.exibir_receita()

# 4. Executando o comportamento da receita (métodos)
bolo_de_cenoura.preparar_massa()

# Tentativa de preparar a massa novamente (demonstra a lógica interna)
bolo_de_cenoura.preparar_massa()

# 5. Assando o bolo
bolo_de_cenoura.assar(tempo_minutos=40, temperatura_celsius=180)

# 6. Exibindo o estado final
bolo_de_cenoura.exibir_receita()

# 7. Exemplo de outra receita (Demonstra que a classe pode criar vários objetos)
print("\n" + "#"*50)
print("INICIANDO OUTRA RECEITA: BOLO DE FUBÁ")
print("#"*50)
bolo_de_fuba = ReceitaDeBolo("Bolo de Fubá Simples")
bolo_de_fuba.adicionar_ingrediente("fubá", "2 xícaras")
bolo_de_fuba.adicionar_ingrediente("leite", "1 xícara")
bolo_de_fuba.preparar_massa()
bolo_de_fuba.assar(tempo_minutos=35, temperatura_celsius=170)
