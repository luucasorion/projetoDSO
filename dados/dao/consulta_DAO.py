from dados.dao.abstract_DAO import DAO

class ConsultaDAO(DAO):
    def __init__(self):
        super().__init__("dados/consulta.pkl")
       