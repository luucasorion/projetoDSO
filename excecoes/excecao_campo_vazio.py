class CampoVazioException(Exception):
    def __init__(self, campo=None):
        mensagem = f"O campo '{campo}' não pode ser vazio." if campo else "Campo obrigatório vazio."
        super().__init__(mensagem)
