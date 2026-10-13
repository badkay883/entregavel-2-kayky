import cv2
import os
from arquivos import ler_anotacoes_csv


def main():
    caminho_csv = os.path.join('dados', 'anotacoes.csv')
    os.makedirs('resultados', exist_ok=True)

    try:
        lista_imagens = ler_anotacoes_csv(caminho_csv)

        if len(lista_imagens) != 10:
            raise ValueError(
                f"O CSV deve conter anotações para dez imagens; "
                f"foram encontradas {len(lista_imagens)}."
            )

        print("Iniciando visualizador de anotações...")

        for img_anotada in lista_imagens:
            imagem_original = cv2.imread(img_anotada.caminho_imagem)

            if imagem_original is None:
                raise ValueError(
                    f"Não foi possível ler a imagem "
                    f"'{img_anotada.caminho_imagem}'."
                )

            altura, largura = imagem_original.shape[:2]

            for deteccao in img_anotada.deteccoes:
                if not (
                    0 <= deteccao.x_min < deteccao.x_max < largura
                    and 0 <= deteccao.y_min < deteccao.y_max < altura
                ):
                    raise ValueError(
                        f"Coordenadas fora da imagem "
                        f"'{img_anotada.caminho_imagem}'."
                    )

            imagem_desenhada = img_anotada.gerar_imagem_anotada(
                imagem_original
            )
            nome_arquivo = os.path.basename(img_anotada.caminho_imagem)
            qtd_caixas = len(img_anotada.deteccoes)

            print(
                f"Imagem atual: {nome_arquivo} | "
                f"Caixas desenhadas: {qtd_caixas}"
            )

            caminho_saida = os.path.join('resultados', nome_arquivo)
            if not cv2.imwrite(caminho_saida, imagem_desenhada):
                raise ValueError(
                    f"Não foi possível salvar a imagem '{caminho_saida}'."
                )

            imagem_exibicao = imagem_desenhada.copy()
            texto_legenda = (
                f"{nome_arquivo} | Classe 0: Verde | Classe 1: Azul"
            )

            cv2.putText(
                imagem_exibicao,
                texto_legenda,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                4
            )
            cv2.putText(
                imagem_exibicao,
                texto_legenda,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2
            )

            altura, largura = imagem_exibicao.shape[:2]
            max_altura, max_largura = 720, 1280

            if altura > max_altura or largura > max_largura:
                proporcao = min(
                    max_largura / largura,
                    max_altura / altura
                )
                nova_largura = int(largura * proporcao)
                nova_altura = int(altura * proporcao)
                imagem_exibicao = cv2.resize(
                    imagem_exibicao,
                    (nova_largura, nova_altura)
                )

            cv2.imshow("Visualizador Harpia", imagem_exibicao)

            while True:
                tecla = cv2.waitKey(0) & 0xFF

                if tecla == ord(' '):
                    break
                elif tecla == ord('q'):
                    print("Execução encerrada pelo usuário.")
                    return

        print("Visualização das dez imagens concluída.")

    except (FileNotFoundError, ValueError, UnicodeDecodeError) as erro:
        print(f"Erro: {erro}")

    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()