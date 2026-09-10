import os
import cv2

# Caminho da pasta onde estão as imagens
pasta_entrada = "raw_images"

# Percorre as pastas de imagens
for categoria in os.listdir(pasta_entrada):
    caminho_categoria = os.path.join(pasta_entrada, categoria)

    # Verefica se é uma pasta
    if os.path.isdir(caminho_categoria):

        # Percorre os arquivos da pasta
        for arquivo in os.listdir(caminho_categoria):
            caminho_imagem = os.path.join(caminho_categoria, arquivo)

            # tenta carregar a imagem
            imagem = cv2.imread(caminho_imagem)

            if imagem is not None:
                print(f"imagem carregada: {caminho_imagem}")