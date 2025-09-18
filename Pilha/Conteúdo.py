#Lista em formato de Pilhas com INSERT, POP e DEL 
#LIFO (Last In First Out)

def main():
    
    pilha = []
    print(f'Pilha vazia {pilha}')

    pilha.insert(0,2)
    print(pilha)
    pilha.insert(1, 31)
    print(pilha)
    pilha.insert(2, 42)
    print(pilha)
    pilha.insert(3, 40)

    pilha.pop(0)
    print(pilha)

    del pilha[0: 2]
    print(pilha)

    pilha.insert(4, 90)
    print(pilha)

if __name__ == "__main__":
    main()


#Exemplo de prática do LIFO(Last In First Out)

# LIFO (Último a Entrar, Primeiro a Sair) usando Pilha
class Pilha:
    def __init__(self):
        self.pilha = []
    
    def empurrar(self, item):
        self.pilha.append(item)
        print(f"Item empurrado: {item}")
    
    def remover(self):
        if self.esta_vazia():
            return "Pilha está vazia"
        return self.pilha.pop()
    
    def topo(self):
        if self.esta_vazia():
            return "Pilha está vazia"
        return self.pilha[-1]
    
    def esta_vazia(self):
        return len(self.pilha) == 0
    
    def tamanho(self):
        return len(self.pilha)
