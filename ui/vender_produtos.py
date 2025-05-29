import logging

from customtkinter import *

import controllers.controle_janela

def iniciar_venda(usuario):
    janela_vender = CTkToplevel()
    janela_vender.title(f"{usuario.nome} - Vender Produto")
    controllers.controle_janela.centralizar_janela(janela_vender, 700, 550)
    controllers.controle_janela.inserir_icon(janela_vender, "logo")
    janela_vender.resizable(False, False)
    janela_vender.grab_set()
    janela_vender.focus()

    janela_vender.mainloop()
