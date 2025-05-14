import logging

import tkinter as tk

from customtkinter import *

from controllers.controle_janela import centralizar_janela, inserir_icon

from PIL import Image

class CaixaMensagens:
    largura = 350
    altura = 100
    @staticmethod
    def error_box(titulo, texto):
        error_box = CTkToplevel()
        error_box.title(titulo)
        inserir_icon(error_box, "erro")

        centralizar_janela(error_box, CaixaMensagens.largura, CaixaMensagens.altura)

        error_box.resizable(False, False)

        error_box.grab_set()
        error_box.focus()

        frame_principal = CTkFrame(master=error_box, width=250, height=100)
        frame_principal.pack(side="right")
        frame_principal.propagate(0)

        frame_imagem = CTkFrame(master=error_box, width=100, height=100)
        frame_imagem.pack(side="left")
        frame_imagem.propagate(0)

        try:
            logo_data = Image.open("assets/images/error_img.png")
            logging.debug("Imagem Mensagem Erro Carregada")
            logo_image = CTkImage(light_image=logo_data, size=(65, 65))
        except Exception as error:
            logging.debug(f"Erro Ao Carregar Imagem Mensagem Erro: {error}")
            return

        imagem_label = CTkLabel(master=frame_imagem, text="", image=logo_image)
        imagem_label.place(relx=0.55, rely=0.5, anchor="center")

        mensagem_label = CTkLabel(master=frame_principal, text=texto, text_color="white")
        mensagem_label.pack(anchor="center", pady=10)

        botao = CTkButton(master=frame_principal, text="Ok", command=error_box.destroy)
        botao.pack(pady=10, anchor="s")



    @staticmethod
    def info_box(titulo, texto):
        info_box = CTkToplevel()
        info_box.title(titulo)
        inserir_icon(info_box, "info")

        centralizar_janela(info_box, CaixaMensagens.largura, CaixaMensagens.altura)
        info_box.resizable(False, False)
        info_box.grab_set()
        info_box.focus()

        frame_principal = CTkFrame(master=info_box, width=250, height=100)
        frame_principal.pack(side="right")
        frame_principal.propagate(0)

        frame_imagem = CTkFrame(master=info_box, width=100, height=100)
        frame_imagem.pack(side="left")
        frame_imagem.propagate(0)

        try:
            logo_data = Image.open("assets/images/info_img.png")
            logging.debug("Imagem Mensagem Info Carregada")
            logo_image = CTkImage(light_image=logo_data, size=(65, 65))
        except Exception as error:
            logging.debug(f"Erro Ao Carregar Imagem Mensagem Info: {error}")
            return

        imagem_label = CTkLabel(master=frame_imagem, text="", image=logo_image)
        imagem_label.place(relx=0.55, rely=0.5, anchor="center")

        mensagem_label = CTkLabel(master=frame_principal, text=texto, text_color="white")
        mensagem_label.pack(anchor="center", pady=10)

        botao = CTkButton(master=frame_principal, text="Ok", command=info_box.destroy)
        botao.pack(pady=10, anchor="s")

    @staticmethod
    def conf_box(titulo, texto):

        resposta = tk.StringVar()

        def sim():
            resposta.set("sim")
            conf_box.destroy()
        def nao():
            resposta.set("nao")
            conf_box.destroy()

        conf_box = CTkToplevel()
        conf_box.title(titulo)
        inserir_icon(conf_box, "interrogation")

        centralizar_janela(conf_box, CaixaMensagens.largura, CaixaMensagens.altura)

        conf_box.resizable(False, False)
        conf_box.grab_set()
        conf_box.focus()

        frame_principal = CTkFrame(master=conf_box, width=250, height=100)
        frame_principal.pack(side="right")
        frame_principal.propagate(0)

        frame_imagem = CTkFrame(master=conf_box, width=100, height=100)
        frame_imagem.pack(side="left")
        frame_imagem.propagate(0)

        try:
            logo_data = Image.open("assets/images/interrogation_img.png")
            logging.debug("Imagem Mensagem Interrogation Carregada")
            logo_image = CTkImage(light_image=logo_data, size=(65, 65))
        except Exception as error:
            logging.debug(f"Erro Ao Carregar Imagem Mensagem Info: {error}")
            return

        imagem_label = CTkLabel(master=frame_imagem, text="", image=logo_image)
        imagem_label.place(relx=0.55, rely=0.5, anchor="center")

        mensagem_label = CTkLabel(master=frame_principal, text=texto, text_color="white")
        mensagem_label.pack(anchor="center", pady=10)

        botao_sim = CTkButton(master=frame_principal, text="Sim", command=sim, width=100)
        botao_sim.place(rely=0.78, relx=0.5, anchor="se")

        botao_nao = CTkButton(master=frame_principal, text="Não", command=nao, width=100)
        botao_nao.place(rely=0.5, relx=0.55, anchor="nw")

        conf_box.wait_variable(resposta)
        return resposta.get() == "sim"

