from datetime import date, time
from modelos.paciente import Paciente
from modelos.medico import Medico

class Consulta():
    def __init__(self, medico: str, paciente: str , identidade : str, data: date, hora: time):

        self.__medico = medico
        self.__paciente = paciente
        self.__identidade = identidade
        self.__data = data
        self.__hora = hora

    @property
    def medico(self):
        return self.__medico
    @medico.setter
    def medico (self, medico):
        self.__medico = medico
    
    @property
    def paciente(self):
        return self.__paciente
    @paciente.setter
    def paciente (self, paciente):
        self.__paciente = paciente

    @property
    def identidade(self):
        return self.__identidade
    @identidade.setter
    def identidade (self, identidade):
        self.__identidade = identidade
    
    @property
    def data(self):
        return self.__data
    @data.setter
    def data (self, data):
        self.__data = data

    @property
    def hora(self):
        return self.__hora
    @hora.setter
    def hora (self, hora):
        self.__hora = hora

