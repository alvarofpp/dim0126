from abc import ABC, abstractmethod


class MilitaryModel(ABC):
    """Classe abstrata de módulo de poder militar"""

    def __init__(self):
        super().__init__()

    @abstractmethod
    def condition(self, bot):
        """Condições para executar as ações"""
        pass

    @abstractmethod
    def build(self, bot):
        pass

    @abstractmethod
    def train(self, bot):
        pass
