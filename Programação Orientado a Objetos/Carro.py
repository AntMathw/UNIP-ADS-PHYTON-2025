# -*- coding: utf-8 -*-
#
# Demonstração simples de Programação Orientada a Objetos (POO) em Python.
# O exemplo utiliza uma classe 'Carro' para representar um objeto do mundo real.

# 1. Definição da Classe
class Carro:
    """
    Define a estrutura de um Carro, que é o nosso objeto.
    Contém atributos (características) e métodos (ações).
    """

    # 2. Método Construtor (__init__)
    # Este método é chamado automaticamente quando um novo objeto é criado.
    # Ele define e inicializa os atributos (marca, modelo, cor, velocidade).
    def __init__(self, marca, modelo, cor):
        self.marca = marca      # Atributo de instância (característica)
        self.modelo = modelo    # Atributo de instância
        self.cor = cor          # Atributo de instância
        self.velocidade = 0     # Atributo inicializado (todos começam parados)

    # 3. Método (Ação)
    # Define o comportamento do objeto.
    def acelerar(self, incremento):
        """Aumenta a velocidade do carro em um determinado incremento."""
        if incremento > 0:
            self.velocidade += incremento
            print(f"O {self.modelo} da {self.marca} na cor {self.cor} acelerou.")
            print(f"Velocidade atual: {self.velocidade} km/h.")
        else:
            print("O incremento deve ser positivo para acelerar.")

    def frear(self, decremento):
        """Diminui a velocidade do carro, garantindo que não seja negativa."""
        if decremento > 0:
            self.velocidade -= decremento
            if self.velocidade < 0:
                self.velocidade = 0
            print(f"O {self.modelo} freou.")
            print(f"Velocidade atual: {self.velocidade} km/h.")
        else:
            print("O decremento deve ser positivo para frear.")

# --- Demonstração de Uso ---

# 4. Criação de Objetos (Instanciação)
# Criamos duas instâncias da classe Carro. Cada uma é um objeto independente.
print("--- Instanciando Objetos ---")
carro1 = Carro("Toyota", "Corolla", "Prata")
carro2 = Carro("Ford", "Mustang", "Vermelho")

# 5. Acessando Atributos
print(f"\nDetalhes do Carro 1: {carro1.marca} {carro1.modelo}, Cor: {carro1.cor}")
print(f"Detalhes do Carro 2: {carro2.marca} {carro2.modelo}, Cor: {carro2.cor}")

# 6. Chamando Métodos (Executando Ações)
print("\n--- Ações do Carro 1 ---")
carro1.acelerar(30)
carro1.acelerar(20)

print("\n--- Ações do Carro 2 ---")
carro2.acelerar(70)
carro2.frear(15)

# 7. Verificando o estado final dos objetos
print(f"\nEstado Final Carro 1: {carro1.velocidade} km/h")
print(f"Estado Final Carro 2: {carro2.velocidade} km/h")
