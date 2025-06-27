from telas.tela_consulta import TelaConsulta
from modelos.consulta import Consulta
from datetime import datetime
from modelos.medico import Medico
from modelos.paciente import Paciente


class ControladorConsulta:
    def __init__(self, controladorSistemas):
        super().__init__()
        self.__consultas = []
        self.__telaConsulta = TelaConsulta()
        self.__controlador_sistema = controladorSistemas    

    def abre_tela(self):
        
        opcoes = {
        1: self.incluir_consulta,
        2: self.alterar_consulta,
        3: self.listar_consultas,
        4: self.excluir_consulta,
        0: self.retornar
        }

        while True:
            opcao = self.__telaConsulta.telaOpcoes()
            opcoes[opcao]()

    
    
    
    def incluir_consulta(self): 
        self.__controlador_sistema.controllerMedico.listarMedicos()
        dados_consulta = self.__telaConsulta.pegarDadosConsulta()
         
        consulta_existente = self.selecionar_consulta_por_cpf_e_data(
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

    def selecionar_consulta_por_cpf_e_data(self, cpf_paciente, data, horario):
        for consulta in self.__consultas:
            if (consulta.cpf_paciente == cpf_paciente and
                consulta.data == data and
                consulta.horario == horario):
                return consulta
        return None

    def alterar_consulta(self):
        self.listar_consultas()
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

    def excluir_consulta(self):
        self.listar_consultas()
        cpf, data = self.__telaConsulta.selecionarConsulta()
        for consulta in self.__consultas:
            if consulta.cpf_paciente == cpf and consulta.data == data:
                self.__consultas.remove(consulta)
                self.__telaConsulta.mostrarMensagem("Consulta removida com sucesso!")
                return
        self.__telaConsulta.mostrarMensagem("ATENÇÃO: Consulta não encontrada.")

    def listar_consultas(self):
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

   