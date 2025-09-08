#Lista em formato de FILA com append, pop e del
#FIFO (First In First Out)

def main():

    fila = []
    print(f'Fila vazia {fila}')

    fila.append(3)
    print(fila)
    fila.append(7)
    print(fila)
    fila.append(2)
    print(fila)
    fila.append(0)
    print(fila)
    fila.pop(0)
    print(fila)

    fila.append(11)

    del fila[0:4]
    print(f'Fila sem elementos {fila}')

if __name__ == "__main__":
    main()
