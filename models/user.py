class Usuario:
    def __init__(self, nome, senha, id, is_logado, id_turno, data_criacao, usuario_criacao,adm=0):
        self.nome = nome
        self.senha = senha
        self.adm = adm
        self.id = id
        self.is_logado = is_logado
        self.id_turno = id_turno
        self.data_criacao = data_criacao
        self.usuario_criacao = usuario_criacao
