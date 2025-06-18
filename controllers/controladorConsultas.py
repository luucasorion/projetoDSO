from views.telaConsulta import TelaConsulta
from models.consulta import Consulta
from datetime import datetime


class ControllerConsulta:
    def __init__(self, controladorSistemas):
        super().__init__()
        self.__consultas = []
        self.__telaConsulta = TelaConsulta()
        self.__controlador_sistema = controladorSistemas

    def incluirConsulta(self):
        dados_consulta = self.__telaConsulta.pegarDadosConsulta()
        consulta_existente = self.selecionarConsultaPorCpfEData(
            dados_consulta["CPF_Paciente"], dados_consulta["Data"], dados_consulta["Horario"]
        )

        if consulta_existente is None:
            nova_consulta = Consulta(
                dados_consulta["CPF_Paciente"],
                dados_consulta["CRM_Medico"],
                dados_consulta["Data"],
                dados_consulta["Horario"]
            )
            self.__consultas.append(nova_consulta)
        else:
            self.__telaConsulta.mostrarMensagem("ATENÇÃO: Consulta já existente!")

    def selecionarConsultaPorCpfEData(self, cpf_paciente, data, horario):
        for consulta in self.__consultas:
            if (consulta.cpf_paciente == cpf_paciente and
                consulta.data == data and
                consulta.horario == horario):
                return consulta
        return None

    def alterarConsulta(self):
        self.listarConsultas()
        cpf, data = self.__telaConsulta.selecionarConsulta()
        consulta = None
        for c in self.__consultas:
            if c.cpf_paciente == cpf and c.data == data:
                consulta = c
                break

        if consulta is not None:
            novos_dados = self.__telaConsulta.pegarDadosConsulta()
            consulta.cpf_paciente = novos_dados["CPF_Paciente"]
            consulta.crm_medico = novos_dados["CRM_Medico"]
            consulta.data = novos_dados["Data"]
            consulta.horario = novos_dados["Horario"]
            self.__telaConsulta.mostrarMensagem("Consulta alterada com sucesso!")
        else:
            self.__telaConsulta.mostrarMensagem("ATENÇÃO: Consulta não encontrada.")

    def excluirConsulta(self):
        self.listarConsultas()
        cpf, data = self.__telaConsulta.selecionarConsulta()
        for consulta in self.__consultas:
            if consulta.cpf_paciente == cpf and consulta.data == data:
                self.__consultas.remove(consulta)
                self.__telaConsulta.mostrarMensagem("Consulta removida com sucesso!")
                return
        self.__telaConsulta.mostrarMensagem("ATENÇÃO: Consulta não encontrada.")

    def listarConsultas(self):
        if not self.__consultas:
            self.__telaConsulta.mostrarMensagem("Nenhuma consulta cadastrada.")
        else:
            for consulta in self.__consultas:
                self.__telaConsulta.mostrarConsulta({
                    "CPF_Paciente": consulta.cpf_paciente,
                    "CRM_Medico": consulta.crm_medico,
                    "Data": consulta.data,
                    "Horario": consulta.horario
                })

    def retornar(self):
        self.__controlador_sistema.inicializarSistema()

    def abreTela(self):
        opcoes = {
            1: self.incluirConsulta,
            2: self.alterarConsulta,
            3: self.listarConsultas,
            4: self.excluirConsulta,
            0: self.retornar
        }

        while True:
            opcao = self.__telaConsulta.telaOpcoes()
            opcoes[opcao]()
