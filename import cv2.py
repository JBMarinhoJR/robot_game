import cv2
import numpy as np
from collections import Counter

# Carregue a imagem
imagem = cv2.imread('C:/Users/Junior/Downloads/piseaqui.png')

# Converta a imagem de BGR para RGB (OpenCV carrega a imagem em formato BGR)
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Redimensione a imagem para reduzir a quantidade de pixels (opcional)
# Isso pode acelerar o processo, mas pode resultar em menos precisão nas cores
# imagem_rgb = cv2.resize(imagem_rgb, (100, 100))  # Redimensione para 100x100 pixels

# Converta a imagem em um array NumPy
pixels = np.array(imagem_rgb)

# Reshape o array em uma lista de pixels (cada pixel é uma lista [R, G, B])
pixels = pixels.reshape(-1, 3)

# Use Counter para contar a ocorrência de cada cor
contagem_cores = Counter(map(tuple, pixels))

# Classifique as cores pela contagem em ordem decrescente
cores_mais_comuns = contagem_cores.most_common()

# Exiba as cores mais comuns e suas contagens
for cor, contagem in cores_mais_comuns:
    print(f'Cor: RGB{cor}, Contagem: {contagem}')