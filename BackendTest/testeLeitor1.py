import cv2
from pyzbar import pyzbar

def lerQRCode(imagem):
    # Carrega a imagem
    img = cv2.imread(imagem)

    # Converte para escala de cinza
    img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecta os códigos de barras na imagem
    qr_codes = pyzbar.decode(img_cinza)

    # Verifica se algum QR code foi encontrado
    if qr_codes:
        # Extrai o conteúdo do primeiro QR code encontrado
        dados = qr_codes[0].data.decode("utf-8")
    else:
        dados = "Nenhum QR code encontrado na imagem"

    return dados

def readAnswerSheet(pathImage, numAnswer, correctAnswers, valueAnswers):

    # Var
    image = cv2.imread(pathImage)
    answer = ["A", "B", "C", "D"]
    coords = [(1413, 1808), (1613, 1808), (1813, 1808), (2013, 1808)]
    w, h = 100, 100
    moveY = 240

    studentAnswers = []
    nota = 0

    # Process

    for i in range(1, numAnswer):
        for j in range(4):

            x, y = coords[j][0] + (i - 1) * 7, coords[j][1] + (i - 1) * moveY
            
            roi = image[y:y+h, x:x+w]
            
            media = cv2.mean(roi)[0]
            
            if media < 175:
                studentAnswers.append(answer[j])
    
    print (studentAnswers)
    
    #Valid

    for i in range (0, len(studentAnswers)):
        
        if studentAnswers[i] == correctAnswers[i]:
            nota = nota+valueAnswers[i]

    student = lerQRCode(pathImage)

    return student, nota

print (readAnswerSheet("Image/testgabarito_ajustada.jpg", 11, ["B","D","B","A","C","A","C","D","B","C"], [1,1,1,1,1,1,1,1,1,1]))