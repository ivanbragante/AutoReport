import pyautogui
import time
import keyboard
import webbrowser
import subprocess
import pygetwindow as gw

def abrir_Nav():
    chrome_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # ajuste o caminho conforme necessário
    # Abrir uma nova janela vazia
    subprocess.Popen([chrome_path, "--new-window", "about:blank"])
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(2.5)
    subprocess.Popen([chrome_path, "--new-window", "about:blank"])
    # Aguardar um pouco para a janela abrir
    time.sleep(1.5)
    # Encontrar a janela do Chrome
    windows = gw.getWindowsWithTitle('about:blank - Google Chrome')  # Tente 'Chrome' em vez de 'Nova janela'
    time.sleep(1.5)
    if windows:
        window = windows[0]
        window.moveTo(700, 331)  # Move para o meio do monitor principal
        time.sleep(1.5)
        pyautogui.hotkey('win', 'up')
        time.sleep(0.5)
        window.maximize()  # Maximiza a janela
    else:
        print("Janela do Chrome não encontrada.")
