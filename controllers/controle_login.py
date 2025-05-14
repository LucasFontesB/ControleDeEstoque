import logging

from controllers.controle_mensagens import CaixaMensagens
from controllers.controle_usuario import ControleUsuario

from ui.tela_principal import TelaPrincipal

def autenticar_usuario(nome, senha, janela):
    if not nome.strip() or not senha.strip():
        CaixaMensagens.error_box("Erro", "Preencha Todos Os Campos!")
    else:
        try:
            autenticacao, id_usuario, is_logado = ControleUsuario.autenticar_login(nome, senha)
            logging.debug(f"ID do usuario: {id_usuario}")

            if autenticacao is True:
                tela = TelaPrincipal(id_usuario, is_logado)
                janela.destroy()
                tela.iniciar()
            else:
                CaixaMensagens.error_box("Erro", "Nenhum Usuário Cadastrado!")
                return
        except Exception as erro:
            CaixaMensagens.error_box("Erro", "Falha ao autenticar usuario (Consulte o LOG)")
            logging.warning(f"Falha ao autenticar usuario ControleLogin: {erro}")
