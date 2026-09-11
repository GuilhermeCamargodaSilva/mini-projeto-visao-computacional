import os
import cv2


class ProcessadorImagens:

    def __init__(self, pasta_entrada):
        self.pasta_entrada = pasta_entrada

    def converter_cinza(self, imagem):
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        return imagem_cinza

    def reduzir_ruido(self, imagem):
        imagem_suavizada = cv2.GaussianBlur(
            imagem,
            (5, 5),
            0
        )

        return imagem_suavizada

    def aplicar_threshold(self, imagem):
        _, imagem_threshold = cv2.threshold(
            imagem,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        return imagem_threshold

    def carregar_imagens(self):

        for categoria in os.listdir(self.pasta_entrada):

            caminho_categoria = os.path.join(
                self.pasta_entrada,
                categoria
            )

            if os.path.isdir(caminho_categoria):

                for arquivo in os.listdir(caminho_categoria):

                    caminho_imagem = os.path.join(
                        caminho_categoria,
                        arquivo
                    )

                    imagem = cv2.imread(caminho_imagem)

                    if imagem is not None:

                        imagem_cinza = self.converter_cinza(imagem)

                        imagem_suavizada = self.reduzir_ruido(
                            imagem_cinza
                        )

                        imagem_threshold = self.aplicar_threshold(
                            imagem_suavizada
                        )

                        print(f"Imagem carregada: {caminho_imagem}")
                        print(
                            f"Imagem em cinza: {imagem_cinza.shape}"
                        )
                        print(
                            f"Ruído reduzido: {imagem_suavizada.shape}"
                        )
                        print(
                            f"Threshold aplicado: "
                            f"{imagem_threshold.shape}"
                        )


# Cria o objeto
processador = ProcessadorImagens("raw_images")

# Executa o processamento das imagens
processador.carregar_imagens()
