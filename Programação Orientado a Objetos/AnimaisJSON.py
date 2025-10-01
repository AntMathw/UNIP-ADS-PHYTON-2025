import json

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass

    def to_dict(self):
        return {
            'tipo': self.__class__.__name__,
            'nome': self.nome,
            'som': self.emitir_som()
        }

class Cachorro(Animal):
    def emitir_som(self):
        return "AU, AU!"

class Gato(Animal):
    def emitir_som(self):
        return "MIAU"


dog = Cachorro('Mano Brown')
cat = Gato('Rato de Laboratório')


animais = [dog, cat]


animais_dict = [animal.to_dict() for animal in animais]


json_str = json.dumps(animais_dict, indent=4, ensure_ascii=False)


print(json_str)


print(dog.nome, '-', dog.emitir_som())
print(cat.nome, '-', cat.emitir_som())
