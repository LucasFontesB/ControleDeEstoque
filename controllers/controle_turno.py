import logging

from utils.datas_hora import get_horaatual, formatar_datahora_objdatetime, formatar_datahora_str

from database import db_turnos

from datetime import timedelta

from controllers.controle_mensagens import CaixaMensagens

def registrar_inicio_turno(is_logado, id_usuario):
    if is_logado == 1:
        logging.info("\n\n\nUsuario ja logado")
        logging.info("Continuando Sem Inicar Turno...\n")
    elif is_logado == 0:
        logging.info("\n\n\nUsuario nao logado. Iniciando registro de turno...\n")
        logging.info(f"\n============LOG INICIO DE TURNO ID {id_usuario}============\n")
        hora_atual = get_horaatual()
        logging.info(f"Hora Atual: {hora_atual}")
        hora_formatada = formatar_datahora_str(hora_atual)
        try:
            db_turnos.iniciar_turno(id_usuario, hora_formatada)
            logging.info("Turno Iniciado Com Sucesso!")
            logging.info("\n================================================\n")
        except Exception as erro:
            CaixaMensagens.error_box("Erro", "Erro Ao Iniciar Turno (Consultar LOG)")
            logging.warning(f"Erro Ao Iniciar Turno: {erro}")
            return

def registrar_final_turno(id_usuario, id_turno):
    if not db_turnos.buscar_horario_saida(id_usuario, id_turno):
        logging.info(f"\n============LOG FECHAMENTO USUaRIO {id_usuario}============\n")
        hora_atual = get_horaatual()
        hora_formatada = formatar_datahora_str(hora_atual)
        logging.info(f"Hora atual: {hora_formatada}")
        logging.info("Registrando Horario Final No Registro De Turnos...")
        try:
            db_turnos.finalizar_turno(id_usuario, hora_formatada)
            logging.info("\n================================================\n")
            return True
        except Exception as erro:
            CaixaMensagens.error_box("Erro", f"Erro ao registrar horario final no registro de turno")
            logging.warning(f"Erro Ao Registrar Horario Final No Registro De Turno: {erro}")
        logging.info("\n================================================\n")
    else:
        CaixaMensagens.error_box("Erro", "Usuario Com Turno Fechado. Reinicie o Sistema")
        return False

def verificar_horario():
    logging.info("Verificacao de horarios")
    try:
        ids_encontrados = db_turnos.busca_de_horarios_abertos()
    except Exception as erro:
        logging.warning(f"Erro Ao Consultar IDs Com Turnos Em Aberto: {erro}")
    if not ids_encontrados:
        logging.info("Nenhum Turno Em Aberto")
    else:
        logging.info(f"Lista de ID's com turno ABERTO: {[row[0] for row in ids_encontrados]}")

        for id, id_turno in ids_encontrados:
            logging.info(f"\n============LOG USUÁRIO {id}============\n")
            try:
                hora_atual = get_horaatual()
                turnos_abertos = db_turnos.buscar_horario_entrada(id)
            except Exception as erro:
                logging.warning(f"Erro Ao Consultar Turnos Em Aberto Ou Formatar Data e Hora: {erro}")

            for data_hora_encontrada in turnos_abertos:
                try:
                    data_hora_formatada = formatar_datahora_objdatetime(data_hora_encontrada[0])
                except Exception as erro:
                    logging.warning(f"Erro Ao Formatar Data e Hora Para DateTime: {erro}")
                diferenca = hora_atual - data_hora_formatada

                logging.info(f"Data De Entrada: {formatar_datahora_str(data_hora_formatada)}")
                logging.info(f"Data Atual: {formatar_datahora_str(hora_atual)}")
                logging.info(f"Diferenca De Horas: {diferenca}")

                if diferenca >= timedelta(hours=24):
                    logging.info(f"Usuario com id {id} logado a mais de 24 horas, fechando turno...")
                    try:
                        registrar_final_turno(id, id_turno)
                    except Exception as erro:
                        logging.warning(f"Erro Ao Registrar Fechamento Automatico De Turno: {erro}")
                else:
                    logging.info(f"Usuario com id {id} logado a menos de 24 horas, continuando turno")
                logging.info("\n=====================================\n")
