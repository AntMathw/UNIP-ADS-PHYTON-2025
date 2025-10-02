#Classe Animais seus respectivos sons e características

class Animal:
    def __init__(self, nome, caracteristicas=None):
        self.nome = nome
        # Aceita lista ou string
        if caracteristicas is None:
            self.caracteristicas = []
        elif isinstance(caracteristicas, list):
            self.caracteristicas = caracteristicas
        else:
            self.caracteristicas = [caracteristicas]

    def emitir_som(self):
        pass

    def mostrar_caracteristicas(self):
        return ', '.join(self.caracteristicas)

class Cachorro(Animal):
    def emitir_som(self):
        return 'AU, AU!'

class Gato(Animal):
    def emitir_som(self):
        return 'MIAU!'


dog = Cachorro('Ronaldo', ['Olhos Castanhos', 'Pelagem maior', 'Raça Pitbull'])
cat = Gato('Gugui', ['Olhos claros', 'Pelagem baixa'])

print(f'{dog.nome} - {dog.mostrar_caracteristicas()} - {dog.emitir_som()}')
print(f'{cat.nome} - {cat.mostrar_caracteristicas()} - {cat.emitir_som()}')
