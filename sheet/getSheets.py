import openpyxl
import pyperclip
import pyautogui
import time
import webbrowser
import glob
import os
# from execucao.esc_encerra import check_for_esc

def sheets():
        def get_latest_file():
            #Obter a lista de arquivos na pasta Downloads que começam com "Detailed Call CSQ Agent" e terminam com ".xlsx"
            list_of_files = glob.glob(os.path.join(os.path.expanduser('~'), 'Downloads', 'Detailed Call CSQ Agent*.xlsx'))
            if not list_of_files:
                raise FileNotFoundError("Nenhum arquivo encontrado na pasta Downloads com o prefixo 'Detailed Call CSQ Agent'.")
            # check_for_esc()
            #Selecionar o arquivo mais recente
            latest_file = max(list_of_files, key=os.path.getctime)
            return latest_file
           
        def copiar_valores(input_file):
            #Abrir a planilha de entrada
            wb = openpyxl.load_workbook(input_file)
            ws = wb.active
            # check_for_esc()
            #String para armazenar os dados
            data_str = ""
            # check_for_esc()
            #Iterar sobre as células da coluna A
            for row in ws.iter_rows(min_col=1, max_col=14):  #max_col=14 representa a coluna N
                cell = row[0]
                if str(cell.value).startswith('1'):
                    #Preparar os valores da coluna A até N e adicionar à string
                    row_values = [str(cell.value) if cell.value is not None else "" for cell in row[:14]]
                    data_str += "\t".join(row_values) + "\n"
            # check_for_esc()
            #Copiar os dados para a área de transferência
            pyperclip.copy(data_str)
            # check_for_esc()
        #Obter o arquivo mais recente na pasta Downloads
        input_file = get_latest_file()
        copiar_valores(input_file)
        
        #Abrir a planilha do Google Sheets no navegador padrão
        url = 'https://docs.google.com/spreadsheets/d/108_GQeqU-4AVT2g02XXd9iolNdviCH7QzJ35FP92u9Q/edit?gid=1388688123#gid=1388688123'
        webbrowser.open(url)
        #Esperar a página carregar (ajuste o tempo conforme necessário)
        time.sleep(13)
        # check_for_esc()
        #Descer até a última célula vazia (segurando Ctrl e pressionando Down)
        pyautogui.keyDown('ctrl')
        for _ in range(3):  # Pressionar 'down' várias vezes para garantir que chegue ao final
            pyautogui.press('down')
            time.sleep(0.1)
        pyautogui.keyUp('ctrl')
        # check_for_esc()
        time.sleep(5)
        pyautogui.press('down')
        # check_for_esc()
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        # check_for_esc()
        #Manter o navegador aberto por algum tempo antes de finalizar o script
        time.sleep(5)