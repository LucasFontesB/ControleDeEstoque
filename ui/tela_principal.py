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

        try:
            add_img_data = Image.open("assets/images/add_img.png")
            add_img = CTkImage(light_image=add_img_data, size=(35, 35))
        except Exception as error:
            print(f"erro: {error}")
            return

        botao_adicionarprodutos = CTkButton(master=frame_menu, text=" Adicionar Produtos", font=CTkFont(size=16),
                                            corner_radius=15, width=190, height=50, image=add_img, compound="left",
                                            anchor="center")
        botao_adicionarprodutos.pack(pady=15, anchor="center")
        botao_adicionarprodutos.propagate(0)

        try:
            sell_img_data = Image.open("assets/images/sell_img.png")
            sell_img = CTkImage(light_image=sell_img_data, size=(35, 35))
        except Exception as error:
            print(f"erro: {error}")
            return

        botao_venderprodutos = CTkButton(master=frame_menu, text="  Vender Produtos", font=CTkFont(size=16),
                                            corner_radius=15, width=210, height=50, image=sell_img, compound="left",
                                         anchor="center")
        botao_venderprodutos.pack(anchor="center")
        botao_venderprodutos.propagate(True)

        try:
            stock_img_data = Image.open("assets/images/stock_img.png")
            stock_img = CTkImage(light_image=stock_img_data, size=(35, 35))
        except Exception as error:
            print(f"erro: {error}")
            return

        botao_estoque = CTkButton(master=frame_menu, text="  Abrir Estoque", font=CTkFont(size=16),
                                         corner_radius=15, width=210, height=50, image=stock_img, compound="left",
                                  anchor="center")
        botao_estoque.pack(pady=15, anchor="center")
        botao_estoque.propagate(True)

        try:
            config_img_data = Image.open("assets/images/config_img.png")
            config_img = CTkImage(light_image=config_img_data, size=(35, 35))
        except Exception as error:
            print(f"erro: {error}")
            return

        botao_config = CTkButton(master=frame_menu, text="  Configurações", font=CTkFont(size=16),
                                         corner_radius=15, width=210, height=50, image=config_img, compound="left",
                                 anchor="center")
        botao_config.pack(anchor="center")
        botao_config.propagate(True)

        try:
            quit_img_data = Image.open("assets/images/quit_img.png")
            quit_img = CTkImage(light_image=quit_img_data, size=(35, 35))
        except Exception as error:
            print(f"erro: {error}")
            return

        botao_fechar_turno = CTkButton(master=frame_menu, text=" Sair/Finalizar Turno",
                                            command=lambda: controle_telaprincipal.fechar(
                                            self.janela_principal, usuario), font=CTkFont(size=16),
                                            corner_radius=15, width=210, height=50, image=quit_img,compound="left",
                                       anchor="center")
        botao_fechar_turno.pack(side="bottom", pady=15)
        botao_fechar_turno.propagate(True)

        inserir_icon(self.janela_principal, "logo")

        logging.info("Preparando para registrar turno")

        controle_mensagens.CaixaMensagens.info_box("Sucesso", f"Seja bem vindo! {usuario.nome}")
        self.janela_principal.mainloop()
