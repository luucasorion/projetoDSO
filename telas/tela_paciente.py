import re
from excecoes.excecao_campo_vazio import CampoVazioException
from excecoes.excecao_formato_invalido import FormatoInvalidoException

class TelaPaciente:

    def tela_opcoes(self):
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

    def pegar_dados_paciente(self):
        print("\n-------- DADOS DO PACIENTE ----------")
        while True:
            try:
                cpf = input("CPF: ").strip()
                if not cpf:
                    raise CampoVazioException("CPF")
                if not re.match(r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$", cpf):
                    raise FormatoInvalidoException("CPF", "000.000.000-00")

                nome = input("Nome: ").strip()
                if not nome:
                    raise CampoVazioException("Nome")
                if not re.match(r"^[A-Za-zÀ-ÿ\s]{3,}$", nome):
                    raise FormatoInvalidoException("Nome", "mínimo 3 caracteres, apenas letras e espaços")

                idade = input("Idade: ").strip()
                if not idade:
                    raise CampoVazioException("Idade")
                if not idade.isdigit():
                    raise FormatoInvalidoException("Idade", "número inteiro positivo")
                idade_int = int(idade)
                if idade_int < 0 or idade_int > 130:
                    raise FormatoInvalidoException("Idade", "valor realista entre 0 e 130")

                telefone = input("Telefone: ").strip()
                if not telefone:
                    raise CampoVazioException("Telefone")
                if not re.match(r"^\(?\d{2}\)?\s?\d{4,5}\-?\d{4}$", telefone):
                    raise FormatoInvalidoException("Telefone", "formato válido, ex: (00) 00000-0000")

                return {"CPF": cpf, "Nome": nome, "Idade": idade_int, "Telefone": telefone}
            except (CampoVazioException, FormatoInvalidoException) as e:
                print(e)

    def mostrar_paciente(self, dadosPaciente):
        print(f"\nNOME DO PACIENTE: {dadosPaciente.get('Nome')}\n"
              f"CPF DO PACIENTE: {dadosPaciente.get('CPF')}\n"
              f"Idade DO PACIENTE: {dadosPaciente.get('Idade')}\n"
              f"Telefone DO PACIENTE: {dadosPaciente.get('Telefone')}\n")

    def selecionar_paciente_por_cpf(self):
        while True:
            try:
                cpf = input("\nCPF do paciente que deseja selecionar: ").strip()
                if not cpf:
                    raise CampoVazioException("CPF")
                if not re.match(r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$", cpf):
                    raise FormatoInvalidoException("CPF", "000.000.000-00")
                return cpf
            except (CampoVazioException, FormatoInvalidoException) as e:
                print(e)

    def mostrar_mensagem(self, msg):
        print(f"\n{msg}")
