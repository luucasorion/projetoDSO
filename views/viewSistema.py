class ViewSistema:
    #tratar dados
    def tela_opcoes(self):
        print("-------- Sistema ---------")
        print("Escolha sua opcao")
        print("1 - Medicos")
        print("2 - Pacientes")
        print("3 - Consultas")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao