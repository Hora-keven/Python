from tkinter import *
from tkinter import ttk
import jogo
from jogo import Jogo
import random

telinha = Tk()



class Tela():
    def __init__(self):
        self.telinha = telinha
        self.vida = 5
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.entrada()
        self.lugares()
        self.pessoas()
        telinha.mainloop()

    def tela(self):
        self.telinha.title("Cara a Cara")
        self.telinha.configure(background="#A9A9A9")
        self.telinha.resizable(True, True)

    def frames(self):
        self.frame = Frame(self.telinha, bg="#4682B4", highlightthickness=0.5, highlightbackground="#4682B4")
        self.frame.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)

        self.frame_2 = Frame(self.telinha, bg='#4682B4', highlightthickness=0.5, highlightbackground="#4682B4")
        self.frame_2.place(relx=0.03, rely=0.20, relwidth=0.94, relheight=0.25)

        self.frame_3 = Frame(self.telinha, bg='#4682B4', highlightthickness=0.5, highlightbackground="#4682B4")
        self.frame_3.place(relx=0.03, rely=0.50, relwidth=0.94, relheight=0.45)

    def botoes(self):
        self.botao_dica = Button(self.frame_3,font=("Arial", 13), text="Opção pessoas", command=self.mostra_dica)
        self.botao_dica.place(relx=0.4, rely=0.38, relwidth=0.1, relheight=0.10)

        self.botao_dica1 = Button(self.frame_3,font=("Arial", 13), text="Opção Lugares", command=self.mostra_dica_lugar)
        self.botao_dica1.place(relx=0.51, rely=0.38, relwidth=0.1, relheight=0.10)

        self.botao_confirma = Button(self.frame_2, font=("Arial", 13), text="Confirmar", command=self.confirma_ganho_perda)
        self.botao_confirma.place(relx=0.33, rely=0.40, relwidth=0.1, relheight=0.15)

    def labels(self):
        self.lb_input = Label(self.frame_2, font=("Arial", 15), text='Escreva quem é: ', bg='#4682B4')
        self.lb_input.place(relx=0.005, rely=0.40, relwidth=0.1, relheight=0.15)

        self.lbStatus = Label(self.frame, font=("Arial", 25), text='-=-=-=-=JOGO CARA A CARA-=-=-=-', fg='black', bg='#4682B4')
        self.lbStatus.place(relx=0.05, rely=0.25, relwidth=0.90, relheight=0.21)

        self.lbDica = Label(self.frame_3,font=("Arial", 15), text='', fg='black', bg='#4682B4')
        self.lbDica.place(relx=0.25, rely=0.28, relwidth=0.50, relheight=0.10)

        self.lbganhador_perdedor = Label(self.frame_3, font=("Arial", 15),  text='', fg='red', bg='#4682B4')
        self.lbganhador_perdedor.place(relx=0.05, rely=0.55, relwidth=0.90, relheight=0.10)

    def entrada(self):
        self.entrada_usuario = Entry(self.frame_2)
        self.entrada_usuario.place(relx=0.10, rely=0.41, relwidth=0.20, relheight=0.15)

    def mostra_dica(self):

        self.pessoa.add_dicas('o mais lindo', "gatão", "lindo", " veio de Salvador", "toca violão")

        self.pessoa2.add_dicas("Estuda no IF", "a melhor front-end", "melhor pessoa", "Ama Java",
                          "Mora em uma cidade pequena")

        self.pessoa3.add_dicas("U melhor em python", "o mais gente boa", "Tem uma aparência com Temóteo",
                          "Está no ensino médio", "O mais novo da sala")

        if self.escolha == self.pessoa3.nome:

            return self.lbDica.config(text=f"Dica: {self.pessoa3.sorteia_dicas}")

        elif self.escolha == self.pessoa2.nome:
            return self.lbDica.config(text=f"Dica: {self.pessoa2.sorteia_dicas}")

        elif self.escolha == self.pessoa.nome:
            return self.lbDica.config(text=f"Dica: {self.pessoa.sorteia_dicas}")

    def pessoas(self):

        self.pessoa3 = Jogo("Pedro")
        self.pessoa = Jogo("Keven")
        self.pessoa2 = Jogo("Manuela")
        lista = [self.pessoa.nome, self.pessoa2.nome, self.pessoa3.nome]
        self.escolha = random.choice(lista)

    def lugares(self):
        self.Maranhao = Jogo("Maranhao")

        self.Bahia = Jogo("Bahia")

        self.Sao_Paulo = Jogo("Sao Paulo")

        lista = [self.Maranhao.nome, self.Bahia.nome, self.Sao_Paulo.nome]
        self.escolha1 = random.choice(lista)


    def mostra_dica_lugar(self):
        self.Maranhao.add_dicas('Parque nacional Lençóis freáticos', "Palácio dos leões",
                           "Catedral Metropolitana Nossa Senhora da Vitória",
                           "Parque Nacional da Chapadas da mesa", "Capital São Luis")

        self.Bahia.add_dicas("Elevador Lacerda", "Basilica Senhor do Bonfim", "Mercado Modelo", "Pelourinho",
                        "Salvador")

        self.Sao_Paulo.add_dicas("Parque Ibirapuera", "Mercado Municipal", "Pinacoteca",
                            "Museu do futebol", "Campinas faz parte")

        if self.escolha1 == self.Sao_Paulo.nome:

            return self.lbDica.config(text=f"Dica: {self.Sao_Paulo.sorteia_dicas}")

        elif self.escolha1 == self.Bahia.nome:
            return self.lbDica.config(text=f"Dica: {self.Bahia.sorteia_dicas}")

        elif self.escolha1 == self.Maranhao.nome:
            return self.lbDica.config(text=f"Dica: {self.Maranhao.sorteia_dicas}")

    def confirma_ganho_perda(self):
        if self.entrada_usuario.get() == self.Maranhao.nome or self.entrada_usuario.get() == self.Bahia.nome or self.entrada_usuario.get() == self.Sao_Paulo.nome:
            self.lbganhador_perdedor.config(text="Você ganhou!")

        elif self.entrada_usuario.get() == self.pessoa.nome or self.entrada_usuario.get() == self.pessoa2.nome or self.entrada_usuario.get() == self.pessoa3.nome:
            self.lbganhador_perdedor.config(text="Você ganhou!")

        else:
            self.vida-=1
            self.lbganhador_perdedor.config(text=f"Você errou! você tem {self.vida} de vida!")
            if self.vida <= 0:
                self.lbganhador_perdedor.config(text=f"SUAS CHANCES ACABARAM!!")



