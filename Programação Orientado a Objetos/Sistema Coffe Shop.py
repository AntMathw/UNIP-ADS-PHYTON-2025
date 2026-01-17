#CÓDIGO PARA ESTUDOS EM POO

import random
import time

class IttemMenu:
    
    def __init__(self, nome, preco, tempo):
        self.nome = nome
        self.preco = preco
        self.tempo = tempo
    
    def __str__(self):
        return f"{self.nome:.<20} R$ {self.preco:>5.2f}"
    
class Pedido:
    
    def __init__(self, nome_cliente):
        self.nome_cliente = nome_cliente
        self.itens = []
        self.codigo_pedido = random.int(1000, 9999)
        self.tempo = 0

    def adicionar_itens(self, item):
        self.itens.append(item)
        self.tempo_total += item.tempo_preparo

class CoffeShop:

    def __init__(self, menu, item):
        self.menu = [
            item("Café Expresso", 5.50, 3),
            item("Cappuccino", 3.40, 9),
            item("Pão de Queijo", 2.50, 2),
            item("Latte Macchiato", 10.50, 6)
        ]

    def exibir_menu(self):
        print('\n=== MENU COFFE SHOP ===\n')
        for i, item in enumerate(self.menu, 1):
            print(f'{i}. {item}')
        print('0. Finalizar Pedido')

    def realizar_atendimento(self):
        print('='*20)
        print('  SISTEMA COFFE SHOP ')
        print('='*20)

        nome = input('Digite seu nome: ').strip().title()
        if not nome: nome = 'Cliente Anônimo'

        novo_pedido = Pedido(nome)
