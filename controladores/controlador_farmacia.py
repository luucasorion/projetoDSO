from telas.tela_farmacia import TelaFarmacia
from modelos.medicamento import Medicamento

class ControllerFarmacia:
    def __init__(self):
        self.__telaFarmacia = TelaFarmacia()
        self.__medicamentos = [] 

    def incluirMedicamento(self):
        dados = self.__telaFarmacia.pegarDadosMedicamento()
        if self.pegarMedicamentoPorNome(dados['nome']) is not None:
            self.__telaFarmacia.mostrarMensagem("Medicamento já cadastrado!")
            return
        novo_medicamento = Medicamento(dados['nome'], dados['quantidade'])
        self.__medicamentos.append(novo_medicamento)
        self.__telaFarmacia.mostrarMensagem("Medicamento incluído com sucesso.")

    def alterarMedicamento(self):
        self.listarMedicamentos()
        nome = self.__telaFarmacia.selecionarMedicamento()
        medicamento = self.pegarMedicamentoPorNome(nome)
        if medicamento:
            novosDados = self.__telaFarmacia.pegarDadosMedicamento()
            medicamento.nome = novosDados['nome']
            medicamento.quantidade = novosDados['quantidade']
            self.__telaFarmacia.mostrarMensagem("Medicamento alterado com sucesso.")
        else:
            self.__telaFarmacia.mostrarMensagem("Medicamento não encontrado.")

    def excluirMedicamento(self):
        self.listarMedicamentos()
        nome = self.__telaFarmacia.selecionarMedicamento()
        medicamento = self.pegarMedicamentoPorNome(nome)
        if medicamento:
            self.__medicamentos.remove(medicamento)
            self.__telaFarmacia.mostrarMensagem("Medicamento excluído com sucesso.")
        else:
            self.__telaFarmacia.mostrarMensagem("Medicamento não encontrado.")

    def listarMedicamentos(self):
        if not self.__medicamentos:
            self.__telaFarmacia.mostrarMensagem("Nenhum medicamento cadastrado.")
            return
        for med in self.__medicamentos:
            self.__telaFarmacia.mostrarMedicamento(med)

    def pegarMedicamentoPorNome(self, nome):
        for med in self.__medicamentos:
            if med.nome.lower() == nome.lower():
                return med
        return None

    def abreTela(self):
        opcoes = {
            1: self.incluirMedicamento,
            2: self.alterarMedicamento,
            3: self.listarMedicamentos,
            4: self.excluirMedicamento,
            0: exit
        }
        while True:
            opcao = self.__telaFarmacia.telaOpcoes()
            if opcao in opcoes:
                opcoes[opcao]()
            else:
                self.__telaFarmacia.mostrarMensagem("Opção inválida. Tente novamente.")
