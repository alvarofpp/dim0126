from abc import ABC, abstractmethod
 
class ModuleAISC(ABC):

    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def run(self, bot):
        pass