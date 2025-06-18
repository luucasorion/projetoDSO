from views.viewSistema import ViewSistema
from controllers.controllerMedico import ControllerMedico
from controllers.controllerPaciente import ControllerPaciente
from controllers.controladorConsultas import ControllerConsulta

class ControladorSistema:
    def __init__(self):
        self.__controllerMedico = ControllerMedico(self)
        self.__controlador_paciente = ControllerPaciente(self)
        self.__controlador_consulta = ControllerConsulta(self)
        self.__tela_sistema = ViewSistema(self.abreTela)

    def inicializarSistema(self):
        self.__tela_sistema.janela_opcoes()

    def cadastrarMedico(self):
        self.__controllerMedico.abreTela()

    def cadastrarPaciente(self):
        self.__controlador_paciente.abreTela()

    def cadastraConsulta(self):
        self.__controlador_consulta.abreTela()

    def encerraSistema(self):
        exit(0)

    def abreTela(self, opcao):
        listaOpcoes = {
            3: self.encerraSistema,
            0: self.cadastrarMedico,
            1: self.cadastrarPaciente,
            2: self.cadastraConsulta
        }
        funcao = listaOpcoes.get(opcao)
        if funcao:
            funcao()

