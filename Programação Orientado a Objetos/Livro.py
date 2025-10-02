class Livro:
    def __init__(self, titulo, autor, ano_de_publicacao, numero_de_paginas):
        self.titulo = titulo
        self.autor = autor
        self.ano_de_publicacao = ano_de_publicacao
        self.numero_de_paginas = numero_de_paginas

    def detalhes(self):
        print(f'Título: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano_de_publicacao}, Páginas: {self.numero_de_paginas}')

    def eh_antigo(self):
        return self.ano_de_publicacao < 2000

    def atualizar_paginas(self, novo_numero_paginas):
        self.numero_de_paginas = novo_numero_paginas


livro1 = Livro("1984", "George Orwell", 1949, 328)

livro1.detalhes()
print(livro1.eh_antigo())
livro1.atualizar_paginas(350)

