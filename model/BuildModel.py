from abc import ABC, abstractmethod


class BuildModel(ABC):
    """Classe abstrata de módulo de construção"""

    def __init__(self):
        super().__init__()

    @abstractmethod
    def condition(self, bot):
        """Condições para executar as ações"""
        pass

    @abstractmethod
    def build(self, bot):
        """Executar o proceso de consrução de algo"""
        pass
