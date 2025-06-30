from dados.dao.abstract_DAO import DAO

class PacienteDAO(DAO):
    def __init__(self):
        super().__init__("dados/paciente.pkl")
        