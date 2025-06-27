class TelaFarmacia:

    def telaOpcoes(self):
        while True:
            print("\n-------- Farmácia ----------")
            print("1 - Incluir medicamento")
            print("2 - Alterar medicamento")
            print("3 - Listar medicamentos")
            print("4 - Excluir medicamento")
            print("0 - Retornar")
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in (0, 1, 2, 3, 4):
                    return opcao
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def pegarDadosMedicamento(self):
        print("\n-------- DADOS DO MEDICAMENTO ----------")

        nome = input("Nome do medicamento: ").strip()
        while not nome:
            print("O nome do medicamento não pode ser vazio.")
            nome = input("Nome do medicamento: ").strip()

        while True:
            try:
                quantidade = int(input("Quantidade: "))
                if quantidade < 0:
                    print("A quantidade não pode ser negativa.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro para a quantidade.")

        return {"nome": nome, "quantidade": quantidade}

    def mostrarMedicamento(self, dadosMedicamento):
        print("\n-------- DADOS DO MEDICAMENTO ----------")
        print(f"Nome: {dadosMedicamento.get('nome', 'N/A')}")
        print(f"Quantidade: {dadosMedicamento.get('quantidade', 'N/A')}")

    def selecionarMedicamento(self):
        nome = input("\nInforme o nome do medicamento que deseja selecionar: ").strip()
        while not nome:
            print("O nome do medicamento não pode ser vazio.")
            nome = input("Informe o nome do medicamento que deseja selecionar: ").strip()
        return nome

    def mostrarMensagem(self, msg):
        print(f"\n{msg}")
