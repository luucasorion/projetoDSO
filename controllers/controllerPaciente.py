from views.viewPaciente import TelaPaciente
from models.paciente import Paciente

class ControllerPaciente():
    def __init__(self, controladorSistemas):
        super().__init__()
        self.__pacientes = []
        self.__telaPacientes = TelaPaciente()
        self.__controlador_sistema = controladorSistemas

    def incluirPaciente(self):
        dados_paciente = self.__telaPacientes.pegarDadosPaciente()
        paciente = self.selecionarPacientePorCpf(dados_paciente["CPF"])
        if paciente is None:
            paciente = Paciente(dados_paciente["CPF"], dados_paciente["Nome"], dados_paciente["Idade"], dados_paciente["Telefone"])
            self.__pacientes.append(paciente)
        else:
            self.__telaPacientes.mostrarMensagem("ATENÇÃO: paciente já cadastrado!")

    def selecionarPacientePorCpf(self, cpf):
        for paciente in self.__pacientes:
            if paciente.identidade == cpf:
                return paciente
        return None

    def alterarPaciente(self):
        self.listarPacientes()
        cpf = self.__telaPacientes.selecionarPaciente()
        paciente = self.selecionarPacientePorCpf(cpf)

        if paciente is not None:
            novos_dados = self.__telaPacientes.pegarDadosPaciente()
            paciente.nome = novos_dados["Nome"]
            paciente.identidade = novos_dados["CPF"]
            paciente.idade = novos_dados["Idade"]
            paciente.telefone = novos_dados["Telefone"]
            self.listarPacientes()
        else:
            self.__telaPacientes.mostrarMensagem("ATENÇÃO: paciente não encontrado!")

    def excluirPacientePorCpf(self):
        self.listarPacientes()
        cpf = self.__telaPacientes.selecionarPaciente()
        paciente = self.selecionarPacientePorCpf(cpf)
        if paciente is not None:
            self.__pacientes.remove(paciente)
        else:
            self.__telaPacientes.mostrarMensagem("ATENÇÃO: paciente não encontrado!")

    def listarPacientes(self):
        for paciente in self.__pacientes:
            self.__telaPacientes.mostrarPaciente({
                "Nome": paciente.nome,
                "CPF": paciente.identidade,
                "Idade": paciente.idade,
                "Telefone": paciente.telefone
            })

    def retornar(self):
        self.__controlador_sistema.abreTela()

    def abreTela(self):
        listaOpcoes = {
            1: self.incluirPaciente,
            2: self.alterarPaciente,
            3: self.listarPacientes,
            4: self.excluirPacientePorCpf,
            0: self.retornar
        }

        continua = True
        while continua:
            opcao = self.__telaPacientes.telaOpcoes()
            if opcao in listaOpcoes:
                listaOpcoes[opcao]()
            else:
                self.__telaPacientes.mostrarMensagem("Opção inválida!")
