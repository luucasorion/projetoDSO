from datetime import date, time
class Consulta():
    def __init__(self, id : str, data : date, hora : time, status : str):
        self.__id = id
        self.__data = data
        self.__hora = hora
        self.__status = status

    @property
    def id(self):
        return self.__id
    @id.setter
    def id (self, id):
        self.__id = id
    

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


    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status):
        self.__status = status
           
