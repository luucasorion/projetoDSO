from controllers.controllerMedico import ControllerMedico

class ControladorSistema():

    def __init__(self):
        self.__controllerMedico = ControllerMedico

    @property
    def controllerMedicos(self):
        return self.__controllerMedico
    
    @property
    def controllerPacientes(self):
        pass
    



    def inicializarSistema(self):
        self.abreTela()

    def cadastrarMedico(self):
        self.__controllerMedico.abreTela()

    def cadastrarPaciente(self):
        pass

    def cadastraConsulta(self):
        pass

    def encerraSistema(self):
        exit(0)

    def abreTela(self):
        listaOpcoes = {1: self.cadastrarMedico, 2: self.cadastrarPaciente, 3: self.cadastraConsulta,
                        0: self.encerra_sistema}

        while True:
            opcaoEscolhida = self.__tela_sistema.tela_opcoes()
            funcaoEscolhida = listaOpcoes[opcaoEscolhida]
            funcaoEscolhida()