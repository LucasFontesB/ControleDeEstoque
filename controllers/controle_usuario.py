import logging

import controllers.controle_turno
from controllers.controle_mensagens import CaixaMensagens

import utils.datas_hora

from ui.user_view import iniciar

from database import db_usuarios

from models import user

class ControleUsuario:

    def iniciar_usuario(id_usuario):
        logging.info(f"Iniciando Usuário Com ID: {id_usuario}")
        try:
            dados = db_usuarios.buscar_usuario(id_usuario)
            if dados:
                logging.info(f"Usuario ID {id_usuario} Iniciado Com Sucesso\n")
                nome, senha, id, adm, is_logado, id_turno, data_criacao, usuario_criacao = dados
                return user.Usuario(nome=nome, senha=senha, id=id, adm=adm, is_logado=is_logado, id_turno=id_turno,
                                    data_criacao=data_criacao, usuario_criacao=usuario_criacao)
            else:
                return None
        except Exception as erro:
            logging.warning(f"Erro Ao Iniciar Usuario: {erro}")
            CaixaMensagens.error_box("Erro", "Erro Ao Iniciar Usuario (Consulte o LOG)")

    def cadastrar_usuario(nome, senha, is_adm, usuario):
        usuario_criacao = usuario.nome
        data_criacao = utils.datas_hora.get_horaatual()
        data_criacao_formatada = utils.datas_hora.formatar_datahora_str(data_criacao)
        db_usuarios.cadastrar_usuario(nome, senha, is_adm, usuario_criacao, data_criacao_formatada)

    def remover_usuario(self):
        pass

    @staticmethod
    def autenticar_login(nome, senha):
        try:
            if db_usuarios.autenticar_usuario(nome, senha) is None:
                return False, None, None
            else:
                user_id, is_logado = db_usuarios.autenticar_usuario(nome, senha)
                return True, user_id, is_logado
        except Exception as erro:
            CaixaMensagens.error_box("Erro", "Falha ao retornar autenticar usuario (Consulte o LOG)")
            logging.warning(f"Falha ao retornar autenticar usuario ControleUsuario: {erro}")

    @staticmethod
    def iniciar_turno(id, is_logado):
        logging.info("Iniciando Turno...")
        controllers.controle_turno.registrar_inicio_turno(id_usuario=id, is_logado=is_logado)
    @staticmethod
    def finalizar_turno(usuario):
        logging.info("Finalizando Turno...")
        return controllers.controle_turno.registrar_final_turno(id_usuario=usuario.id, id_turno=usuario.id_turno)
    @staticmethod
    def alterar_senha(usuario):
        pass
    def abrir_menu_usuario(janela, usuario):
        iniciar(janela, usuario)