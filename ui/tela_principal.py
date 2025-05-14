import logging

from customtkinter import *

from PIL import Image

from controllers.controle_janela import centralizar_janela
from controllers import controle_usuario
from controllers import controle_mensagens
from controllers import controle_telaprincipal
from controllers.controle_janela import inserir_icon

class TelaPrincipal:
    def __init__(self, id_usuario, is_logado):
        self.id_usuario = id_usuario
        self.is_logado = is_logado

    def iniciar(self):
        self.janela_principal = CTk()
        self.janela_principal.title("Estoque")
        centralizar_janela(self.janela_principal, 1250, 750)
        controle_usuario.ControleUsuario.iniciar_turno(self.id_usuario, self.is_logado)
        usuario = controle_usuario.ControleUsuario.iniciar_usuario(self.id_usuario)
        nome_usuario = usuario.nome
        self.janela_principal.resizable(False, False)

        frame_principal = CTkFrame(master=self.janela_principal, fg_color="blue", width=1250, height=750)
        frame_principal.pack()
        frame_principal.propagate(0)

        frame_menu = CTkFrame(master=frame_principal, fg_color="black", width=250, height=750)
        frame_menu.pack(anchor="w")
        frame_menu.propagate(0)

        frame_usuario = CTkFrame(master=frame_menu, fg_color="transparent", border_color="gray", border_width=1, width=250, height=100)
        frame_usuario.pack(anchor="nw")
        frame_usuario.propagate(0)

        frame_bemvindo = CTkFrame(master=frame_usuario, fg_color="transparent", width=85, height=15)
        frame_bemvindo.place(rely=0.41, relx=0.35, anchor="w")
        frame_bemvindo.pack_propagate(False)

        frame_nome = CTkFrame(master=frame_usuario, fg_color="transparent", width=85, height=15)
        frame_nome.place(rely=0.58, relx=0.35, anchor="w")
        frame_nome.pack_propagate(False)

        texto_label = CTkLabel(master=frame_bemvindo, text="Bem Vindo,", text_color="white", font=CTkFont(size=16))
        texto_label.pack(anchor="w", pady=0)
        nome_label = CTkLabel(master=frame_nome, text=nome_usuario, text_color="white", font=CTkFont(size=16))
        nome_label.pack(anchor="w", pady=0)

        try:
            account_img_data = Image.open("assets/images/account_img.png")
            account_img = CTkImage(light_image=account_img_data, size=(50, 50))
        except Exception as error:
            print(f"erro: {error}")
            return

        img_botao = CTkButton(master=frame_usuario, image=account_img, width=50, height=50, fg_color="transparent",
                              hover=False, text="",
                              command=lambda: controle_usuario.ControleUsuario.abrir_menu_usuario(
                                self.janela_principal, usuario))
        img_botao.place(rely=0.5, relx=0.2, anchor="center")

        botao_fechar_turno = CTkButton(master=frame_menu, text="Sair/Finalizar Turno",
                                            command=lambda: controle_telaprincipal.fechar(
                                            self.janela_principal, usuario), font=CTkFont(size=16),
                                            corner_radius=15, width=190, height=50)
        botao_fechar_turno.place(rely=0.95, relx=0.5, anchor="s")

        inserir_icon(self.janela_principal, "logo")

        logging.info("Preparando para registrar turno")

        controle_mensagens.CaixaMensagens.info_box("Sucesso", f"Seja bem vindo! {usuario.nome}")
        self.janela_principal.mainloop()
