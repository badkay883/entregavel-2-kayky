# Entregável 2 - Kayky Souza

**Objetivo:** 

Implementar um sistema em Python orientado a objetos para processar imagens, ler metadados de um arquivo CSV, validar a integridade das coordenadas e anotar visualmente os objetos detectados utilizando OpenCV.

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`.
- `opencv-python`
- `numpy`

## Instruções de Execução

1. Clone este repositório no seu ambiente local.
2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate

## Instale as dependências:

pip install -r requirements.txt

## Execute o programa principal:

python src/main.py

## Controles do Visualizador

Tecla de Espaço: Avança para a próxima imagem.

Tecla 'q': Encerra a visualização e o programa imediatamente.

## Explicação das Classes

Deteccao: Modela cada caixa delimitadora (bounding box). Armazena as coordenadas (x_min, y_min, x_max, y_max) e o rótulo da classe, definindo a cor da caixa (Verde para classe 0, Azul para classe 1).

ImagemAnotada: Gerencia todas as detecções de uma única imagem. Valida se as caixas estão dentro dos limites matemáticos da resolução e aplica os desenhos sobre a imagem original usando as funções do OpenCV.
