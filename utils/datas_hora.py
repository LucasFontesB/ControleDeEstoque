from datetime import datetime

def get_horaatual():
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return datetime.strptime(data_hora, "%d/%m/%Y %H:%M:%S")

def formatar_datahora_objdatetime(data_hora):
    return datetime.strptime(data_hora, "%d/%m/%Y %H:%M:%S")

def formatar_datahora_str(data_hora):
    return data_hora.strftime("%d/%m/%Y %H:%M:%S")

def calcular_diferenca_horas(hora):
    data_hora = get_horaatual()
    hora_formatada = formatar_datahora_objdatetime(hora)
    diferenca = data_hora - hora_formatada
    return diferenca
