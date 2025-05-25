
from abc import abstractmethod, ABC

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, identidade : str, nome : str):
        self.__identidade = identidade
        self.__nome = nome
    
    
    @property
    def identidade(self):
        return self.__identidade
    @identidade.setter
    def identidade(self, identidade):
        self.__identidade = identidade
    
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    