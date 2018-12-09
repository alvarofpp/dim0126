from abc import ABC, abstractmethod


class OperationModel(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def build(self, bot):
        pass
