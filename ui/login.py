from PIL import Image

from customtkinter import *

from controllers.controle_janela import centralizar_janela, inserir_icon
from controllers.controle_login import autenticar_usuario

class TelaLogin:
    def __init__(self):
        set_appearance_mode("dark")
        self.janela = CTk()
        self.janela.title("Login - Controle De Estoque")
        centralizar_janela(self.janela, 600, 480)
        inserir_icon(self.janela, "logo")
        self.janela.resizable(False, False)

        try:
            self.logo_data = Image.open("assets/images/logo_img.png")
            self.logo_image = CTkImage(light_image=self.logo_data, size=(300, 300))
        except Exception as error:
            print(f"erro: {error}")
            return

        self.logo_frame = CTkFrame(master=self.janela, width=300, height=480, fg_color="white")
        self.logo_frame.pack(side="left")
        self.logo_label = CTkLabel(master=self.logo_frame, text="", image=self.logo_image)
        self.logo_label.place(relx=0.5, rely=0.5, anchor="center")
        self.logo_frame.propagate(0)

        self.login_frame = CTkFrame(master=self.janela, width=300, height=480, fg_color="black", corner_radius=15)
        self.login_frame.pack(side="right")
        self.login_frame.propagate(0)

        self.frame_teste = CTkFrame(master=self.login_frame, fg_color="transparent")
        self.frame_teste.place(relx=0.5, rely=0.5, anchor="center")

        self.frame_nome = CTkFrame(master=self.frame_teste, fg_color="transparent")
        self.frame_nome.pack(anchor="center", pady=10)
        self.nome_label = CTkLabel(master=self.frame_nome, text="Nome", text_color="white")
        self.nome_label.pack()
        self.nome = CTkEntry(master=self.frame_nome)
        self.nome.pack()

        self.frame_senha = CTkFrame(master=self.frame_teste, fg_color="transparent")
        self.frame_senha.pack(anchor="center", pady=5)
        self.senha_label = CTkLabel(master=self.frame_senha, text="Senha", text_color="white")
        self.senha_label.pack()
        self.senha = CTkEntry(master=self.frame_senha, show="*")
        self.senha.pack()

        self.button = CTkButton(master=self.frame_teste, text="Entrar", command=lambda: autenticar_usuario(
            nome=self.nome.get(), senha=self.senha.get(), janela=self.janela), corner_radius=20)
        self.button.pack(pady=25, anchor="s")

        self.janela.mainloop()
