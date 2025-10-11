class Livro:
    
    def __init__(self, titulo: str, autor: str, isbn: str):
        # Atributos do objeto Livro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True  # Começa como disponível

    def __str__(self):
        """Método especial para representação em string do objeto."""
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn}) - Status: {status}"

    def emprestar(self):
        """Altera o status do livro para emprestado, se estiver disponível."""
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        """Altera o status do livro para disponível."""
        self.disponivel = True


class Biblioteca:
    """
    Representa a coleção de livros e gerencia suas operações.
    """
    def __init__(self):
        # Atributo que guarda a coleção de livros (um dicionário onde a chave é o ISBN)
        self.colecao = {}

    def adicionar_livro(self, livro: Livro):
        """Adiciona um objeto Livro à coleção da biblioteca."""
        if livro.isbn in self.colecao:
            print(f"Erro: Livro com ISBN {livro.isbn} já existe na biblioteca.")
        else:
            self.colecao[livro.isbn] = livro
            print(f"Livro '{livro.titulo}' adicionado com sucesso.")

    def emprestar_livro(self, isbn: str):
        """Empresta um livro pelo seu ISBN."""
        if isbn in self.colecao:
            livro = self.colecao[isbn]
            if livro.emprestar():
                print(f"Livro '{livro.titulo}' emprestado.")
            else:
                print(f"Livro '{livro.titulo}' já está emprestado.")
        else:
            print(f"Erro: Livro com ISBN {isbn} não encontrado.")

    def devolver_livro(self, isbn: str):
        """Devolve um livro pelo seu ISBN."""
        if isbn in self.colecao:
            livro = self.colecao[isbn]
            if not livro.disponivel: # Verifica se está emprestado antes de devolver
                livro.devolver()
                print(f"Livro '{livro.titulo}' devolvido com sucesso.")
            else:
                 print(f"Erro: Livro '{livro.titulo}' já estava disponível.")
        else:
            print(f"Erro: Livro com ISBN {isbn} não encontrado.")

    def listar_livros(self):
        """Exibe todos os livros da coleção e seus status."""
        if not self.colecao:
            print("A biblioteca está vazia.")
            return

        print("\n--- Coleção da Biblioteca ---")
        for livro in self.colecao.values():
            print(livro)
        print("----------------------------\n")