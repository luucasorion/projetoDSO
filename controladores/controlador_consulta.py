from controladores.abstrato_controlador import ControladorBase
from dados.dao.consulta_DAO import ConsultaDAO
from telas.tela_consulta import TelaConsulta
from modelos.consulta import Consulta

class ControladorConsulta(ControladorBase):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
   
    def incluir(self):
        dados = self._pegar_dados()
        if self._controlador_sistema.controlador_medico.selecionar_por_id(dados["CRM"]) is None or self. _controlador_sistema.controlador_paciente.selecionar_por_id(dados["CPF"]) is None:
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
