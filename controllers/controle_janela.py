import logging
from os import path

def centralizar_janela(janela, largura, altura):
    try:
        janela.update_idletasks()
        largura_tela = janela.winfo_screenwidth()
        altura_tela = janela.winfo_screenheight()
        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)
        janela.geometry(f"{largura}x{altura}+{x}+{y}")
    except Exception as erro:
        logging.warning(f"Falha Ao Centralizar Janela: {erro}")

def inserir_icon(janela, tipo_icone):
    if tipo_icone == "erro":
        try:
            caminho_icone = path.abspath(
                path.join(path.dirname(__file__), "..", "assets", "icons", "error_icon.ico"))
            janela.after(200, lambda: janela.iconbitmap(caminho_icone))
        except Exception as erro:
            logging.warning(f"Falha Ao Carregar Icone De Erro - Box: {erro}")
    elif tipo_icone == "info":
        try:
            caminho_icone = path.abspath(
                path.join(path.dirname(__file__), "..", "assets", "icons", "info_icon.ico"))
            janela.after(200, lambda: janela.iconbitmap(caminho_icone))
        except Exception as erro:
            logging.warning(f"Falha Ao Carregar Icone De Info - Box: {erro}")
    elif tipo_icone == "logo":
        try:
            caminho_icone = path.abspath(
                path.join(path.dirname(__file__), "..", "assets", "icons", "logo_icon.ico"))
            janela.after(200, lambda: janela.iconbitmap(caminho_icone))
        except Exception as erro:
            logging.warning(f"Falha Ao Carregar Icone De Logo - Box: {erro}")
    elif tipo_icone == "interrogation":
        try:
            caminho_icone = path.abspath(
                path.join(path.dirname(__file__), "..", "assets", "icons", "interrogation_icon.ico"))
            janela.after(200, lambda: janela.iconbitmap(caminho_icone))
        except Exception as erro:
            logging.warning(f"Falha Ao Carregar Icone De Interrogation - Box: {erro}")
    elif tipo_icone == "account":
        try:
            caminho_icone = path.abspath(
                path.join(path.dirname(__file__), "..", "assets", "icons", "account_icon.ico"))
            janela.after(200, lambda: janela.iconbitmap(caminho_icone))
        except Exception as erro:
            logging.warning(f"Falha Ao Carregar Icone De Account - Box: {erro}")
