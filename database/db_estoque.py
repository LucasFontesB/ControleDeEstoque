import logging

from database.db_conexao import conectar

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

def cadastrar_produto(nome, quantidade, preco_compra, preco_venda, categoria):
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO produtos (nome, quantidade, preco_compra, preco_venda, categoria)
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


def atualizar_estoque(id_produto, quantidade):
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (quantidade, id_produto))
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