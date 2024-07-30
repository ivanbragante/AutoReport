import pyautogui
import time
import keyboard 
import socket
import tkinter as tk
import sys
from tkinter import messagebox
from execucao.testnet import check_internet_connection
from relat.abrirNav import abrir_Nav
from relat.login import fazer_Login
from relat.relatorio import gerar_relatorio
from sheet.getSheets import sheets
from execucao.confirmation import confirm_execution
from execucao.esc_encerra import check_for_esc

def main():
    try:
        time.sleep(3)
        confirm_execution()  #Pergunta ao usuário se deseja executar o programa
        check_for_esc()
        time.sleep(3)
        check_internet_connection()  #Checando se tem conexão com a internet
        check_for_esc()
        abrir_Nav()  #Abre o chrome
        check_for_esc()
        fazer_Login()  #Faz login
        check_for_esc()
        time.sleep(3)
        gerar_relatorio()  #Navega e gera o relatório
        check_for_esc()
        time.sleep(1.5)
        sheets() #Copia do excel pro sheets

        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("AutoReport", "AutoReport finalizado com sucesso.")
        root.destroy()

    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário.")
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("AutoReport", "Programa interrompido pelo usuário.")
        
if __name__ == "__main__":
    main()