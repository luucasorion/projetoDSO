class FormatoInvalidoException(Exception):
    def __init__(self, campo=None, exemplo=None):
        if campo:
            mensagem = f"O campo '{campo}' está em formato inválido."
        else:
            mensagem = "Formato inválido."
        if exemplo:
            mensagem += f" Exemplo esperado: {exemplo}"
        super().__init__(mensagem)
