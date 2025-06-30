from controladores.abstrato_controlador import ControladorBase
from dados.dao.paciente_DAO import PacienteDAO
from telas.tela_paciente import TelaPaciente
from modelos.paciente import Paciente

class ControladorPaciente(ControladorBase):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)

    def _get_dao(self):
        return PacienteDAO()

    def _get_tela(self):
        return TelaPaciente()

    def _criar_objeto(self, dados):
        return Paciente(dados["CPF"], dados["Nome"], dados["Idade"], dados["Telefone"])

    def _mostrar_entidade(self, paciente):
        self._tela.mostrar_paciente({"Nome": paciente.nome, "CPF": paciente.identidade, "Idade": paciente.idade, "Telefone": paciente.telefone})

    def _pegar_dados(self):
        while True:
            try:
                return self._tela.pegar_dados_paciente()
            except Exception as e:
                self._tela.mostrar_mensagem(str(e))

    def _selecionar_identificador(self):
        while True:
            try:
                return self._tela.selecionar_paciente_por_cpf()
            except Exception as e:
                self._tela.mostrar_mensagem(str(e))

    def _get_identidade(self, paciente):
        return paciente.identidade

    def exclui_filiado(self, paciente):
        if self.selecionar_por_id(paciente) is not None:
            ids_consultas_para_remover = []

            for consulta in self._controlador_sistema.controlador_consulta._dao.get_all():
                if consulta.paciente == paciente:
                    ids_consultas_para_remover.append(consulta.identidade)

            if ids_consultas_para_remover:
                for id_consulta in ids_consultas_para_remover:
                    self._controlador_sistema.controlador_consulta._dao.remove(id_consulta)
                
    def _atualizar_entidade(self, paciente, novos_dados):
        paciente.nome = novos_dados["Nome"]
        paciente.identidade = novos_dados["CPF"]
        paciente.idade = novos_dados["Idade"]
        paciente.telefone = novos_dados["Telefone"]

    def _id_chave(self):
        return "CPF"
