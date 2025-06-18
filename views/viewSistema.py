import tkinter as tk

# Cria a janela principal
janela = tk.Tk()

# Define o título da janela
janela.title("Minha Tela Tkinter")

# Define o tamanho da janela (largura x altura)
janela.geometry("400x300")

# Mantém a janela aberta
janela.mainloop()




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