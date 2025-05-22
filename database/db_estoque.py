import logging

import utils.datas_hora
from database.db_conexao import conectar

def retornar_vendas_dia():
    pass

def retornar_vendas_hora():
    conn = None
    logging.info(f"DB - Carregando Vendas Por Hora")
    try:
        data_atual = utils.datas_hora.get_horaatual()
        data = data_atual.date()
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT total, data FROM vendas WHERE DATE(data) = ?", (data,))
        produtos = cursor.fetchall()
        print(f"Vendas: {produtos}")
        return produtos
    except Exception as erro:
        logging.warning(f"Falha Ao Listar Produtos: {erro}")
        if conn:
            conn.rollback()
        else:
            logging.warning("Falha Ao Conectar Conn - listar_produtos")
    finally:
        if conn:
            conn.close()
        else:
            logging.warning("Falha Ao Conectar Conn - listar_produtos")

def listar_produtos():
    conn = None
    logging.info(f"DB - ")
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        return produtos
    except Exception as erro:
        logging.warning(f"Falha Ao Listar Produtos: {erro}")
        if conn:
            conn.rollback()
        else:
            logging.warning("Falha Ao Conectar Conn - listar_produtos")
    finally:
        if conn:
            conn.close()
        else:
            logging.warning("Falha Ao Conectar Conn - listar_produtos")

def cadastrar_categoria(nome):
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO categorias (nome) VALUES (?)", (nome,))
        conn.commit()
    except Exception as erro:
        logging.warning(f"DB - Erro Ao Cadastrar Categoria: {erro}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
        else:
            logging.warning("DB - Falha Ao Inicializar Conn - cadastrar_categoria")

def cadastrar_produto(nome, quantidade, preco_compra, preco_venda, categoria):
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO produtos (nome, quantidade, preco_compra, preco_venda, categoria_id)
                     VALUES (?,?,?,?,?)""", (nome, quantidade, preco_compra, preco_venda, categoria))
        conn.commit()
    except Exception as erro:
        logging.warning(f"Erro Ao Cadastrar Produtos: {erro}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
        else:
            logging.warning("Falha Ao Inicializar Conn - cadastrar_produto")


def atualizar_estoque(nome, quantidade):
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("UPDATE produtos SET quantidade = ? WHERE nome = ?", (quantidade, nome))
        conn.commit()
    except Exception as erro:
        logging.warning(f"Falha Ao Atualizar Item De Estoque: {erro}")
        if conn:
            conn.rollback()
        else:
            logging.warning("Falha Ao Inicializar Conn - atualizar_estoque")
    finally:
        if conn:
            conn.close()
        else:
            logging.warning("Falha Ao Inicializar Conn - atualizar_estoque")

def remover_produto(produto_id):
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id, ))
        conn.commit()
    except Exception as erro:
        logging.warning(f"Falha Ao Remover Produto: {erro}")
        if conn:
            conn.rollback()
        else:
            logging.warning("Falha Ao Inicializar Conn - remover_produto")
    finally:
        if conn:
            conn.close()
        else:
            logging.warning("Falha Ao Inicializar Conn - remover_produto")

def vender(itens_venda):
    pass