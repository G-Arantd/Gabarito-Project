import cv2

# carrega a imagem do gabarito
img = cv2.imread('gabarito.jpg')

# define os pontos de referência para cada uma das alternativas
pontos = [(1413, 1808), (1613, 1808), (1813, 1808), (2013, 1808)]

# define a largura e altura de cada caixa de seleção
w, h = 100, 100

# define a distância vertical entre as questões, em pixels
deslocamento_y = 240

# percorre as questões do gabarito
for i in range(1, 11):
    # percorre as alternativas de cada questão
    for j in range(4):
        # define as coordenadas da caixa de seleção atual
        x, y = pontos[j][0] + (i - 1) * 7, pontos[j][1] + (i - 1) * deslocamento_y
        # extrai a região da imagem correspondente à caixa de seleção
        roi = img[y:y+h, x:x+w]
        # calcula a média dos valores de pixel na região
        media = cv2.mean(roi)[0]
        # verifica se a caixa de seleção foi preenchida
        if media < 150:
            print(f"Questão {i}, alternativa {chr(j+65)}: marcada")
        else:
            #print(f"Questão {i}, alternativa {chr(j+65)}: não foi marcada")
            pass