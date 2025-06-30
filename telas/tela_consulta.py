from datetime import datetime

class TelaConsulta:

    def tela_opcoes(self):
        while True:
            print("\n-------- Consultas ----------\n"
                  "1 - Incluir consulta\n"
                  "2 - Alterar consulta\n"
                  "3 - Listar consultas\n"
                  "4 - Listar consultas por CRM\n"
                  "5 - Listar consultas por CPF\n"
                  "6 - Excluir consulta\n"
                  "0 - Retornar")
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4, 5, 6]:
                    return opcao
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def pegar_dados_consulta(self):
        print("\n-------- DADOS DA CONSULTA ----------")

        cpf = input("CPF do Paciente: ").strip()
        while not cpf:
            print("O CPF do paciente não pode ser vazio.")
            cpf = input("CPF do Paciente: ").strip()

        crm = input("CRM do Médico: ").strip()
        while not crm:
            print("O CRM do médico não pode ser vazio.")
            crm = input("CRM do Médico: ").strip()
        
        identidade = input("ID da Consulta: ").strip()
        while not identidade:
            print("O ID da consulta não pode ser vazio.")
            identidade = input("ID da Consulta: ").strip()
        
        while True:
            data_input = input("Data da consulta (DD/MM/AAAA): ").strip()
            try:
                data = datetime.strptime(data_input, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Data inválida. Use o formato DD/MM/AAAA.")

        while True:
            hora_input = input("Horário da consulta (HH:MM): ").strip()
            try:
                hora = datetime.strptime(hora_input, "%H:%M").time()
                break
            except ValueError:
                print("Horário inválido. Use o formato HH:MM.")

        return {
            "CPF": cpf,
            "CRM": crm,
            "Identidade": identidade,
            "Data": data,
            "Hora": hora
        }

    def mostrar_consulta(self, dados_consulta):
        print(f"\nCPF DO PACIENTE: {dados_consulta.get('CPF')}\n"
              f"CRM DO MÉDICO: {dados_consulta.get('CRM')}\n"
              f"ID DA CONSULTA: {dados_consulta.get('Identidade')}\n"
              f"DATA DA CONSULTA: {dados_consulta.get('Data').strftime('%d/%m/%Y')}\n"
              f"HORÁRIO DA CONSULTA: {dados_consulta.get('Hora').strftime('%H:%M')}\n")

    def selecionar_consulta(self):
        identidade = input("\nID da consulta que deseja selecionar: ").strip()
        while not identidade:
            print("O ID não pode ser vazio.")
            identidade = input("ID da consulta que deseja selecionar: ").strip()
        return identidade
       

    def mostrar_mensagem(self, msg):
        print(f"\n{msg}")
