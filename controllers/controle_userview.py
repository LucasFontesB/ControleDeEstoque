import logging
import time

from controllers.controle_mensagens import CaixaMensagens
from utils import reiniciar_sistema
from database.db_usuarios import editar_cadastro
from ui.tela_principal import TelaPrincipal


edicao_ativa = 0
def editar_usuario(entry_nome, entry_senha, entry_isadm, botao_editar, botao_salvar):
    logging.info("Iniciando Edição De Usuário")
    global edicao_ativa
    usuario_isadm = entry_isadm.get()
    if usuario_isadm == "Sim":
        logging.info("Usuário ADM. Liberando Campos")
        edicao_ativa = 1
        entry_nome.configure(state="normal", text_color="white")
        entry_senha.configure(state="normal", text_color="white")
        entry_senha.configure(show="", text_color="white")
        entry_isadm.configure(state="normal", text_color="white")
        botao_salvar.configure(state="normal", text_color="white")
        botao_editar.configure(state="disable", text_color="gray")
    else:
        logging.info("Usuário Não ADM. Bloqueando Campos")
        CaixaMensagens.info_box("Atenção", "Apenas Usuarios ADM Pode Modificar")

def salvar(janela, id_usuario, nome_atual, senha_atual, isadm_atual, entry_nome, entry_senha, entry_isadm,
           botao_editar, botao_salvar):
    logging.info("Preparando Para Salvar Alterações")
    dicionario_sim = ["sim", "s"]
    dicionario_nao = ["nao", "não", "n"]
    dicionario_adm = [1, 0]
    nome_atualizado = entry_nome.get()
    senha_atualizado = entry_senha.get()
    isadm_atualizado = entry_isadm.get()

    adm_formatado = None
    if isadm_atualizado.lower() in dicionario_sim:
        logging.debug("ADM Formatado = 1")
        adm_formatado = 1
    elif isadm_atualizado.lower() in dicionario_nao:
        logging.debug("ADM Formatado = 0")
        adm_formatado = 0
    else:
        logging.debug("Valor De ADM Inválido")
        CaixaMensagens.error_box("Erro", "Valor Para ADM Inválido")
        return

    if not nome_atualizado.strip() or not senha_atualizado.strip() or not isadm_atualizado.strip():
        logging.debug("Campos Não Preenchidos")
        CaixaMensagens.error_box("Erro", "Preencha Todos Os Campos Para Salvar")
    else:
        if adm_formatado in dicionario_adm:
            logging.info("Chamando Funções Para Salvar No DB")
            try:
                editar_cadastro(id_usuario, "nome", nome_atualizado)
                editar_cadastro(id_usuario, "senha", senha_atualizado)
                editar_cadastro(id_usuario, "adm", adm_formatado)
                CaixaMensagens.info_box("Sucesso", "Reiniciando Sistema...")
                janela.after(1000, lambda: reiniciar_sistema.reiniciar(janela))
            except Exception as erro:
                logging.warning(f"Erro Ao Salvar Alterações No DB: {erro}")


def cancelar(janela):
    global edicao_ativa
    if edicao_ativa == 1:
        logging.debug("Edição Ativa")
        conf = CaixaMensagens.conf_box("Cancelar Alteração", "Deseja Cancelar A Edição?")
        if conf:
            janela.destroy()
            edicao_ativa = 0
        else:
            return
    else:
        logging.debug("Edição Não Ativa")
        janela.destroy()
