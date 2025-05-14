import logging

import database.db_conexao as db_conexao

def alterar_turno(id_usuario, data_entrada):
    conn = None
    logging.info(f"DB - Alterando Turno: Usuario ID {id_usuario} para data: {data_entrada}")
    try:
        conn = db_conexao.conectar()
        cursor = conn.cursor()

        cursor.execute("UPDATE registro_turno SET hora_entrada = ? WHERE id_usuario = ?", (
            data_entrada, id_usuario))
        conn.commit()
    except Exception as erro:
        logging.warning(f"Falha Ao Alterar Horário: {erro}")
        if conn:
            conn.rollback()
        else:
            logging.warning("Falha Ao Inicializar Conn - alterar_turno ")
    finally:
        if conn:
            conn.close()
        else:
            logging.warning("Falha Ao Inicializar Conn - alterar_turno ")

def iniciar_turno(id_usuario, hora_atual):
    conn = None
    logging.info(f"DB - Iniciando Turno Do Usuario ID {id_usuario} Com a Hora Atual: {hora_atual}")
    try:
        conn = db_conexao.conectar()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO registro_turno (id_usuario, hora_entrada) VALUES (?, ?)", (
            id_usuario, hora_atual))
        conn.commit()
        cursor.execute("UPDATE usuarios SET is_logado = ? where id = ?", (1, id_usuario))
        conn.commit()
    except Exception as erro:
        logging.warning(f"Falha Ao Iniciar Turno: {erro}")
        if conn:
            conn.rollback()
        else:
            logging.warning("Falha Ao Inicializar Conn - iniciar_turno ")
    finally:
        if conn:
            conn.close()
        else:
            logging.warning("Falha Ao Inicializar Conn - alterar_turno ")

def finalizar_turno(id_usuario, hora_atual):
    conn = None
    logging.info(f"DB - Finalizando Turno Do Usuário ID {id_usuario} Com A Hora Atual: {hora_atual}")
    try:
        conn = db_conexao.conectar()
        cursor = conn.cursor()

        cursor.execute("UPDATE registro_turno SET hora_saida = ? WHERE id_usuario = ?", (
            hora_atual, id_usuario))
        conn.commit()
        cursor.execute("UPDATE usuarios SET is_logado = ? where id = ?", (0, id_usuario))
        conn.commit()
    except Exception as erro:
        logging.warning(f"Falha ao Finalizar Turno: {erro}")
        if conn:
            conn.rollback()
        else:
            logging.warning("Falha Ao Inicializar Conn - finalizar_turno ")
    finally:
        if conn:
            conn.close()
        else:
            logging.warning("Falha Ao Inicializar Conn - finalizar_turno ")

def buscar_horario_entrada(id_usuario):
    conn = None
    logging.info(f"DB - Buscando Horário De Entrada Para O Usuario ID {id_usuario}")
    try:
        conn = db_conexao.conectar()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT hora_entrada FROM registro_turno WHERE id_usuario = ? AND hora_saida IS NULL",
            (id_usuario,)
        )
        turnos_abertos = cursor.fetchall()
        logging.info(f"DB - Resultado Dos Turnos Abertos Do Usuario ID {id_usuario}: {turnos_abertos}")
        return turnos_abertos
    except Exception as erro:
        logging.warning(f"Falha Ao Buscar Horário De Entrada: {erro}")
        if conn:
            conn.rollback()
            return None
        else:
            logging.warning("Falha Ao Inicializar Conn - buscar_horario_entrada ")
            return None
    finally:
        if conn:
            conn.close()
        else:
            logging.warning("Falha Ao Inicializar Conn - buscar_horario_entrada ")

def buscar_horario_saida(id_usuario, id_turno):
    conn = None
    logging.info(f"DB - Buscando Horario De Saida Do Usuario ID {id_usuario} Do Turno ID {id_turno}")
    try:
        conn = db_conexao.conectar()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT hora_saida FROM registro_turno WHERE id_usuario = ? and id = ?",
            (id_usuario, id_turno)
        )
        horario_saida = cursor.fetchall()

        if horario_saida[0][0]:
            logging.info(f"DB - Resultado Dos Horários De Saida Do Usuario ID {id_usuario} Do Turno ID {id_turno}")
            logging.info(f"DB - {horario_saida[0][0]}")
            return horario_saida[0][0]
        else:
            logging.info(f"""DB - Nenhum Resultado Dos Horários De Saida Do Usuario ID
                         {id_usuario} Do Turno ID {id_turno} Encontrado""")
            return None
    except Exception as erro:
        logging.warning("Falha Ao Buscar Horario De Saída")
        if conn:
            conn.rollback()
            return None
        else:
            logging.warning("Falha Ao Inicializar Conn - buscar_horario_saida")
            return None
    finally:
        if conn:
            conn.close()
        else:
            logging.warning("Falha Ao Inicializar Conn - buscar_horario_saida")


def busca_de_horarios_abertos():
    conn = None
    logging.info(f"DB - Buscando Horarios Abertos Dos Usuarios")
    try:
        conn = db_conexao.conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT id_usuario, id FROM registro_turno WHERE hora_saida IS NULL")
        ids_encontrados = cursor.fetchall()
        logging.info(f"DB - Resultado Da Busca De Horarios Abertos")
        logging.info(f"DB - {ids_encontrados}")
        return ids_encontrados
    except Exception as erro:
        logging.warning(f"Falha Ao Buscar Horarios Em Aberto: {erro}")
        if conn:
            conn.rollback()
        else:
            logging.warning("Falha Ao Inicializar Conn - buscar_de_horario_abertos")
    finally:
        if conn:
            conn.close()
        else:
            logging.warning("Falha Ao Inicializar Conn - buscar_de_horario_abertos")