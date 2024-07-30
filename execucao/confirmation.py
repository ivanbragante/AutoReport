import tkinter as tk
import sys
from tkinter import messagebox

def confirm_execution():
        root = tk.Tk()
        root.withdraw()  #Oculta a janela principal

        result = messagebox.askquestion("AutoReport", "Você deseja executar o AutoReport?")
        root.destroy()

        if result == 'no':
            sys.exit("Execução do programa cancelada pelo usuário.")