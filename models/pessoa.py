
from abc import abstractmethod, ABC

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, id : str, nome : str):
        self.__id = id
        self.__nome = nome
    
    @abstractmethod
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id
    
    @abstractmethod
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    