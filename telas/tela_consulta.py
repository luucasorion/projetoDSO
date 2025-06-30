from datetime import datetime
import re
from excecoes.excecao_campo_vazio import CampoVazioException
from excecoes.excecao_formato_invalido import FormatoInvalidoException

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
        while True:
            try:
                cpf = input("CPF do Paciente: ").strip()
                if not cpf:
                    raise CampoVazioException("CPF")
                if not re.match(r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$", cpf):
                    raise FormatoInvalidoException("CPF", "000.000.000-00")

                crm = input("CRM do Médico: ").strip()
                if not crm:
                    raise CampoVazioException("CRM")
                if not re.match(r"^.{5,}$", crm):
                    raise FormatoInvalidoException("CRM", "mínimo 5 caracteres")

                identidade = input("ID da Consulta: ").strip()
                if not identidade:
                    raise CampoVazioException("ID da Consulta")

                data_input = input("Data da consulta (DD/MM/AAAA): ").strip()
                try:
                    data = datetime.strptime(data_input, "%d/%m/%Y").date()
                except ValueError:
                    raise FormatoInvalidoException("Data", "DD/MM/AAAA")
                if data < datetime.today().date():
                    raise FormatoInvalidoException("Data", "Data não pode ser no passado")

                hora_input = input("Horário da consulta (HH:MM): ").strip()
                try:
                    hora = datetime.strptime(hora_input, "%H:%M").time()
                except ValueError:
                    raise FormatoInvalidoException("Hora", "HH:MM")

                return {
                    "CPF": cpf,
                    "CRM": crm,
                    "Identidade": identidade,
                    "Data": data,
                    "Hora": hora
                }
            except (CampoVazioException, FormatoInvalidoException) as e:
                print(e)

    def mostrar_consulta(self, dados_consulta):
        print(f"\nCPF DO PACIENTE: {dados_consulta.get('CPF')}\n"
              f"CRM DO MÉDICO: {dados_consulta.get('CRM')}\n"
              f"ID DA CONSULTA: {dados_consulta.get('Identidade')}\n"
              f"DATA DA CONSULTA: {dados_consulta.get('Data').strftime('%d/%m/%Y')}\n"
              f"HORÁRIO DA CONSULTA: {dados_consulta.get('Hora').strftime('%H:%M')}\n")

    def selecionar_consulta(self):
        while True:
            try:
                identidade = input("\nID da consulta que deseja selecionar: ").strip()
                if not identidade:
                    raise CampoVazioException("ID da Consulta")
                return identidade
            except CampoVazioException as e:
                print(e)

    def mostrar_mensagem(self, msg):
        print(f"\n{msg}")
