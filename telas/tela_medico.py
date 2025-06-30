import re
from excecoes.excecao_campo_vazio import CampoVazioException
from excecoes.excecao_formato_invalido import FormatoInvalidoException

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
        while True:
            try:
                crm = input("CRM: ").strip()
                if not crm:
                    raise CampoVazioException("CRM")
                if not re.match(r"^.{5,}$", crm):
                    raise FormatoInvalidoException("CRM", "mínimo 5 caracteres")

                nome = input("Nome: ").strip()
                if not nome:
                    raise CampoVazioException("Nome")
                if not re.match(r"^[A-Za-zÀ-ÿ\s]{3,}$", nome):
                    raise FormatoInvalidoException("Nome", "mínimo 3 caracteres, apenas letras e espaços")

                especialidade = input("Especialidade: ").strip()
                if not especialidade:
                    raise CampoVazioException("Especialidade")
                if not re.match(r"^[A-Za-zÀ-ÿ\s]{4,}$", especialidade):
                    raise FormatoInvalidoException("Especialidade", "mínimo 4 caracteres, apenas letras e espaços")

                return {"CRM": crm, "Nome": nome, "Especialidade": especialidade}
            except (CampoVazioException, FormatoInvalidoException) as e:
                print(e)

    def mostrar_medico(self, dadosMedico):
        print(f"\nNOME DO MEDICO: {dadosMedico.get('Nome')}\n"
              f"CRM DO MEDICO: {dadosMedico.get('CRM')}\n"
              f"ESPECIALIDADE: {dadosMedico.get('Especialidade')}\n")

    def selecionar_medico_por_crm(self):
        while True:
            try:
                crm = input("\nCRM do medico que deseja selecionar: ").strip()
                if not crm:
                    raise CampoVazioException("CRM")
                if not re.match(r"^.{5,}$", crm):
                    raise FormatoInvalidoException("CRM", "mínimo 5 caracteres")
                return crm
            except (CampoVazioException, FormatoInvalidoException) as e:
                print(e)

    def mostrar_mensagem(self, msg):
        print(f"\n{msg}")
