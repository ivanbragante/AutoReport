import pyautogui
import time
import keyboard
import webbrowser
from execucao.esc_encerra import check_for_esc

def fazer_Login():
        check_for_esc()
        #Função para fazer login no navegador
        webbrowser.open_new_tab('site do report')
        time.sleep(3)
        pyautogui.click(672, 346)  #Clique na posição do campo de usuário 
        check_for_esc()
        pyautogui.typewrite('usuario') #Coloca o login
        pyautogui.click(682, 558) #Clica no next
        time.sleep(1.5)
        check_for_esc()
        pyautogui.click(672, 361) #Clica no campo de senha
        time.sleep(0.5)
        check_for_esc()
        pyautogui.typewrite('senha') #Coloca a senha
        time.sleep(0.2)
        pyautogui.press('enter')
        check_for_esc()
        time.sleep(5)
