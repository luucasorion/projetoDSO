from datetime import datetime

class TelaConsulta:

    def tela_opcoes(self):
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

    def pegar_dados_consulta(self):
        print("\n-------- DADOS DA CONSULTA ----------")

        cpf_paciente = input("CPF do Paciente: ").strip()
        while not cpf_paciente:
            print("O CPF do paciente não pode ser vazio.")
            cpf_paciente = input("CPF do Paciente: ").strip()

        crm_medico = input("CRM do Médico: ").strip()
        while not crm_medico:
            print("O CRM do médico não pode ser vazio.")
            crm_medico = input("CRM do Médico: ").strip()
        
        id_consulta = input("ID da Consulta: ").strip()
        while not id_consulta:
            print("O ID da consulta não pode ser vazio.")
            crm_medico = input("ID da Consulta: ").strip()
        
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
                hora = datetime.strptime(horario_input, "%H:%M").time()
                break
            except ValueError:
                print("Horário inválido. Use o formato HH:MM.")

        return {
            "CPF_paciente": cpf_paciente,
            "CRM_medico": crm_medico,
            "ID_consulta": id_consulta,
            "Data": data,
            "Hora": hora
        }

    def mostrar_consulta(self, dados_consulta):
        print(f"\nCPF DO PACIENTE: {dados_consulta.get('CPF_paciente')}\n"
              f"CRM DO MÉDICO: {dados_consulta.get('CRM_medico')}\n"
              f"ID DA CONSULTA: {dados_consulta.get('ID_consulta')}\n"
              f"DATA DA CONSULTA: {dados_consulta.get('Data').strftime('%d/%m/%Y')}\n"
              f"HORÁRIO DA CONSULTA: {dados_consulta.get('Hora').strftime('%H:%M')}\n")

    def selecionar_consulta(self):
        ID_consulta = input("\nID da consulta que deseja selecionar: ").strip()
        while not ID_consulta:
            print("O ID não pode ser vazio.")
            ID_consulta = input("ID da consulta que deseja selecionar: ").strip()
        return ID_consulta
       

    def mostrar_mensagem(self, msg):
        print(f"\n{msg}")
