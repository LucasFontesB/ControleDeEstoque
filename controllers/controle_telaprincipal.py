import logging

from controllers import controle_mensagens, controle_usuario

def atualizar_vendas_por_hora(ax, canvas):
    pass

def atualizar_vendas_por_dia(ax, canvas):
    pass

def fechar(janela_principal, usuario):
    logging.info("Fechando Turno e Finalizando Janela")
    if controle_mensagens.CaixaMensagens.conf_box("Finalizar Turno", "Deseja Sair e Finalizar Turno?"):
        try:
            if controle_usuario.ControleUsuario.finalizar_turno(usuario) is True:
                janela_principal.destroy()
                logging.info("Turno Finalizado Com Sucesso e Fechando a Janela")
            else:
                controle_mensagens.CaixaMensagens.error_box("Erro", f"""Erro Ao Finalizar Turno Ou Fechar Janela
                                                                     {usuario.nome}""")
        except Exception as erro:
            logging.warning(f"Erro Ao Fechar Turno Ou Finalizar Janela: {erro}")
    else:
        pass
