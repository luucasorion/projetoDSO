from abc import ABC, abstractmethod
class ControladorBase(ABC):
    def __init__(self, controlador_sistema):
        self._controlador_sistema = controlador_sistema
        self._dao = self._get_dao()
        self._tela = self._get_tela()

    @abstractmethod
    def _get_dao(self):
        pass

    @abstractmethod
    def _get_tela(self):
        pass

    @abstractmethod
    def _criar_objeto(self, dados):
        pass

    @abstractmethod
    def _mostrar_entidade(self, entidade):
        pass

    @abstractmethod
    def _pegar_dados(self):
        pass

    @abstractmethod
    def _selecionar_identificador(self):
        pass

    @abstractmethod
    def _get_identidade(self, entidade):
        pass

    def abre_tela(self):
        opcoes = {
            1: self.incluir,
            2: self.alterar,
            3: self.listar,
            4: self.excluir,
            0: self.retornar
        }

        while True:
            opcao = self._tela.tela_opcoes()
            if opcao in opcoes:
                opcoes[opcao]()
            else:
                self._tela.mostrar_mensagem("Opção inválida!")

    def incluir(self):
        while True:
            try:
                dados = self._pegar_dados()
                break
            except Exception as e:
                self._tela.mostrar_mensagem(str(e))

        id_entidade = dados[self._id_chave()]
        if self.selecionar_por_id(id_entidade) is None:
            entidade = self._criar_objeto(dados)
            self._dao.add(id_entidade, entidade)
        else:
            self._tela.mostrar_mensagem("ATENÇÃO: entidade já cadastrada!")

    def selecionar_por_id(self, id_entidade):
        for entidade in self._dao.get_all():
            if self._get_identidade(entidade) == id_entidade:
                return entidade
        return None

    def alterar(self):
        if self.listar() == 1:
            return
        while True:
            try:
                id_entidade = self._selecionar_identificador()
                break
            except Exception as e:
                self._tela.mostrar_mensagem(str(e))
        entidade = self.selecionar_por_id(id_entidade)
        if entidade is not None:
            while True:
                try:
                    novos_dados = self._pegar_dados()
                    break
                except Exception as e:
                    self._tela.mostrar_mensagem(str(e))
            self._atualizar_entidade(entidade, novos_dados)
            self.listar()
        else:
            self._tela.mostrar_mensagem("ATENÇÃO: entidade não encontrada!")

    @abstractmethod
    def _atualizar_entidade(self, entidade, novos_dados):
        pass

    def excluir(self):
        if self.listar() == 1:
            return
        while True:
            try:
                id_entidade = self._selecionar_identificador()
                break
            except Exception as e:
                self._tela.mostrar_mensagem(str(e))

        self.exclui_filiado(id_entidade)
        entidade = self.selecionar_por_id(id_entidade)
        if entidade is not None:
            self._dao.remove(id_entidade)
            self._tela.mostrar_mensagem("Entidade removida!")
        else:
            self._tela.mostrar_mensagem("ATENÇÃO: entidade não encontrada!")

    def listar(self):
        entidades = self._dao.get_all()
        if entidades:
            for entidade in entidades:
                self._mostrar_entidade(entidade)
        else:
            print("Não há entidades para listar!")
            return 1

    def retornar(self):
        self._dao.save()
        self._controlador_sistema.inicializar_sistema()

    @abstractmethod
    def _id_chave(self):
        pass

    def exclui_filiado(self, id_entidade):
        pass
