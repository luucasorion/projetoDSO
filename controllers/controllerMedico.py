from data.dao.medico_DAO import MedicoDAO
from views.viewMedico import TelaMedico
from models.medico import Medico



class ControllerMedico():
    def __init__(self, controladorSistemas):
        self.__telaMedicos = TelaMedico()
        self.__controlador_sistema = controladorSistemas
        self.__medico_dao = MedicoDAO()

    
    def incluirMedico(self):
        dados_medico = self.__telaMedicos.pegarDadosMedico()
        crm = dados_medico["CRM"]
        medico_existe = self.selecionarMedicoPorCrm(crm)
        if medico_existe is None:
            medico = Medico(dados_medico["CRM"], dados_medico["Nome"], dados_medico["Especialidade"])
            self.__medico_dao.add(crm, medico)
       
        else:
            self.__telaMedicos.mostrarMensagem("ATENCAO: medico já existente")
            

    def selecionarMedicoPorCrm(self, crm):
        for medico in self.__medico_dao.get_all():
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
            for medico in self.__medico_dao.get_all():
             if medico.identidade == crm:
                self.__medico_dao.remove(medico)
                return 
        self.__telaMedicos.mostrarMensagem("ATENCAO: medico não existente")
       
            
    def listarMedicos(self):
        if self.__medico_dao is not None:    
            for medico in self.__medico_dao.get_all():
                self.__telaMedicos.mostrarMedico({"Nome": medico.nome, "CRM": medico.identidade, "Especialidade" : medico.especialidade})
            return
        print("nao ha medicos para lsitar!")
        return
    
    def retornar(self):
        self.__medico_dao.save()
        self.__controlador_sistema.inicializarSistema()
        
        

    def abreTela(self):
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



    
