import cv2


class Deteccao:
    def __init__(self, classe_id, x_min, y_min, x_max, y_max):
        self.classe_id = classe_id
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def desenhar(self, imagem):
        if self.classe_id == 0:
            cor = (0, 255, 0)  # Verde
        else:
            cor = (255, 0, 0)  # Azul

        cv2.rectangle(
            imagem,
            (self.x_min, self.y_min),
            (self.x_max, self.y_max),
            cor,
            2
        )


class ImagemAnotada:
    def __init__(self, caminho_imagem):
        self.caminho_imagem = caminho_imagem
        self.deteccoes = []

    def adicionar_deteccao(self, deteccao):
        self.deteccoes.append(deteccao)

    def gerar_imagem_anotada(self, imagem_original):
        imagem_copia = imagem_original.copy()

        for deteccao in self.deteccoes:
            deteccao.desenhar(imagem_copia)

        return imagem_copia