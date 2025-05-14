import os

import logging

import sqlite3

db_name = "estoque.db"

def conectar():
    try:
        logging.debug("Conexão com o banco de dados efetuada com sucesso")
        pasta_base = os.path.dirname(__file__)
        caminho_db = os.path.join(pasta_base, db_name)
        return sqlite3.connect(caminho_db)
    except Exception as erro:
        logging.warning(f"Erro Ao Conectar Com O Banco De Dados: {erro}")

def criar_tabelas():
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS categorias(
                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            nome TEXT NOT NULL)""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            nome TEXT NOT NULL,
                            senha TEXT NOT NULL,
                            adm INTEGER NOT NULL,
                            data_criacao TEXT NOT NULL,
                            usuario_criacao TEXT NOT NULL,
                            is_logado INTEGER DEFAULT 0 NOT NULL)""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS vendas(
                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            quant_produtos INTEGER NOT NULL,
                            total REAL NOT NULL,
                            data TEXT NOT NULL,
                            status TEXT NOT NULL)""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS produtos(
                       id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                       nome TEXT NOT NULL,
                       quantidade INTEGER NOT NULL,
                       preco_venda REAL NOT NULL,
                       preco_compra REAL,
                       categoria_id INTEGER NOT NULL,
                       FOREIGN KEY(categoria_id) REFERENCES categorias(id))""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS itens_venda (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        venda_id INTEGER NOT NULL,
                        produto_id INTEGER NOT NULL,
                        quantidade INTEGER NOT NULL,
                        preco_unitario REAL NOT NULL,
                        FOREIGN KEY(venda_id) REFERENCES vendas(id),
                        FOREIGN KEY(produto_id) REFERENCES produtos(id))""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS registro_turno (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_usuario INTEGER NOT NULL,
                        hora_entrada TEXT NOT NULL,
                        hora_saida TEXT,
                        FOREIGN KEY(id_usuario) REFERENCES usuarios(id))""")

        conn.commit()
    except Exception as erro:
        logging.warning(f"Erro Ao Criar Tabelas:{erro}")
        if conn:
            conn.rollback()
        else:
            logging.warning(f"Falha Ao Conectar Conn")
    finally:
        if conn:
            conn.close()
        else:
            logging.warning(f"Falha Ao Conectar Conn")