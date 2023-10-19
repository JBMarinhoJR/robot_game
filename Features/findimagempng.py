import cv2
import numpy as np
import pyautogui
import time

def find_image_on_screen(image_path):
    # Lê a imagem do arquivo
    image = cv2.imread(image_path)

    # Converte a profundidade e o tipo de dados da imagem
    image = cv2.convertScaleAbs(image)

    # Captura uma captura de tela
    screenshot = pyautogui.screenshot()

    # Converte a captura de tela para um array numpy
    screenshot_np = np.array(screenshot)

    # Converte a profundidade e o tipo de dados da captura de tela
    screenshot_np = cv2.convertScaleAbs(screenshot_np)

    # Tenta encontrar a imagem na captura de tela
    result = cv2.matchTemplate(screenshot_np, image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Se a correspondência for encontrada, retorna a posição da imagem
    if max_val > 0.8:
        image_width, image_height = image.shape[1], image.shape[0]
        top_left = max_loc
        bottom_right = (top_left[0] + image_width, top_left[1] + image_height)
        return top_left, bottom_right
    else:
        return None

# Exemplo de uso
if __name__ == "__main__":
    # Caminho para o arquivo da imagem PNG que você deseja procurar na tela
    image_path = "imagemteste.png"

    # Intervalo de tempo entre cada iteração (em segundos)
    intervalo = 1

    while True:
        # Procura a imagem na tela
        result = find_image_on_screen(image_path)

        # Se a imagem for encontrada, imprime a posição
        if result:
            print("Imagem encontrada na posição:", result)
        else:
            print("Imagem não encontrada na tela.")

        # Aguarda o intervalo de tempo antes da próxima iteração
        time.sleep(intervalo)
