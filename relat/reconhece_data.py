import datetime
import pyautogui
import time
import keyboard

data_atual = datetime.date.today()

def se_segunda():
         
    # Verificar se hoje é segunda-feira (weekday() retorna 0 para segunda-feira)
    return  data_atual.weekday() == 0

def pegar_data():
        
        global data_atual

        sexta_anterior = data_atual - datetime.timedelta(days=3)
        sexta_formatada = sexta_anterior.strftime("%m/%d/%Y")

        domingo_anterior = data_atual - datetime.timedelta(days=1)
        domingo_formatado = domingo_anterior.strftime("%m/%d/%Y")
        
        # Separar os valores de MM/DD/YYYY da sexta-feira anterior
        mes_sexta, dia_sexta, ano_sexta = sexta_formatada.split('/')
        
        # Separar os valores de MM/DD/YYYY do domingo seguinte
        mes_dom, dia_dom, ano_dom = domingo_formatado.split('/')

        # Esperar 2 segundos para o usuário colocar o foco no primeiro campo
        time.sleep(2)

        # Clicar no campo desejado e colar a data da sexta-feira anterior
        pyautogui.click(x=437, y=432)  #clica em custom
        time.sleep(0.8)
        pyautogui.click(x=685, y=400) #clica na primeira data
        time.sleep(0.8)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.3)
        pyautogui.typewrite(sexta_formatada)
        time.sleep(1)
        pyautogui.click(x=929, y=400)  #clica na segunda data
        time.sleep(0.4)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.3)
        pyautogui.typewrite(domingo_formatado)

def pegar_ontem():
    time.sleep(0.4)
    pyautogui.click(423, 493)  # Clica no campo 'Yesterday' 

