from views.viewSistema import ViewSistema
from controllers.controllerMedico import ControllerMedico
from controllers.controllerPaciente import ControllerPaciente
from controllers.controladorConsultas import ControllerConsulta

class ControladorSistema():

    def __init__(self):
        self.__controllerMedico = ControllerMedico(self)
        self.__controlador_paciente = ControllerPaciente(self)
        self.__controlador_consulta = ControllerConsulta(self)
        self.__tela_sistema = ViewSistema()
    
    @property
    def controllerMedicos(self):
        return self.__controllerMedico
    
    @property
    def controllerPacientes(self):
        return self.__controlador_paciente
    
    @property
    def controllerConsulta(self):
        return self.__controlador_consulta


    def inicializarSistema(self):
        self.abreTela()

    def cadastrarMedico(self):
        self.__controllerMedico.abreTela()

    def cadastrarPaciente(self):
        self.__controlador_paciente.abreTela()

    def cadastraConsulta(self):
        self.__controlador_consulta.abreTela()
    

    def encerraSistema(self):
        exit(0)

    def abreTela(self):
        listaOpcoes = {1: self.cadastrarMedico, 2: self.cadastrarPaciente, 3: self.cadastraConsulta,
                        0: self.encerraSistema}

        while True:
            opcaoEscolhida = self.__tela_sistema.tela_opcoes()
            funcaoEscolhida = listaOpcoes[opcaoEscolhida]
            funcaoEscolhida()