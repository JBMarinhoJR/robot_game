import cv2
import numpy as np

# Carregue a imagem
imagem = cv2.imread('C:/Users/Junior/Downloads/piseaqui.png')

# Converta a imagem para o espaço de cores HSV
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Defina a faixa de valores de matiz (hue) para a cor laranja
cor_laranja_min = np.array([10, 100, 100])  # Matiz mínima, Saturação mínima, Valor mínima
cor_laranja_max = np.array([30, 255, 255])  # Matiz máxima, Saturação máxima, Valor máxima

# Crie uma máscara que seleciona os pixels na faixa de matiz laranja
mascara = cv2.inRange(imagem_hsv, cor_laranja_min, cor_laranja_max)

# Aplique a máscara à imagem original para manter apenas os pixels laranja
imagem_laranja = cv2.bitwise_and(imagem, imagem, mask=mascara)

# Salve a imagem resultante
cv2.imwrite('imagem_laranja.jpg', imagem_laranja)

# Exiba a imagem resultante (opcional)
cv2.imshow('Imagem Laranja', imagem_laranja)
cv2.waitKey(0)
cv2.destroyAllWindows()
