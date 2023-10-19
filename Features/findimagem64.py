import cv2
import numpy as np
import pyautogui
import base64
import time

def find_image_on_screen(image_base64, region=None, tolerance=0.8):
    # Decodifica a imagem em base64 para bytes
    image_bytes = base64.b64decode(image_base64)

    # Converte os bytes para um array numpy
    image_np = np.frombuffer(image_bytes, dtype=np.uint8)

    # Lê a imagem usando o OpenCV
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    # Captura uma captura de tela na região especificada
    screenshot = pyautogui.screenshot(region=region)

    # Converte a captura de tela para um array numpy
    screenshot_np = np.array(screenshot)

    # Tenta encontrar a imagem na captura de tela
    result = cv2.matchTemplate(screenshot_np, image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Se a correspondência for encontrada dentro da tolerância especificada, retorna a posição da imagem
    if max_val > tolerance:
        image_width, image_height = image.shape[1], image.shape[0]
        top_left = max_loc
        bottom_right = (top_left[0] + image_width, top_left[1] + image_height)
        return top_left, bottom_right
    else:
        return None

# Imagem em base64 que você deseja procurar na tela
image_base64 = "iVBORw0KGgoAAAANSUhEUgAAAB8AAAAXCAYAAADz/ZRUAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAEQSURBVEhL3ZI7CsJQEEWzgazTVrC20NrYWrkFGxHBJmsQG21cgY0rGHMDI5P7/iIGDBzIfM970UpEktR1LTnwXApvksHiybSR2Xwri2Yvy/VBVpuT7I4XOV8fXYuML1cwk4M3ydjFsUPc7s8/lOdIFZ4P4U0CuwyUyH3wfuAkFAykhPoe68OTLbenHUWeknIu1W8vZF3Obws+leccwpHzUGhJanmO3OLIYwtK5LFePEXyqvt7gFhN4T1cH8gtLEeMgbZte/Bub2trtge1WL2Xd4d445PzMGKV2xrei2OWM76b2885WFYaWzkzuhzw0E/kCg+FDlUc+2QMD4XyxbEuCmEH7OA36n1DCjRbvlOX6gXNogoZme4q0wAAAABJRU5ErkJggg=="

# Região onde procurar a imagem (left, top, width, height)
region = (0, 0, pyautogui.size().width, pyautogui.size().height)

# Tolerância para a correspondência da imagem (ajuste conforme necessário)
tolerance = 0.8

while True:
    # Procura a imagem na tela
    result = find_image_on_screen(image_base64, region, tolerance)

    # Se a imagem for encontrada, imprime a posição
    if result:
        print("Imagem encontrada na posição:", result)
        # Adicione aqui o código para realizar ações quando a imagem for encontrada
    else:
        print("Imagem não encontrada na tela.")

    # Aguarda o intervalo de tempo antes da próxima iteração
    time.sleep(1)
