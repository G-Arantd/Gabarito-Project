from PIL import Image, ImageDraw, ImageFont
import qrcode

#Tamanho da Página
widthA4 = 2480
heightA4 = 3508

#Tamanho do Cartão resposta
imageWidth = 327
imageHeight = 184

#Caminho Imagem
pathImage = Image.open("Image/Componets/Gabarito.jpg")

#Criação da Página
mainImage = Image.new("RGB", (widthA4, heightA4), "white")

#Definições de Numero de Questão

repeat = 10

for i in range(0, repeat):
    x_pos = int((widthA4 / 2) - int(imageWidth / 2) + 1)
    y_pos = int(heightA4 / 1.55) + int(95 * i)
    mainImage.paste(pathImage, (x_pos, y_pos))

#Definições de QrCode

qrSize = 350
qrXpos = (int(widthA4 / 2) - int(qrSize / 2))
qrYpos = int(heightA4/2.25)-725

#Definição de qual aluno pertence

qr_content = "2022013990"
aluno = "Gabriel Arantd Felipe"

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(qr_content)
qr.make(fit=True)
qrcode_img = qr.make_image(fill_color="black", back_color="white").resize((qrSize, qrSize))

mainImage.paste(qrcode_img, (qrXpos, qrYpos))

# Caminha da Logo da Cesul

pathLogo = Image.open("Image/Componets/Logo.png")

#Definição de Tamanho da Logo e localização

heightLogo = 536
widthLogo = 960
logoX = (int(widthA4/2)-int(widthLogo/2)-30)
logoY = 100

mainImage.paste(pathLogo, (logoX, logoY))

#Definição de texto "Gabarito" na página

titleX = 930
titleY = 675

title_text = "GABARITO"
title_font = ImageFont.truetype("arial.ttf", 120)

draw = ImageDraw.Draw(mainImage)

draw.text((titleX, titleY), title_text, font=title_font, fill="black")

#Definição de indentificação do aluno na prova

raX = 75
raY = 3400

raText = "Nome: "+aluno+" RA: "+qr_content+"       Assinatura do Aluno: ___________________________"
raFont = ImageFont.truetype("arial.ttf", 50)

draw = ImageDraw.Draw(mainImage)

draw.text((raX, raY), raText, font=raFont, fill="black")

for i in range(0, repeat):

    if i < 9:
        x_pos = int((widthA4 / 2 - 550) - int(imageWidth / 2 - 500) + 1)
    else:
        x_pos = int((widthA4 / 2 - 580) - int(imageWidth / 2 - 500) + 1)

    y_pos = int(heightA4 / 1.539) + int(95 * i)

    AnwserText = str(i+1)+"-"
    draw.text((x_pos, y_pos), AnwserText, font=raFont, fill="black")

x_pos = 1037
y_pos = int(heightA4 / 2.75)

title_font = ImageFont.truetype("arial.ttf", 95)
draw.text((x_pos, y_pos), "REGRAS", font=title_font, fill="black")


for i in range(0, 4):

    regras = ["1- Usar canetas preta ou azul, para marcar as respostas no gabarito. Pois na hora da correção podem \nnão ser detectadas corretamente.",
              "2- Preencher os Círculos completamente de acordo com sua resposta. Qualquer preenchimento fora do \npadrão pode resultar na anulação da questão.",
              "3- Marcar apenas uma questão no gabarito, pois o preenchimento de mais de uma alternativa irá anular \na questão.",
              "4- Evitar marcação fora dos círculos designados e no Qr Code impedindo sua leitura."]

    x_pos = 75

    y_pos = int(heightA4 / 2.35) + int(145 * i)

    AnwserText = str(i+1)+"-"
    draw.text((x_pos, y_pos), regras[i], font=raFont, fill="black")
    
x_pos = 945
y_pos = int(heightA4 / 1.65)

title_font = ImageFont.truetype("arial.ttf", 95)
draw.text((x_pos, y_pos), "QUESTÕES", font=title_font, fill="black")

mainImage.save("answerCardPrint.png")