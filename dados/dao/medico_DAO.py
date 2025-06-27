from dados.dao.abstract_DAO import DAO

class MedicoDAO(DAO):
    def __init__(self):
        super().__init__("dados/medico.pkl")
       