class Biblioteca:
    bibliotecas = [] # atributo de classe (compartilhado por todas as instâncias)
    
    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
    
    def __str__(self):
        return self.nome
    
    def registrar(self):
        """Adiciona a instância atual à lista de bibliotecas"""
        Biblioteca.bibliotecas.append(self)
    
    @classmethod
    def listar_bibliotecas(cls):
        """Mostra todas as bibliotecas registradas"""
        for biblioteca in cls.bibliotecas:
            print(f"{biblioteca.nome} - {biblioteca.ativo}")
    
    # setter: altera o valor de _ativo
    def alterna_estado(self):
        """Alterna o estado da biblioteca"""
        self._ativo = not self._ativo
    
    # getter: retorna o estado de forma legível
    @property
    def ativo(self):
        """Propriedade que permite acessar o estado da biblioteca"""
        return "ativado" if self._ativo else "desativado"

# Criando instâncias
b1 = Biblioteca("Biblioteca da Cidade")
b2 = Biblioteca("Biblioteca do Shopping")

b1.registrar()
b1.alterna_estado()

b2.registrar()
b2.alterna_estado()

# Chamando classmethod sem precisar de instância
Biblioteca.listar_bibliotecas()