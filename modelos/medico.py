from modelos.pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, crm: str, nome: str, especialidade: str):
        super().__init__(crm, nome)
        self.__especialidade = especialidade

    @property
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade):
        self.__especialidade = especialidade
    
   

    
   