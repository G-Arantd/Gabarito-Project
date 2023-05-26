from PIL import Image, ImageEnhance

def ajustar_brilho_contraste(imagem, nivel_brilho, nivel_contraste):
    # Abrir a imagem utilizando a PIL
    imagem_pil = Image.open(imagem)

    # Converter a imagem para escala de cinza
    imagem_pil = imagem_pil.convert("L")

    # Criar um objeto de melhoria da imagem
    melhoria_imagem = ImageEnhance.Brightness(imagem_pil)

    # Ajustar o brilho
    imagem_brilho = melhoria_imagem.enhance(nivel_brilho)

    # Criar um objeto de melhoria do contraste
    melhoria_contraste = ImageEnhance.Contrast(imagem_brilho)

    # Ajustar o contraste
    imagem_ajustada = melhoria_contraste.enhance(nivel_contraste)

    return imagem_ajustada

# Carregar a imagem
imagem_original = 'Image/testgabarito.jpg'

# Ajustar o brilho e contraste
nivel_brilho = 1.5  # Valor maior que 1 aumenta o brilho, valor menor que 1 diminui o brilho
nivel_contraste = 3.5  # Valor maior que 1 aumenta o contraste, valor menor que 1 diminui o contraste
imagem_ajustada = ajustar_brilho_contraste(imagem_original, nivel_brilho, nivel_contraste)

# Salvar a imagem com o nome específico
imagem_ajustada.save('Image/testgabarito_ajustada.jpg')

print("Imagem salva com sucesso.")
