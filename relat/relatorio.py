import pyautogui
import time
import keyboard
import datetime
from execucao.esc_encerra import check_for_esc
from relat.reconhece_data import se_segunda, pegar_data, pegar_ontem

def gerar_relatorio():
        check_for_esc()
# Função para navegar e gerar o relatório
        time.sleep(0.5)
        # Espera a página carregar
        pyautogui.click(44, 409)  # Clica em 'reports' 
        time.sleep(9)
        check_for_esc()
        
        pyautogui.click(156, 359)  # Clica em 'Stock' 
        check_for_esc()
        time.sleep(0.8)

        pyautogui.click(287, 390)  # Clica em 'Unified CCX Historical' 
        time.sleep(0.8)
        check_for_esc()

        pyautogui.click(191, 470)  # Clica em 'inbound' 
        time.sleep(1)
        check_for_esc()
        for _ in range(5): #rolando a pagina para baixo
                pyautogui.press('pagedown')
                time.sleep(0.5)
        pyautogui.click(245, 607)  # Clica em 'Detailed Call CSQ Agent Report'
        check_for_esc()
        time.sleep(2.5)
        pyautogui.click(420, 400)  # Clica no campo 'DateRange'
        check_for_esc() 
        
        if se_segunda(): #Função se for segunda, pegar ultimos 3 dias
                pegar_data()
        else:            #Se não, pegar apenas dia de ontem
                pegar_ontem() 

        check_for_esc()
        time.sleep(0.5)
        pyautogui.click(730, 359)  # Clica no campo em branco 
        for _ in range(7): #Rolando a pagina para baixo
                pyautogui.press('pagedown')
                time.sleep(0.3)
        check_for_esc()
        pyautogui.click(432, 407)  # Clica no PwC_TI - alterado
        time.sleep(0.5)
        check_for_esc()
        pyautogui.click(721, 402)  # Clica no TI_csq # alterado
        time.sleep(0.3)
        check_for_esc()
        pyautogui.click(1100, 663)  # Clica em run
        check_for_esc()
        time.sleep(5.7)
        check_for_esc()
        pyautogui.click(1097, 275)  # Clica na engrenagem 
        time.sleep(0.9)
        check_for_esc()
        pyautogui.click(1101, 343)  # Clica em export 
        time.sleep(1.7)
        #Sai do sistema
        time.sleep(1.5)
        pyautogui.click(924, 141)  # Clica em branco
        time.sleep(0.9)
        pyautogui.click(1329, 148)  # Clica no usuario
        time.sleep(0.9)
        pyautogui.click(1329, 221)  # Clica em SignOut
        time.sleep(1.1)
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(1)