import csv
import os
from modelos import Deteccao, ImagemAnotada


def ler_anotacoes_csv(caminho_csv):
    imagens = {}
    colunas_necessarias = {
        'imagem', 'classe_id', 'x_min', 'y_min', 'x_max', 'y_max'
    }

    try:
        with open(caminho_csv, mode='r', encoding='utf-8', newline='') as arquivo:
            leitor = csv.DictReader(arquivo)

            if not leitor.fieldnames or not colunas_necessarias.issubset(
                leitor.fieldnames
            ):
                raise ValueError("O CSV não contém todas as colunas necessárias.")

            for numero_linha, linha in enumerate(leitor, start=2):
                try:
                    nome_imagem = linha['imagem'].strip()
                    classe_id = int(linha['classe_id'])
                    x_min = int(linha['x_min'])
                    y_min = int(linha['y_min'])
                    x_max = int(linha['x_max'])
                    y_max = int(linha['y_max'])
                except (AttributeError, TypeError, ValueError, KeyError):
                    raise ValueError(
                        f"Campos inválidos na linha {numero_linha} do CSV."
                    )

                if not nome_imagem:
                    raise ValueError(
                        f"Nome de imagem vazio na linha {numero_linha}."
                    )

                if classe_id not in (0, 1):
                    raise ValueError(
                        f"Classe inválida na linha {numero_linha}: "
                        f"use 0 ou 1."
                    )

                if not (0 <= x_min < x_max and 0 <= y_min < y_max):
                    raise ValueError(
                        f"Coordenadas inválidas na linha {numero_linha}."
                    )

                if nome_imagem not in imagens:
                    caminho_imagem = os.path.join('imagens', nome_imagem)
                    imagens[nome_imagem] = ImagemAnotada(caminho_imagem)

                deteccao = Deteccao(
                    classe_id, x_min, y_min, x_max, y_max
                )
                imagens[nome_imagem].adicionar_deteccao(deteccao)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Arquivo CSV não encontrado: '{caminho_csv}'."
        )

    return [imagens[nome] for nome in sorted(imagens)]