from dados.dao.medico_DAO import MedicoDAO
from telas.tela_medico import TelaMedico
from modelos.medico import Medico



class ControladorMedico():
    def __init__(self, controladorSistemas):
        self.__tela_medicos = TelaMedico()
        self.__controlador_sistema = controladorSistemas
        self.__medico_dao = MedicoDAO()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_medico, 
            2: self.alterar_medico, 
            3: self.listar_medicos,
            4: self.excluir_medico_por_crm,
            0: self.retornar
        }
        continua = True
        while continua:
            lista_opcoes[self.__tela_medicos.tela_opcoes()]()
 
    def incluir_medico(self):
        dados_medico = self.__tela_medicos.pegar_dados_medico()
        crm = dados_medico["CRM"]
        medico_existe = self.selecionar_medico_por_crm(crm)
        if medico_existe is None:
            medico = Medico(dados_medico["CRM"], dados_medico["Nome"], dados_medico["Especialidade"])
            self.__medico_dao.add(crm, medico)
       
        else:
            self.__tela_medicos.mostrar_mensagem("ATENCAO: medico já existente")
            

    def selecionar_medico_por_crm(self, crm):
        for medico in self.__medico_dao.get_all():
            if(medico.identidade == crm):
                return medico
        return None
    
    def alterar_medico(self):
        self.listar_medicos()
        crm = self.__tela_medicos.selecionar_medico_por_crm()
        medico = self.selecionar_medico_por_crm(crm)
        
        if(medico is not None):
            novos_dados_medico = self.__tela_medicos.pegar_dados_medico()
            medico.nome = novos_dados_medico["Nome"]
            medico.identidade = novos_dados_medico["CRM"]
            medico.especialidade = novos_dados_medico["Especialidade"]
            self.listar_medicos()
        else:
            self.__tela_medicos.mostrar_mensagem("ATENCAO: medico não existente")
        
    def excluir_medico_por_crm(self):
        self.listar_medicos()
        
        crm = self.__tela_medicos.selecionar_medico_por_crm()
        medico = self.selecionar_medico_por_crm(crm)
        
        if(medico is not None):
            self.__medico_dao.remove(crm)
            return 
        self.__tela_medicos.mostrar_mensagem("ATENCAO: medico não existente")
       
            
    def listar_medicos(self):
        if self.__medico_dao is not None:    
            for medico in self.__medico_dao.get_all():
                self.__tela_medicos.mostrar_medico({"Nome": medico.nome, "CRM": medico.identidade, "Especialidade" : medico.especialidade})
            return
        print("nao ha medicos para lsitar!")
        return
    
    def retornar(self):
        self.__medico_dao.save()
        self.__controlador_sistema.inicializarSistema()
        
        

    


    
