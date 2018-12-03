from abc import ABC, abstractmethod


class ModuleModel(ABC):

    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def run(self, bot):
        pass
