from modelos.abstrato_pessoa import Pessoa


class Paciente (Pessoa):
    def __init__(self, cpf, nome, idade : int, telefone : str):
        super().__init__(cpf, nome)
        self.__idade = idade
        self.__telefone = telefone
    
    
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
 
    

