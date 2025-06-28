from controladores.abstrato_controlador import ControladorBase
from dados.dao.medico_DAO import MedicoDAO
from telas.tela_medico import TelaMedico
from modelos.medico import Medico

class ControladorMedico(ControladorBase):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)

    def _get_dao(self):
        return MedicoDAO()

    def _get_tela(self):
        return TelaMedico()

    def _criar_objeto(self, dados):
        return Medico(dados["CRM"], dados["Nome"], dados["Especialidade"])

    def _mostrar_entidade(self, medico):
        self._tela.mostrar_medico({"Nome": medico.nome, "CRM": medico.identidade, "Especialidade": medico.especialidade})

    def _pegar_dados(self):
        return self._tela.pegar_dados_medico()

    def _selecionar_identificador(self):
        return self._tela.selecionar_medico_por_crm()

    def _get_identidade(self, medico):
        return medico.identidade


    def exclui_filiado(self, medico):

        if medico is not None:
            ids_consultas_para_remover = []

            for consulta in self._controlador_sistema.controlador_consulta._dao.get_all():
                if consulta.medico == medico:
                    ids_consultas_para_remover.append(consulta.identidade)

            if ids_consultas_para_remover:
                for id_consulta in ids_consultas_para_remover:
                    self._controlador_sistema.controlador_consulta._dao.remove(id_consulta)
                

    def _atualizar_entidade(self, medico, novos_dados):
        medico.nome = novos_dados["Nome"]
        medico.identidade = novos_dados["CRM"]
        medico.especialidade = novos_dados["Especialidade"]

    def _id_chave(self):
        return "CRM"
