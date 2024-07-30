import pyautogui
import time
import keyboard
import webbrowser
from execucao.esc_encerra import check_for_esc

def fazer_Login():
        check_for_esc()
        #Função para fazer login no navegador
        webbrowser.open_new_tab('https://uccx01.pwc.intcloud.com.br:8444/cuicui/Main.jsp')
        time.sleep(3)
        pyautogui.click(672, 346)  #Clique na posição do campo de usuário 
        check_for_esc()
        pyautogui.typewrite('fpaula002') #Coloca o login
        pyautogui.click(682, 558) #Clica no next
        time.sleep(1.5)
        check_for_esc()
        pyautogui.click(672, 361) #Clica no campo de senha
        time.sleep(0.5)
        check_for_esc()
        pyautogui.typewrite('8959') #Coloca a senha
        time.sleep(0.2)
        pyautogui.press('enter')
        check_for_esc()
        time.sleep(5)