class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


livro1 = Livro('Curso de Python', 'Alcimar Costa')
print(livro1.autor)

livro1.autor = 'José da Silva'
print(livro1.autor) 


class Casa:
    def __init__(self, mansao, barraco):
        self.mansao = mansao
        self.barraco = barraco


casa1 = Casa('Mansao de Rico', 'casa de pobre')
print (casa1.mansao)

casa1.barraco = 'silvio santos'
print (casa1.barraco)