import time

from controllers.controle_mensagens import CaixaMensagens
from utils import reiniciar_sistema
from database.db_usuarios import editar_cadastro
from ui.tela_principal import TelaPrincipal


edicao_ativa = 0
def editar_usuario(entry_nome, entry_senha, entry_isadm, botao_editar, botao_salvar):
    global edicao_ativa
    usuario_isadm = entry_isadm.get()
    if usuario_isadm == "Sim":
        edicao_ativa = 1
        entry_nome.configure(state="normal", text_color="white")
        entry_senha.configure(state="normal", text_color="white")
        entry_senha.configure(show="", text_color="white")
        entry_isadm.configure(state="normal", text_color="white")
        botao_salvar.configure(state="normal", text_color="white")
        botao_editar.configure(state="disable", text_color="gray")
    else:
        CaixaMensagens.info_box("Atenção", "Apenas Usuarios ADM Pode Modificar")

def salvar(janela, id_usuario, nome_atual, senha_atual, isadm_atual, entry_nome, entry_senha, entry_isadm, botao_editar, botao_salvar):
    dicionario_sim = ["sim", "s"]
    dicionario_nao = ["nao", "não", "n"]
    dicionario_adm = [1, 0]
    nome_atualizado = entry_nome.get()
    senha_atualizado = entry_senha.get()
    isadm_atualizado = entry_isadm.get()

    adm_formatado = None
    if isadm_atualizado.lower() in dicionario_sim:
        adm_formatado = 1
    elif isadm_atualizado.lower() in dicionario_nao:
        adm_formatado = 0
    else:
        CaixaMensagens.error_box("Erro", "Valor Para ADM Inválido")
        return

    if not nome_atualizado.strip() or not senha_atualizado.strip() or not isadm_atualizado.strip():
        CaixaMensagens.error_box("Erro", "Preencha Todos Os Campos Para Salvar")
    else:
        if adm_formatado in dicionario_adm:
            editar_cadastro(id_usuario, "nome", nome_atualizado)
            editar_cadastro(id_usuario, "senha", senha_atualizado)
            editar_cadastro(id_usuario, "adm", adm_formatado)
            CaixaMensagens.info_box("Sucesso", "Reiniciando Sistema...")
            janela.after(1000, lambda: reiniciar_sistema.reiniciar(janela))


def cancelar(janela):
    global edicao_ativa
    if edicao_ativa == 1:
        print("Edição Ativa")
        conf = CaixaMensagens.conf_box("Cancelar Alteração", "Deseja Cancelar A Edição?")
        if conf:
            janela.destroy()
            edicao_ativa = 0
        else:
            return
    else:
        print("Edição Não Ativa")
        janela.destroy()
