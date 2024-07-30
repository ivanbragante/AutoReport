import socket
import tkinter as tk
import sys
from tkinter import messagebox


def check_internet_connection():
    try:
        # Tenta se conectar a um site conhecido (por exemplo, o Google)
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

if check_internet_connection():
    # Se a máquina estiver conectada à internet, execute o código principal aqui
    print("A máquina está conectada à internet. Rodando o código...")
    # ...
else:
    # Se não houver conexão com a internet, exiba uma mensagem
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    messagebox.showerror("AutoReport", "O AutoReport não será executado devido à falta de conexão com a internet.")
    root.destroy() 
    sys.exit()