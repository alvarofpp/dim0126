from abc import ABC, abstractmethod


class ModuleModel(ABC):
    """Classe abstrata de módulo geral"""

    def __init__(self):
        super().__init__()

    @abstractmethod
    def condition(self, bot):
        """Condições para executar as ações"""
        pass

    @abstractmethod
    def run(self, bot):
        """Ações que serão executadas"""
        pass
