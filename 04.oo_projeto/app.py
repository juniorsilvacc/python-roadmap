from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

# biblioteca_cidade.registrar()
# biblioteca_shopping.registrar()

# biblioteca_cidade.receber_avaliacao("Junior Silva", 9.5)
# biblioteca_cidade.receber_avaliacao("Cícero Júnior", 10.0)

# biblioteca_shopping.receber_avaliacao("Cícero Júnior", 8.0)
# biblioteca_shopping.receber_avaliacao("Cícero Júnior", 7.0)

livro1 = Livro("1984", "Georgffe Orwell", 30.0, "012-3245")
revista1 = Revista("National Geographic", "John Doe", 15.0, "Quinta")

def main():
    Biblioteca.listar_bibliotecas()
    print(vars(livro1))
    print(vars(revista1))
if __name__ == "__main__":
    main()