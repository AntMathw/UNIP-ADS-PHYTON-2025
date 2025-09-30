class Animal:
    def __init__(self, nome):
        self.nome = nome
    def emitir_som(self):
        pass
class Cachorro(Animal):
    def emitir_som(self):
        return 'AU, AU!'

class Gato(Animal):
    def emitir_som(self):
        return 'MIAU!'

dog = cachorro('Ronaldo')
cat = gato('Estrassalha Pussy')

print(dog.nome,'-',dog.emitir_som())
print(cat.nome,'-',cat.emitir_som())



