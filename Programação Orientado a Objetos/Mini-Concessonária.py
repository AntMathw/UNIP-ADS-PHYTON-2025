class veiculo:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    def info(self):
       return (f'Modelo: {self.modelo}\nCor: {self.cor}\nAno: {self.ano}')
print('=================CARROS================\n')
carro = veiculo('Jetta', 'Branco', '2010')
carro2 = veiculo('Fusca', 'Preto', '2014\n')
print(carro.info())
print('-' * 25)
print(carro2.info())

class moto(veiculo):
    def info(self):
        return (f'Modelo: {self.modelo}\nCor: {self.cor}\nAno: {self.ano}')

moto = veiculo('Kawasaki 400', 'Preto', '2024')
moto2 = veiculo('Yamaha R3', 'Branco', '2021\n')

print('=================MOTOS===================\n')
print(moto.info())
print('-' * 25)
print(moto2.info())

class caminhão(veiculo):
    def info(self):
        return (f'Modelo: {self.modelo}\nCor: {self.cor}\nAno: {self.ano}')

print('============CAMINHÕES=============\n')
caminhão = veiculo('Mercedes 1113', 'Azul', '1970')
caminhão2 = veiculo('Scania L-65', 'Azul', '1950\n')
print(caminhão.info())
print('-' * 25)
print(caminhão2.info())

class especial(veiculo):
    def info(self):
        return (f'Modelo: {self.modelo}\nCor: {self.cor}\nAno: {self.ano}')
print('============ESPECIAIS===========\n')

especial1 = veiculo('Guindaste Zunline', 'Branco', '2011')
especial2 = veiculo('Escavadeira PC 8000', 'Amarelo', '2004\n')

print(especial1.info())
print('-' * 25)
print(especial2.info())
