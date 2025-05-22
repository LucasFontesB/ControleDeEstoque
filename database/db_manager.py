from database.db_conexao import conectar
def alterar_horario(id_usuario):
    conn = conectar()
    cursor = conn.cursor()
    data = "09/05/2025 10:05:24"

    cursor.execute("UPDATE registro_turno SET hora_entrada = ? WHERE id_usuario = ?", (data, id_usuario))
    conn.commit()
    conn.close()

def deletar(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM categorias WHERE id = ?", (id,))
    conn.commit()
    conn.close()








