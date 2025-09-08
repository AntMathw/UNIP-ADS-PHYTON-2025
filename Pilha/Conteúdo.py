#Lista em formato de Pilhas com INSERT, POP e DEL 

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
