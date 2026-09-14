import cv2
import os


class ProcessadorImagens:

    def __init__(self, pasta_entrada):
        # Define a pasta onde estão as imagens originais
        self.pasta_entrada = pasta_entrada

    def converter_cinza(self, imagem):
        # Converte a imagem colorida para escala de cinza
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        return imagem_cinza

    def reduzir_ruido(self, imagem):
        # Aplica um filtro para suavizar e reduzir ruídos
        imagem_suavizada = cv2.GaussianBlur(imagem, (5, 5), 0)
        return imagem_suavizada

    def aplicar_threshold(self, imagem):
        # Utiliza Otsu para separar os elementos da imagem
        _, imagem_threshold = cv2.threshold(
            imagem,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        return imagem_threshold

    def aplicar_morfologia(self, imagem):
        # Cria um kernel para as operações morfológicas
        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (3, 3)
        )

        # Realiza a erosão para tratar pequenos detalhes
        imagem_erodida = cv2.erode(
            imagem,
            kernel,
            iterations=1
        )

        # Realiza a dilatação após a erosão
        imagem_dilatada = cv2.dilate(
            imagem_erodida,
            kernel,
            iterations=1
        )

        return imagem_dilatada

    def detectar_bordas(self, imagem):
        # Detecta os contornos presentes na imagem
        imagem_bordas = cv2.Canny(imagem, 100, 200)
        return imagem_bordas

    def redimensionar_imagem(self, imagem):
        # Padroniza todas as imagens para 256x256 pixels
        imagem_redimensionada = cv2.resize(
            imagem,
            (256, 256)
        )
        return imagem_redimensionada

    def salvar_imagem(self, imagem, categoria, nome_imagem):
        # Define a pasta de saída de acordo com a categoria
        pasta_saida = os.path.join(
            "processed_images",
            categoria
        )

        # Cria a pasta caso ela ainda não exista
        os.makedirs(pasta_saida, exist_ok=True)

        caminho_saida = os.path.join(
            pasta_saida,
            nome_imagem
        )

        # Salva a imagem processada
        cv2.imwrite(caminho_saida, imagem)

    def carregar_imagens(self):

        # Percorre as categorias de imagens
        for categoria in os.listdir(self.pasta_entrada):

            caminho_categoria = os.path.join(
                self.pasta_entrada,
                categoria
            )

            if not os.path.isdir(caminho_categoria):
                continue

            # Percorre todas as imagens da categoria
            for nome_imagem in os.listdir(caminho_categoria):

                caminho_imagem = os.path.join(
                    caminho_categoria,
                    nome_imagem
                )

                # Carrega a imagem utilizando o OpenCV
                imagem = cv2.imread(caminho_imagem)

                if imagem is None:
                    print(f"Erro ao carregar: {caminho_imagem}")
                    continue

                # Etapa 1: conversão para escala de cinza
                imagem_cinza = self.converter_cinza(imagem)

                # Etapa 2: redução de ruído
                imagem_suavizada = self.reduzir_ruido(
                    imagem_cinza
                )

                # Etapa 3: aplicação do threshold
                imagem_threshold = self.aplicar_threshold(
                    imagem_suavizada
                )

                # Etapa 4: operações morfológicas
                imagem_morfologica = self.aplicar_morfologia(
                    imagem_threshold
                )

                # Etapa 5: detecção de bordas
                imagem_bordas = self.detectar_bordas(
                    imagem_morfologica
                )

                # Etapa 6: redimensionamento
                imagem_redimensionada = self.redimensionar_imagem(
                    imagem_bordas
                )

                # Etapa 7: salvamento da imagem processada
                self.salvar_imagem(
                    imagem_redimensionada,
                    categoria,
                    nome_imagem
                )

                print(
                    f"Imagem salva: "
                    f"processed_images/{categoria}/{nome_imagem}"
                )

                print(f"Imagem carregada: {caminho_imagem}")
                print(f"Imagem em cinza: {imagem_cinza.shape}")
                print(f"Ruído reduzido: {imagem_suavizada.shape}")
                print(f"Threshold aplicado: {imagem_threshold.shape}")
                print(f"Morfologia aplicada: {imagem_morfologica.shape}")
                print(f"Bordas detectadas: {imagem_bordas.shape}")
                print(
                    f"Imagem redimensionada: "
                    f"{imagem_redimensionada.shape}"
                )


# Cria o processador apontando para a pasta das imagens originais
processador = ProcessadorImagens("raw_images")

# Inicia o processamento de todas as imagens
processador.carregar_imagens()