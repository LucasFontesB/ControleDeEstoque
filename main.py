import logging

import os

import database.db_estoque
from utils.datas_hora import get_horaatual

from database import db_conexao, db_manager

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

#database.db_estoque.cadastrar_categoria("Bebida")
#database.db_estoque.cadastrar_produto("Agua", 10, 0.75, 3, 1)



db_conexao.criar_tabelas()

if __name__ == "__main__":
    logging.info("Iniciando Programa...")
    verificar_horario()
    login.TelaLogin()
