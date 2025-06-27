from telas.tela_sistema import ViewSistema
from controladores.controlador_medico import ControladorMedico
from controladores.controlador_paciente import ControladorPaciente
from controladores.controlador_consulta import ControladorConsulta

class ControladorSistema:
    def __init__(self):
        self.controllerMedico = ControladorMedico(self)
        self.__controlador_paciente = ControladorPaciente(self)
        self.__controlador_consulta = ControladorConsulta(self)
        self.__tela_sistema = ViewSistema(self.abreTela)

    def inicializarSistema(self):
        self.__tela_sistema.janela_opcoes()

    def cadastrarMedico(self):
        self.controllerMedico.abre_tela()

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

