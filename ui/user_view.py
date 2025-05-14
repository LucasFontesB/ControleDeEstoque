from customtkinter import *

from PIL import Image

from controllers.controle_janela import inserir_icon, centralizar_janela
from controllers import controle_userview

def iniciar(janela, usuario):
    nome = usuario.nome
    senha = usuario.senha

    is_adm = usuario.adm
    is_adm_formatado = None
    if is_adm == 1:
        is_adm_formatado = "Sim"
    else:
        is_adm_formatado = "Não"

    id = usuario.id
    data_criacao = usuario.data_criacao
    usuario_criacao = usuario.usuario_criacao

    user_view = CTkToplevel()
    user_view.title(f"Perfil - {nome}")
    user_view.resizable(False, False)
    user_view.grab_set()
    user_view.focus()
    centralizar_janela(user_view, 500, 250)
    inserir_icon(user_view, "account")

    frame_principal = CTkFrame(master=user_view, height=250, width=500, fg_color="transparent")
    frame_principal.pack()

    try:
        img_data = Image.open("assets/images/account_img.png")
        img = CTkImage(light_image=img_data, size=(180, 180))
    except Exception as error:
        print(f"erro: {error}")
        return

    frame_img = CTkFrame(master=frame_principal, height=200, width=200, fg_color="transparent")
    frame_img.place(rely=0, relx=1, anchor="ne")
    img_label = CTkLabel(master=frame_img, image=img, text="")
    img_label.place(rely=0.05, relx=0.05)

    user_info_frame = CTkFrame(master=frame_principal, height=200, width=300, fg_color="transparent")
    user_info_frame.place(rely=0, relx=0, anchor="nw")

    nome_frame = CTkFrame(master=user_info_frame, width=75, fg_color="transparent")
    nome_frame.place(rely=0, relx=0)
    nome_label = CTkLabel(master=nome_frame, text="Nome")
    nome_label.pack(pady=0, padx=10, anchor="nw")
    nome_entry = CTkEntry(master=nome_frame, width=125)
    nome_entry.pack(pady=0, padx=10, anchor="nw")
    nome_entry.insert(0, nome)
    nome_entry.configure(state="disable", text_color="gray")

    id_frame = CTkFrame(master=user_info_frame, fg_color="transparent")
    id_frame.place(rely=0, relx=0.5)
    id_label = CTkLabel(master=id_frame, text="Id Do Usuário")
    id_label.pack(pady=0, padx=10, anchor="nw")
    id_entry = CTkEntry(master=id_frame, width=125)
    id_entry.pack(pady=0, padx=10, anchor="nw")
    id_entry.insert(0, id)
    id_entry.configure(state="disable", text_color="gray")

    senha_frame = CTkFrame(master=user_info_frame, fg_color="transparent")
    senha_frame.place(rely=0.3, relx=0)
    senha_label = CTkLabel(master=senha_frame, text="Senha")
    senha_label.pack(pady=0, padx=10, anchor="nw")
    senha_entry = CTkEntry(master=senha_frame, show="*", width=125)
    senha_entry.pack(pady=0, padx=10, anchor="nw")
    senha_entry.insert(0, senha)
    senha_entry.configure(state="disable", text_color="gray")

    is_adm_frame = CTkFrame(master=user_info_frame, fg_color="transparent")
    is_adm_frame.place(rely=0.3, relx=0.5)
    is_adm_label = CTkLabel(master=is_adm_frame, text="Usuario ADM")
    is_adm_label.pack(pady=0, padx=10, anchor="nw")
    is_adm_entry = CTkEntry(master=is_adm_frame, width=125)
    is_adm_entry.pack(pady=0, padx=10, anchor="nw")
    is_adm_entry.insert(0, is_adm_formatado)
    is_adm_entry.configure(state="disable", text_color="gray")

    data_criacao_frame = CTkFrame(master=user_info_frame, fg_color="transparent")
    data_criacao_frame.place(rely=0.6, relx=0)
    data_criacao_label = CTkLabel(master=data_criacao_frame, text="Data De Criação")
    data_criacao_label.pack(pady=0, padx=10, anchor="nw")
    data_criacao_entry = CTkEntry(master=data_criacao_frame, width=125)
    data_criacao_entry.pack(pady=0, padx=10, anchor="nw")
    data_criacao_entry.insert(0, data_criacao)
    data_criacao_entry.configure(state="disable", text_color="gray")

    usuario_criacao_frame = CTkFrame(master=user_info_frame, fg_color="transparent")
    usuario_criacao_frame.place(rely=0.6, relx=0.5)
    usuario_criacao_label = CTkLabel(master=usuario_criacao_frame, text="Criado Por")
    usuario_criacao_label.pack(pady=0, padx=10, anchor="nw")
    usuario_criacao_entry = CTkEntry(master=usuario_criacao_frame, width=125)
    usuario_criacao_entry.pack(pady=0, padx=10, anchor="nw")
    usuario_criacao_entry.insert(0, usuario_criacao)
    usuario_criacao_entry.configure(state="disable", text_color="gray")

    frame_botao = CTkFrame(master=frame_principal, width=500, height=50, fg_color="transparent")
    frame_botao.place(rely=0.75, relx=0)

    botao_cancelar = CTkButton(master=frame_botao, text="Cancelar", width=100, height=25, font=CTkFont(size=22),
                               corner_radius=20, command=lambda: controle_userview.cancelar(user_view))
    botao_cancelar.place(rely=0.3, relx=0.05)

    botao_salvar = CTkButton(master=frame_botao, text="Salvar", width=100, height=25, font=CTkFont(size=22),
                             corner_radius=20, command=lambda: controle_userview.salvar(
                            entry_nome=nome_entry, entry_senha=senha_entry, entry_isadm=is_adm_entry,
                            botao_editar=botao_editar, botao_salvar=botao_salvar, nome_atual=nome, senha_atual=senha,
                            isadm_atual=is_adm_formatado, id_usuario=id, janela=janela))
    botao_salvar.place(rely=0.3, relx=0.41)
    botao_salvar.configure(state="disable", text_color="gray")

    botao_editar = CTkButton(master=frame_botao, text="Editar", width=100, height=25, font=CTkFont(size=22),
                             corner_radius=20, command=lambda: controle_userview.editar_usuario(
                            entry_nome=nome_entry, entry_senha=senha_entry, entry_isadm=is_adm_entry,
                            botao_editar=botao_editar, botao_salvar=botao_salvar))
    botao_editar.place(rely=0.3, relx=0.75)
