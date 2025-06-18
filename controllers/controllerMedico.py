import pickle
from views.viewMedico import TelaMedico
from models.medico import Medico



class ControllerMedico():
    def __init__(self, controladorSistemas):
        super().__init__()
        self.__medicos = []
        self.__telaMedicos = TelaMedico()
        self.__controlador_sistema = controladorSistemas

    
    def incluirMedico(self):
        dados_medico = self.__telaMedicos.pegarDadosMedico()
        crm = self.selecionarMedicoPorCrm(dados_medico["CRM"])
        if crm is None:
            medico = Medico(dados_medico["CRM"], dados_medico["Nome"], dados_medico["Especialidade"])
            self.__medicos.append(medico)
       
           
        else:
            self.__telaMedicos.mostrarMensagem("ATENCAO: medico já existente")
            

    def selecionarMedicoPorCrm(self, crm):
        for medico in self.__medicos:
            if(medico.identidade == crm):
                return medico
        return None
    
    def alterarMedico(self):
        self.listarMedicos()
        crm = self.__telaMedicos.selecionarMedico()
        medico = self.selecionarMedicoPorCrm(crm)
        
        if(medico is not None):
            novosDadosMedico = self.__telaMedicos.pegarDadosMedico()
            medico.nome = novosDadosMedico["Nome"]
            medico.identidade = novosDadosMedico["CRM"]
            medico.especialidade = novosDadosMedico["Especialidade"]
            self.listarMedicos()
        else:
            self.__telaMedicos.mostrarMensagem("ATENCAO: medico não existente")
        
    def excluirMedicoPorCrm(self):
        self.listarMedicos()
        crm = self.__telaMedicos.selecionarMedico()
        medico = self.selecionarMedicoPorCrm(crm)
        
        if(medico is not None):
            for medico in self.__medicos:
             if medico.identidade == crm:
                self.__medicos.remove(medico)
                return 
        self.__telaMedicos.mostrarMensagem("ATENCAO: medico não existente")
       
            
    def listarMedicos(self):    
        for medico in self.__medicos:
    
            self.__telaMedicos.mostrarMedico({"Nome": medico.nome, "CRM": medico.identidade, "Especialidade" : medico.especialidade})
    
    def retornar(self):
        with open("data/medico.pkl", "wb") as f:
            pickle.dump(self.__medicos, f)
        self.__controlador_sistema.abreTela()
        
        

    def abreTela(self):
        with open("data/medico.pkl", "rb") as f:
            nova_pessoa = pickle.load(f)
        self.__medicos = nova_pessoa
        
        listaOpcoes = {
            1: self.incluirMedico, 
            2: self.alterarMedico, 
            3: self.listarMedicos,
            4: self.excluirMedicoPorCrm,
            0: self.retornar
        }

        continua = True
        while continua:
            listaOpcoes[self.__telaMedicos.telaOpcoes()]()



    
