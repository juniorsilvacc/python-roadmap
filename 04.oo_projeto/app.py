from modelos.biblioteca import Biblioteca

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

biblioteca_cidade.registrar()
biblioteca_shopping.registrar()

biblioteca_cidade.receber_avaliacao("Junior Silva", 9.5)
biblioteca_cidade.receber_avaliacao("Cícero Júnior", 10.0)

biblioteca_shopping.receber_avaliacao("Cícero Júnior", 8.0)
biblioteca_shopping.receber_avaliacao("Cícero Júnior", 7.0)

def main():
    Biblioteca.listar_bibliotecas()

if __name__ == "__main__":
    main()