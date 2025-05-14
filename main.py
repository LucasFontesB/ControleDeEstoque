import logging

import os

from utils.datas_hora import get_horaatual

from database import db_conexao
from database import db_turnos
from database import db_usuarios

from controllers.controle_turno import verificar_horario

from ui import login

data_hora_atual = get_horaatual()

data_formatada = data_hora_atual.strftime("%Y-%m-%d_%H-%M-%S")

log_nome = f"log_{data_formatada}.log"

pasta_base = os.path.dirname(__file__)
caminho_log = os.path.join(pasta_base, "logs", log_nome)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=caminho_log,
    filemode="w"
)

#db_turnos.alterar_turno(2, "11/05/2025 10:00:00")

#db_usuarios.remover_usuario(3)

db_conexao.criar_tabelas()

if __name__ == "__main__":
    logging.info("Iniciando Programa...")
    verificar_horario()
    login.TelaLogin()
