import tkinter as tk
from tkinter import ttk

class ViewSistema:
    def __init__(self, callback):
        self.callback = callback

    def janela_opcoes(self):
        self.janela = tk.Tk()
        self.janela.configure(bg="#fbf3e1")
        self.janela.geometry("400x400")
        estilo = ttk.Style()
        estilo.theme_use('clam')
        self.espaco = tk.Label(self.janela,bg="#fbf3e1", height=2)
        self.espaco.pack()
        texto = ["Medicos", "Pacientes", "Consultas", "Finalizar Sistema"]

        for i in range(4):
            botao = ttk.Button(self.janela, text=texto[i], command=lambda n=i: self.acao_botao(n))
            botao.pack(pady=5, padx=20, fill='x')

        self.janela.mainloop()

    def acao_botao(self, num):
        self.janela.destroy()
        self.callback(num)
