from database.db_conexao import conectar
def cadastrar_usuario(nome, senha, is_adm, usuario_criacao, data_criacao):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO usuarios (nome, senha, adm, data_criacao, usuario_criacao)
                    VALUES (?, ?, ?, ?, ?)""", (nome, senha, is_adm, data_criacao, usuario_criacao))
    conn.commit()
    conn.close()

def editar_cadastro(id_usuario, tipo_alteracao, valor):
    if tipo_alteracao == "nome":
        conn = None
        try:
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("UPDATE usuarios SET nome = ? WHERE id = ?", (valor, id_usuario))
            conn.commit()
        except Exception as erro:
            print(f"Erro ao editar cadastro de nome: {erro}")
            if conn:
                conn.rollback()
        finally:
            if conn:
                conn.rollback()
            else:
                print(f"Erro ao editar cadastro de nome")
    elif tipo_alteracao == "senha":
        conn = None
        try:
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("UPDATE usuarios SET senha = ? WHERE id = ?", (valor, id_usuario))
            conn.commit()
        except Exception as erro:
            print(f"Erro ao editar cadastro de senha: {erro}")
            if conn:
                conn.rollback()
        finally:
            if conn:
                conn.rollback()
            else:
                print(f"Erro ao editar cadastro de senha")
    elif tipo_alteracao == "adm":
        conn = None
        try:
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("UPDATE usuarios SET adm = ? WHERE id = ?", (valor, id_usuario))
            conn.commit()
        except Exception as erro:
            print(f"Erro ao editar cadastro de adm: {erro}")
            if conn:
                conn.rollback()
        finally:
            if conn:
                conn.rollback()
            else:
                print(f"Erro ao editar cadastro de adm")

def remover_usuario(id_usuario):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    conn.commit()
    conn.close()

def autenticar_usuario(nome, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, is_logado FROM usuarios WHERE nome = ? AND senha = ?", (nome, senha))
    resultado_usuario = cursor.fetchone()
    conn.close()

    if resultado_usuario:
        return resultado_usuario
    else:
        return None

def buscar_usuario(id_usuario):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""SELECT usuarios.nome, usuarios.senha, usuarios.id AS usuario_id, usuarios.adm, usuarios.is_logado,
                    registro_turno.id AS turno_id, usuarios.data_criacao, usuarios.usuario_criacao
                    FROM usuarios JOIN registro_turno ON usuarios.id = registro_turno.id_usuario
                    AND registro_turno.hora_saida IS NULL WHERE usuario_id = ?""", (id_usuario,))
    dados_usuario = cursor.fetchone()
    conn.close()

    return dados_usuario