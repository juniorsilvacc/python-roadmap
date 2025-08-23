from modelos.avaliacao import Avaliacao

class Biblioteca:
    bibliotecas = []

    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        self._avaliacao = []

    def __str__(self):
        return self.nome
    
    def registrar(self):
        """Adiciona a instância atual à lista de bibliotecas"""
        Biblioteca.bibliotecas.append(self)
    
    @classmethod
    def listar_bibliotecas(cls):
        """Mostra todas as bibliotecas registradas"""
        print(f"{'Nome da biblioteca'.ljust(25)} | {'Nota média'.ljust(25)} | {'Status'.ljust(25)}")
        for biblioteca in cls.bibliotecas:
            print(f"{biblioteca.nome.ljust(25)} | {str(biblioteca.media_avaliacoes).ljust(25)} | {biblioteca.ativo.ljust(25)}")
    
    def alterna_estado(self):
        """setter: Alterna o estado da biblioteca"""
        self._ativo = not self._ativo
    
    @property
    def ativo(self):
        """getter: Propriedade que permite acessar o estado da biblioteca"""
        return "ativado" if self._ativo else "desativado"
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        else:
            soma = sum(avaliacao._nota for avaliacao in self._avaliacao) # Pegar cada nota, para cada avaliação que esteja na lista de avaliações
            media = round(soma / len(self._avaliacao), 1)
            return media