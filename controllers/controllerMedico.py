from models.medico import Medico

class ControllerMedico(Medico):
    def __init__(self, crm, nome, especialidade):
        super().__init__(crm, nome, especialidade)
        self.__medicos = []

    def incluirMedico(self, crm, nome, especialidade):
        informacoes = [crm, nome, especialidade]
        self.__medicos.append(informacoes)
    
    def escolherMedico
    
