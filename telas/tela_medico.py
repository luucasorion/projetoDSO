class TelaMedico:

    def tela_opcoes(self):
        while True:
            print("\n-------- Medicos ----------\n"
                  "1 - Incluir medico\n"
                  "2 - Alterar medico\n"
                  "3 - Listar medico\n"
                  "4 - Excluir medico\n"
                  "0 - Retornar")
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def pegar_dados_medico(self):
        print("\n-------- DADOS DO MEDICO ----------")

        crm = input("CRM: ").strip()
        while not crm:
            print("O CRM não pode ser vazio.")
            crm = input("CRM: ").strip()

        nome = input("Nome: ").strip()
        while not nome:
            print("O nome não pode ser vazio.")
            nome = input("Nome: ").strip()

        especialidade = input("Especialidade: ").strip()
        while not especialidade:
            print("A especialidade não pode ser vazia.")
            especialidade = input("Especialidade: ").strip()    

        return {"CRM": crm, "Nome": nome, "Especialidade": especialidade}

    def mostrar_medico(self, dadosMedico):
        print(f"\nNOME DO MEDICO: {dadosMedico.get('Nome')}\n"
              f"CRM DO MEDICO: {dadosMedico.get('CRM')}\n"
              f"ESPECIALIDADE: {dadosMedico.get('Especialidade')}\n")

    def selecionar_medico_por_crm(self):
        crm = input("\nCRM do medico que deseja selecionar: ").strip()
        while not crm:
            print("O CRM não pode ser vazio.")
            crm = input("CRM do medico que deseja selecionar: ").strip()
        return crm

    def mostrar_mensagem(self, msg):
        print(f"\n{msg}")
