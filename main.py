import cv2
import os


class ProcessadorImagens:

    def __init__(self, pasta_entrada):
        self.pasta_entrada = pasta_entrada

    def converter_cinza(self, imagem):
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        return imagem_cinza

    def reduzir_ruido(self, imagem):
        imagem_suavizada = cv2.GaussianBlur(imagem, (5, 5), 0)
        return imagem_suavizada

    def aplicar_threshold(self, imagem):
        _, imagem_threshold = cv2.threshold(
            imagem,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        return imagem_threshold

    def aplicar_morfologia(self, imagem):
        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (3, 3)
        )

        imagem_erodida = cv2.erode(
            imagem,
            kernel,
            iterations=1
        )

        imagem_dilatada = cv2.dilate(
            imagem_erodida,
            kernel,
            iterations=1
        )

        return imagem_dilatada

    def carregar_imagens(self):

        for categoria in os.listdir(self.pasta_entrada):

            caminho_categoria = os.path.join(
                self.pasta_entrada,
                categoria
            )

            if not os.path.isdir(caminho_categoria):
                continue

            for nome_imagem in os.listdir(caminho_categoria):

                caminho_imagem = os.path.join(
                    caminho_categoria,
                    nome_imagem
                )

                imagem = cv2.imread(caminho_imagem)

                if imagem is None:
                    print(f"Erro ao carregar: {caminho_imagem}")
                    continue

                imagem_cinza = self.converter_cinza(imagem)

                imagem_suavizada = self.reduzir_ruido(
                    imagem_cinza
                )

                imagem_threshold = self.aplicar_threshold(
                    imagem_suavizada
                )

                imagem_morfologica = self.aplicar_morfologia(
                    imagem_threshold
                )

                print(f"Imagem carregada: {caminho_imagem}")
                print(f"Imagem em cinza: {imagem_cinza.shape}")
                print(f"Ruído reduzido: {imagem_suavizada.shape}")
                print(f"Threshold aplicado: {imagem_threshold.shape}")
                print(f"Morfologia aplicada: {imagem_morfologica.shape}")


processador = ProcessadorImagens("raw_images")

processador.carregar_imagens()