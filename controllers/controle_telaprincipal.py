import logging

from controllers import controle_mensagens, controle_usuario

def atualizar_vendas_por_hora(ax, canvas):
    ax.clear()
    ax.plot(horas, valores, marker='o', linestyle='-', color='blue')
    ax.set_title("Vendas por Hora - Hoje")
    ax.set_xlabel("Hora")
    ax.set_ylabel("Valor (R$)")
    ax.grid(True)
    canvas.draw()

def atualizar_vendas_por_dia(ax, canvas):
    ax.clear()
    ax.bar(dias, valores, color='skyblue')
    ax.set_title("Vendas por Produto - Hoje")
    ax.set_xlabel("Dia Da Semana")
    ax.set_ylabel("Valor Vendido (R$)")
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)
    canvas.draw()

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
