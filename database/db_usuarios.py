import logging

from database.db_conexao import conectar
def cadastrar_usuario(nome, senha, is_adm, usuario_criacao, data_criacao):
    logging.info("DB - Iniciando Cadastro De Usuário")
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO usuarios (nome, senha, adm, data_criacao, usuario_criacao)
                        VALUES (?, ?, ?, ?, ?)""", (nome, senha, is_adm, data_criacao, usuario_criacao))
        conn.commit()
    except Exception as erro:
        logging.warning(f"DB - Erro Ao Cadastrar Usuario: {erro}")
        if conn:
            logging.info("DB - Realizando RollBack - cadastrar_usuario")
            conn.rollback()
        else:
            logging.warning("DB - Erro Ao Realizar RollBack - cadastrar_usuario")
    finally:
        if conn:
            conn.close()
        else:
            logging.warning("DB - Erro Ao Fechar Conn - cadastrar_usuario")

def editar_cadastro(id_usuario, tipo_alteracao, valor):
    logging.info("DB - Iniciando Edição De Cadastro")
    if tipo_alteracao == "nome":
        logging.debug("DB - Iniciando Edição De Cadastro (Nome)")
        conn = None
        try:
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("UPDATE usuarios SET nome = ? WHERE id = ?", (valor, id_usuario))
            conn.commit()
        except Exception as erro:
            logging.warning(f"DB - Erro ao editar cadastro de nome: {erro}")
            if conn:
                logging.info("DB - Realizando RollBack - editar_cadastro(nome)")
                conn.rollback()
            else:
                logging.warning("DB - Erro Ao Realizar RollBack - editar_cadastro(nome)")
        finally:
            if conn:
                conn.close()
            else:
                logging.warning(f"DB - Erro Ao Fechar Conn - editar_cadastro(nome)")

    elif tipo_alteracao == "senha":
        logging.info("DB - Iniciando Edição De Cadastro (Senha)")
        conn = None
        try:
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("UPDATE usuarios SET senha = ? WHERE id = ?", (valor, id_usuario))
            conn.commit()
        except Exception as erro:
            logging.warning(f"DB - Erro ao editar cadastro de senha: {erro}")
            if conn:
                logging.info("DB - Iniciando RollBack - editar_cadastro(senha)")
                conn.rollback()
            else:
                logging.warning("DB - Erro Ao Efetuar RollBack - editar_cadastro(senha)")
        finally:
            if conn:
                conn.close()
            else:
                print(f"Erro Ao Fechar Conn - editar_cadastro(senha)")

    elif tipo_alteracao == "adm":
        logging.info("DB - Iniciando Edição De Cadastro (ADM)")
        conn = None
        try:
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("UPDATE usuarios SET adm = ? WHERE id = ?", (valor, id_usuario))
            conn.commit()
        except Exception as erro:
            logging.warning(f"DB - Erro ao editar cadastro de adm: {erro}")
            if conn:
                logging.info("DB - Iniciando RollBack - editar_cadastro(adm)")
                conn.rollback()
            else:
                logging.warning("DB - Erro Ao Efetuar RollBack - editar_cadastro(adm)")
        finally:
            if conn:
                conn.close()
            else:
                logging.warning(f"Erro Ao Fechar Conn - editar_cadastro(adm)")

def remover_usuario(id_usuario):
    logging.info("DB - Iniciando Remoção De Usuário")
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
        conn.commit()
    except Exception as erro:
        logging.warning(f"DB - Erro Ao Remover Usuário: {erro}")
        if conn:
            logging.info("DB - Iniciando RollBack - remover_usuario")
            conn.rollback()
        else:
            logging.warning(f"DB - Erro Ao Efetuar RollBack - remover_usuario")
    finally:
        if conn:
            conn.close()
        else:
            logging.warning("Erro Ao Fechar Conn - remover_usuario")

def autenticar_usuario(nome, senha):
    logging.info("DB - Iniciando Autenticação De Usuario")
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT id, is_logado FROM usuarios WHERE nome = ? AND senha = ?", (nome, senha))
        resultado_usuario = cursor.fetchone()

        if resultado_usuario:
            return resultado_usuario
        else:
            return None
    except Exception as erro:
        logging.warning(f"DB - Erro Ao Autenticar Usuario: {erro}")
        if conn:
            logging.debug("DB - Realizando RollBack")
            conn.rollback()
        else:
            logging.warning(f"DB - Erro Ao Realizar RollBack - autenticar_usuario: {erro}")
    finally:
            if conn:
                conn.close()
            else:
                logging.warning("DB - Erro Ao Fechar Conn - autenticar_usuario")

def buscar_usuario(id_usuario):
    logging.info("DB - Iniciando Busca De Usuario")
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""SELECT usuarios.nome, usuarios.senha, usuarios.id AS usuario_id, usuarios.adm, usuarios.is_logado,
                        registro_turno.id AS turno_id, usuarios.data_criacao, usuarios.usuario_criacao
                        FROM usuarios JOIN registro_turno ON usuarios.id = registro_turno.id_usuario
                        AND registro_turno.hora_saida IS NULL WHERE usuario_id = ?""", (id_usuario,))
        dados_usuario = cursor.fetchone()

        return dados_usuario
    except Exception as erro:
        logging.warning(f"DB - Erro Ao Buscar Usuário: {erro}")
        if conn:
            logging.info("DB - Efetuando RollBack - buscar_usuario")
            conn.rollback()
        else:
            logging.warning("DB - Erro Ao Efetuar RollBack - buscar_usuario")
    finally:
        if conn:
            conn.close()
        else:
            logging.warning("DB - Erro Ao Fechar Conn - buscar_usuario")