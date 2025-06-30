from controladores.abstrato_controlador import ControladorBase
from dados.dao.consulta_DAO import ConsultaDAO
from telas.tela_consulta import TelaConsulta
from modelos.consulta import Consulta

class ControladorConsulta(ControladorBase):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
   
    def incluir(self):
        self.listar_todos_medicos()
        self.listar_todos_pacientes()
        dados = self._pegar_dados()
        if self._controlador_sistema.controlador_medico.selecionar_por_id(dados["CRM"]) is None or self._controlador_sistema.controlador_paciente.selecionar_por_id(dados["CPF"]) is None:
            return self._tela.mostrar_mensagem("ATENÇÃO: Medico ou Paciente não cadastrados!")

        id_entidade = dados[self._id_chave()]
        if self.selecionar_por_id(id_entidade) is None:
            entidade = self._criar_objeto(dados)
            self._dao.add(id_entidade, entidade)
        else:
            self._tela.mostrar_mensagem("ATENÇÃO: entidade já cadastrada!")

    def _get_dao(self):
        return ConsultaDAO()

    def _get_tela(self):
        return TelaConsulta()

    def _criar_objeto(self, dados):
        return Consulta(dados["CRM"], dados["CPF"], dados["Identidade"], dados["Data"], dados["Hora"])

    def _mostrar_entidade(self, consulta):
        self._tela.mostrar_consulta({"CRM": consulta.medico, "CPF": consulta.paciente, "Identidade": consulta.identidade, "Data": consulta.data, "Hora": consulta.hora})

    def _pegar_dados(self):
        return self._tela.pegar_dados_consulta()

    def _selecionar_identificador(self):
        return self._tela.selecionar_consulta()

    def _get_identidade(self, consulta):
        return consulta.identidade

    def _atualizar_entidade(self, consulta, novos_dados):
        consulta.crm = novos_dados["CRM"]
        consulta.cpf = novos_dados["CPF"]
        consulta.identidade = novos_dados["Identidade"]
        consulta.data = novos_dados["Data"]
        consulta.hora = novos_dados["Hora"]

    def _id_chave(self):
        return "Identidade"

    def listar_por_crm(self):
        if self._controlador_sistema.controlador_medico.listar() == 1:
            return
        id_entidade = self._controlador_sistema.controlador_medico._selecionar_identificador()
        entidade = self._controlador_sistema.controlador_medico.selecionar_por_id(id_entidade)
        if entidade is not None:
            for m in self._dao.get_all():
                if m.medico == entidade.identidade:
                    self._mostrar_entidade(m)
        else:
            self._tela.mostrar_mensagem("ATENÇÃO: entidade não encontrada!")
    
    def listar_por_cpf(self):
        if self._controlador_sistema.controlador_paciente.listar() == 1:
            return
        id_entidade = self._controlador_sistema.controlador_paciente._selecionar_identificador()
        entidade = self._controlador_sistema.controlador_paciente.selecionar_por_id(id_entidade)
        if entidade is not None:
            for m in self._dao.get_all():
                if m.paciente == entidade.identidade:
                    self._mostrar_entidade(m)
        else:
            self._tela.mostrar_mensagem("ATENÇÃO: entidade não encontrada!")

    def listar_todos_medicos(self):
        medicos = self._controlador_sistema.controlador_medico._dao.get_all()
        if not medicos:
            self._tela.mostrar_mensagem("Nenhum médico cadastrado.")
            return
        print("\n-------- Lista de Médicos --------")
        for medico in medicos:
            print(f"Nome: {medico.nome}, CRM: {medico.identidade}, Especialidade: {medico.especialidade}")

    def listar_todos_pacientes(self):
        pacientes = self._controlador_sistema.controlador_paciente._dao.get_all()
        if not pacientes:
            self._tela.mostrar_mensagem("Nenhum paciente cadastrado.")
            return
        print("\n-------- Lista de Pacientes --------")
        for paciente in pacientes:
            print(f"Nome: {paciente.nome}, CPF: {paciente.identidade}, Idade: {paciente.idade}, Telefone: {paciente.telefone}")

    def abre_tela(self):
        opcoes = {
            1: self.incluir,
            2: self.alterar,
            3: self.listar,
            4: self.listar_por_crm,
            5: self.listar_por_cpf,
            6: self.excluir,
            7: self.listar_todos_medicos,
            8: self.listar_todos_pacientes,
            0: self.retornar
        }
        while True:
            opcao = self._tela.tela_opcoes()
            if opcao in opcoes:
                opcoes[opcao]()
            else:
                self._tela.mostrar_mensagem("Opção inválida!")
