from PIL import Image, ImageDraw, ImageFont
import qrcode

widthA4 = 2480
heightA4 = 3508

imageWidth = 654
imageHeight = 184

pathImage = Image.open("./Gabarito-Project/Backend/Gabarito.jpg")

mainImage = Image.new("RGB", (widthA4, heightA4), "white")

repeat = 10

for i in range(0, repeat):
    x_pos = int((widthA4 / 2) - int(imageWidth / 2) + 1)
    y_pos = int(heightA4 / 2.5) + int(190 * i)
    mainImage.paste(pathImage, (x_pos, y_pos))

qrSize = 350
qrXpos = (int(widthA4 / 2) - int(qrSize / 2))
qrYpos = int(heightA4/2)-750

qr_content = "2022013990"
aluno = "Gabriel Arantd Felipe"

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(qr_content)
qr.make(fit=True)
qrcode_img = qr.make_image(fill_color="black", back_color="white").resize((qrSize, qrSize))

mainImage.paste(qrcode_img, (qrXpos, qrYpos))

pathLogo = Image.open("./Gabarito-Project/Backend/Logo.png")

heightLogo = 536
widthLogo = 960

logoX = (int(widthA4/2)-int(widthLogo/2)-30)
logoY = 100

mainImage.paste(pathLogo, (logoX, logoY))

titleX = 930
titleY = 675

title_text = "GABARITO"
title_font = ImageFont.truetype("arial.ttf", 120)

draw = ImageDraw.Draw(mainImage)

draw.text((titleX, titleY), title_text, font=title_font, fill="black")

raX = 100
raY = 3400

raText = "Nome: "+aluno+" RA: "+qr_content
raFont = ImageFont.truetype("arial.ttf", 50)

draw = ImageDraw.Draw(mainImage)

draw.text((raX, raY), raText, font=raFont, fill="black")


mainImage.save("./Gabarito-Project/Backend/imageTest.png")