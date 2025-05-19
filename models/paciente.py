from models.pessoa import Pessoa


class Paciente (Pessoa):
    def __init__(self, id, nome, idade : int, telefone : str, email : str):
        super().__init__(id, nome)
        self.__idade = idade
        self.__telefone = telefone
        self.__email = email
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email    
    
    

