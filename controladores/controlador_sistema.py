from telas.tela_sistema import TelaSitema
from controladores.controlador_medico import ControladorMedico
from controladores.controlador_paciente import ControladorPaciente
from controladores.controlador_consulta import ControladorConsulta

class ControladorSistema:
    def __init__(self):
        self.controlador_medico = ControladorMedico(self)
        self.controlador_paciente = ControladorPaciente(self)
        self.controlador_consulta = ControladorConsulta(self)
        self.__tela_sistema = TelaSitema(self.abre_tela)

    def abre_tela(self, opcao):
        lista_opcoes = {
            3: self.encerra_sistema,
            0: self.inicializar_medico,
            1: self.inicializar_paciente,
            2: self.inicializar_consulta
        }
        funcao = lista_opcoes.get(opcao)
        if funcao:
            funcao()

    def inicializar_sistema(self):
        self.__tela_sistema.janela_opcoes()
    def inicializar_medico(self):
        self.controlador_medico.abre_tela()
    def inicializar_paciente(self):
        self.controlador_paciente.abre_tela()
    def inicializar_consulta(self):
        self.controlador_consulta.abre_tela()

    def encerra_sistema(self):
        exit(0)

    

