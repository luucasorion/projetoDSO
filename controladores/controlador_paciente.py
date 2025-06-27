from dados.dao.paciente_DAO import PacienteDAO
from telas.tela_paciente import TelaPaciente
from modelos.paciente import Paciente

class ControladorPaciente():
    def __init__(self, controladorSistemas):
        self.__paciente_dao = PacienteDAO()
        self.__tela_pacientes = TelaPaciente()
        self.__controlador_sistema = controladorSistemas

    def abreTela(self):

        listaOpcoes = {
            1: self.incluir_paciente,
            2: self.alterar_paciente,
            3: self.listar_pacientes,
            4: self.excluir_paciente_por_cpf,
            0: self.retornar
        }

        continua = True
        while continua:
            opcao = self.__tela_pacientes.tela_opcoes()
            if opcao in listaOpcoes:
                listaOpcoes[opcao]()
            else:
                self.__tela_pacientes.mostrar_mensagem("Opção inválida!")

    def incluir_paciente(self):
        dados_paciente = self.__tela_pacientes.pegar_dados_paciente()
        cpf = dados_paciente["CPF"]
        paciente_existe = self.selecionar_paciente_por_cpf(cpf)
        if paciente_existe is None:
            paciente = Paciente(dados_paciente["CPF"], dados_paciente["Nome"], dados_paciente["Idade"], dados_paciente["Telefone"])
            self.__paciente_dao.add(cpf, paciente)
        else:
            self.__tela_pacientes.mostrar_mensagem("ATENÇÃO: paciente já cadastrado!")

    def selecionar_paciente_por_cpf(self, cpf):
        for paciente in self.__paciente_dao.get_all():
            if paciente.identidade == cpf:
                return paciente
        return None

    def alterar_paciente(self):
        self.listar_pacientes()
        cpf = self.__tela_pacientes.selecionar_paciente()
        paciente = self.selecionar_paciente_por_cpf(cpf)

        if paciente is not None:
            novos_dados = self.__tela_pacientes.pegar_dados_paciente()
            paciente.nome = novos_dados["Nome"]
            paciente.identidade = novos_dados["CPF"]
            paciente.idade = novos_dados["Idade"]
            paciente.telefone = novos_dados["Telefone"]
            self.listar_pacientes()
        else:
            self.__tela_pacientes.mostrar_mensagem("ATENÇÃO: paciente não encontrado!")

    def excluir_paciente_por_cpf(self):
        self.listar_pacientes()
        cpf = self.__tela_pacientes.selecionar_paciente()
        paciente = self.selecionar_paciente_por_cpf(cpf)
        if paciente is not None:
            self.__paciente_dao.remove(paciente)
        else:
            self.__tela_pacientes.mostrar_mensagem("ATENÇÃO: paciente não encontrado!")

    def listar_pacientes(self):
        if self.__paciente_dao.get_all() is not None:
            for paciente in self.__paciente_dao.get_all():
                self.__tela_pacientes.mostrar_paciente({
                    "Nome": paciente.nome,
                    "CPF": paciente.identidade,
                    "Idade": paciente.idade,
                    "Telefone": paciente.telefone
                })
            return
        print("nao ha pacientes para lsitar!")
        return
        

    def retornar(self):
            self.__paciente_dao.save()
            self.__controlador_sistema.inicializarSistema()

    