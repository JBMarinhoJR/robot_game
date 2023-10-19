import pyautogui
import cv2
import numpy as np
import time
import pygetwindow as gw

# Caminho da imagem que você deseja usar
imagem_path = r"C:\Users\Junior\OneDrive\Documentos\robot_game\Features\recorte2.png"

# Carrega a imagem de referência usando o OpenCV
imagem_referencia = cv2.imread(imagem_path, 0)

# Loop para procurar a imagem na tela
while True:
    try:
        # Encontra a janela minimizada pelo título
        janela = gw.getWindowsWithTitle('(463) John Jr - BOT - 12/10/2023 - YouTube - Google Chrome')[0]

        # Restaura a janela minimizada se necessário
        if janela.isMinimized:
            janela.restore()

        # Captura uma imagem da tela
        tela = pyautogui.screenshot(region=(janela.left, janela.top, janela.width, janela.height))

        # Converte a imagem da tela para escala de cinza
        tela_gray = cv2.cvtColor(np.array(tela), cv2.COLOR_RGB2GRAY)

        # Tenta encontrar a imagem de referência na tela
        res = cv2.matchTemplate(tela_gray, imagem_referencia, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)  # Ajuste o valor de 0.8 conforme necessário

        if len(loc[0]) > 0:
            # Se a imagem for encontrada, imprime a posição e para o loop
            print("Imagem encontrada na posição:", (loc[1][0], loc[0][0]))
            break
        else:
            print("Imagem não encontrada. Tentando novamente em breve...")
            # Aguarde por um curto período antes de tentar novamente
            time.sleep(1)

    except Exception as e:
        print("Erro:", e)
        break