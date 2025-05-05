from views.viewMedico import TelaMedico
from models.medico import Medico


class ControllerMedico(Medico, TelaMedico):
    def __init__(self, crm, nome, especialidade):
        super().__init__(crm, nome, especialidade)
        self.__medicos = []
        self.__telaMedicos = TelaMedico

    def incluirMedico(self):
        informacoes = self.__telaMedicos.pegarDadosMedico()
        crmMedico = self.escolherMedico(informacoes["CRM"])
        
        if crmMedico is None:
            self.__medicos.append(informacoes)
            return
        self.__telaMedicos.mostraMensagem("ATENÇÃO: Medico já cadastrado!!!")


    def selecionarMedico(self):
        self.listarMedicos()
        informacoes = TelaMedico.selecionarMedico()
        for medico in self.__medicos:
            if medico[0] == informacoes:
                return medico
    
    def alterarMedico(self):
        self.listarMedicos()
        crm = self.__telaMedicos.selecionarMedico()
        medico = self.pega_livro_por_codigo(crm)
        
        if(medico is not None):
            novosDadosMedico = self.__telaMedicos.pegarDadosMedico()
            medico.nome = novosDadosMedico["nome"]
            medico.crm = novosDadosMedico["CRM"]
            self.listarMedicos()
        else:
            self.__telaMedicos.mostrarMensagem("ATENCAO: medico não existente")
        
    def excluirMedico(self):
        self.listarMedicos()
        informacoes = TelaMedico.selecionarMedico()
        for medico in self.__medicos:
            if medico[0] == informacoes: 
                self.__medicos.remove(medico)
                return
            
    def listarMedicos(self):    
        for medico in self.__medicos:
    
            self.__telaMedicos.mostrarMedico({"titulo": medico.nome, "CRM": medico.crm})
    
    def abreTela(self):
        listaOpcoes = {1: self.incluirMedico, 2: self.alterarMedico, 3: self.listarMedicos, 4: self.excluirMedico, 0: self.re}

        continua = True
        while continua:
            listaOpcoes[self.__telaMedicos.telaOpcoes()]()

    
