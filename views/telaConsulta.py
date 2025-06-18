from datetime import datetime

class TelaConsulta:

    def telaOpcoes(self):
        while True:
            print("\n-------- Consultas ----------\n"
                  "1 - Incluir consulta\n"
                  "2 - Alterar consulta\n"
                  "3 - Listar consultas\n"
                  "4 - Excluir consulta\n"
                  "0 - Retornar")
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def pegarDadosConsulta(self):
        print("\n-------- DADOS DA CONSULTA ----------")

        cpf_paciente = input("CPF do Paciente: ").strip()
        while not cpf_paciente:
            print("O CPF do paciente não pode ser vazio.")
            cpf_paciente = input("CPF do Paciente: ").strip()

        crm_medico = input("CRM do Médico: ").strip()
        while not crm_medico:
            print("O CRM do médico não pode ser vazio.")
            crm_medico = input("CRM do Médico: ").strip()

        while True:
            data_input = input("Data da consulta (DD/MM/AAAA): ").strip()
            try:
                data = datetime.strptime(data_input, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Data inválida. Use o formato DD/MM/AAAA.")

        while True:
            horario_input = input("Horário da consulta (HH:MM): ").strip()
            try:
                horario = datetime.strptime(horario_input, "%H:%M").time()
                break
            except ValueError:
                print("Horário inválido. Use o formato HH:MM.")

        return {
            "CPF_Paciente": cpf_paciente,
            "CRM_Medico": crm_medico,
            "Data": data,
            "Horario": horario
        }

    def mostrarConsulta(self, dadosConsulta):
        print(f"\nCPF DO PACIENTE: {dadosConsulta.get('CPF')}\n"
              f"CRM DO MÉDICO: {dadosConsulta.get('CRM_Medico')}\n"
              f"DATA DA CONSULTA: {dadosConsulta.get('Data').strftime('%d/%m/%Y')}\n"
              f"HORÁRIO DA CONSULTA: {dadosConsulta.get('Horario').strftime('%H:%M')}\n")

    def selecionarConsulta(self):
        cpf_paciente = input("\nCPF do paciente da consulta que deseja selecionar: ").strip()
        while not cpf_paciente:
            print("O CPF não pode ser vazio.")
            cpf_paciente = input("CPF do paciente da consulta que deseja selecionar: ").strip()

        while True:
            data_input = input("Data da consulta (DD/MM/AAAA): ").strip()
            try:
                data = datetime.strptime(data_input, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Data inválida. Use o formato DD/MM/AAAA.")

        return cpf_paciente, data

    def mostrarMensagem(self, msg):
        print(f"\n{msg}")
