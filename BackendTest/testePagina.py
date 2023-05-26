import cv2
import numpy as np

def ajustar_contraste(imagem, nivel_contraste):
    # Converter a imagem para o formato HSV
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    # Aumentar o contraste no canal de valor (V)
    imagem_hsv[:,:,2] += nivel_contraste

    # Limitar os valores do canal de valor (V) entre 0 e 255
    imagem_hsv[:,:,2] = np.clip(imagem_hsv[:,:,2], 0, 255)

    # Converter a imagem de volta para o formato BGR
    nova_imagem = cv2.cvtColor(imagem_hsv, cv2.COLOR_HSV2BGR)

    return nova_imagem

# Carregar a imagem
imagem_original = cv2.imread('testgabarito.jpg')

# Ajustar o contraste
nivel_contraste = 50
imagem_contraste = ajustar_contraste(imagem_original, nivel_contraste)

# Redimensionar a imagem para exibição
largura_desejada = 800
proporcao = largura_desejada / imagem_contraste.shape[1]
altura_desejada = int(imagem_contraste.shape[0] * proporcao)
imagem_redimensionada = cv2.resize(imagem_contraste, (largura_desejada, altura_desejada))

# Exibir a imagem redimensionada
cv2.imshow('Imagem com Contraste', imagem_redimensionada)
cv2.waitKey(0)
cv2.destroyAllWindows()
