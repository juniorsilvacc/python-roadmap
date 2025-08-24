from abc import ABC, abstractmethod

class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor, preco):
        self._titulo = titulo
        self._autor = autor
        self._preco = preco
    
    # Quando você quer aplicar polimorfismo, normalmente cria uma superclasse abstrata com um método que deve ser implementado nas subclasses.
    @abstractmethod
    def aplicar_desconto(self):
        """Cada subclasse deve implementar sua própria regra de desconto"""
        pass