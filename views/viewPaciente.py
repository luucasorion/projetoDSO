class TelaPaciente:

    def telaOpcoes(self):
        while True:
            print("\n-------- Pacientes ----------\n"
                  "1 - Incluir paciente\n"
                  "2 - Alterar paciente\n"
                  "3 - Listar paciente\n"
                  "4 - Excluir paciente\n"
                  "0 - Retornar")
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def pegarDadosPaciente(self):
        print("\n-------- DADOS DO PACIENTE ----------")

        cpf = input("CPF: ").strip()
        while not cpf:
            print("O CPF não pode ser vazio.")
            cpf = input("CPF: ").strip()

        nome = input("Nome: ").strip()
        while not nome:
            print("O nome não pode ser vazio.")
            nome = input("Nome: ").strip()
       
        idade = input("Idade: ").strip()
        while not idade:
            print("O idade não pode ser vazio.")
            idade = input("Idade: ").strip()
        
        telefone = input("Telefone: ").strip()
        while not telefone:
            print("O telefone não pode ser vazio.")
            telefone = input("telefone: ").strip()

        return {"CPF": cpf, "Nome": nome, "Idade" : idade, "Telefone" : telefone }

    def mostrarPaciente(self, dadosPaciente):
        print(f"\nNOME DO PACIENTE: {dadosPaciente.get('Nome')}\n"
              f"CPF DO PACIENTE: {dadosPaciente.get('CPF')}\n"
              f"Idade DO PACIENTE: {dadosPaciente.get('Idade')}\n"
              f"Telefone DO PACIENTE: {dadosPaciente.get('Telefone')}\n")

    def selecionarPaciente(self):
        cpf = input("\nCPF do paciente que deseja selecionar: ").strip()
        while not cpf:
            print("O CPF não pode ser vazio.")
            cpf = input("CPF do paciente que deseja selecionar: ").strip()
        return cpf

    def mostrarMensagem(self, msg):
        print(f"\n{msg}")
