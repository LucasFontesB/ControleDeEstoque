import time

from ui import login,tela_principal

def reiniciar(janela):
    time.sleep(1)
    janela.destroy()
    login.TelaLogin()