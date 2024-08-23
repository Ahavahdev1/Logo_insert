# Logo_insert
Documentação do Programa: Adição de Logotipo a Imagens
1. Introdução
Este programa em Python permite adicionar um logotipo a uma imagem existente. O logotipo é posicionado no canto inferior direito da imagem, e a imagem resultante é salva em um diretório específico.

2. Pré-requisitos
Antes de executar o programa, é necessário ter o seguinte instalado no seu ambiente:

Python 3.6+: O programa é escrito em Python e requer uma versão moderna do Python.
Pillow: Biblioteca de manipulação de imagens. Pode ser instalada com o seguinte comando:
bash
Copy code
pip install Pillow
3. Estrutura de Diretórios
O programa espera uma estrutura de diretórios específica para localizar a imagem e o logotipo, bem como para salvar a imagem resultante.

php
Copy code
C:\
└── ia\
    └── logotipo\
        ├── Imagem\
        │   └── <imagem.jpg>
        ├── logotipo.png
        └── Imagem\
            └── imglogo\
                └── <imagem_com_logotipo.jpg>
C:\ia\logotipo\Imagem\: Contém a imagem original.
C:\ia\logotipo\logotipo.png: Contém o logotipo a ser adicionado.
C:\ia\logotipo\Imagem\imglogo\: Pasta onde a imagem com o logotipo será salva.
4. Código do Programa
4.1. Descrição do Código
O código realiza as seguintes operações:

Busca o primeiro arquivo de imagem na pasta Imagem.
Busca o arquivo de logotipo na pasta logotipo.
Redimensiona o logotipo para ocupar 10% da largura da imagem original.
Posiciona o logotipo no canto inferior direito da imagem.
Salva a nova imagem com o logotipo na pasta imglogo.
4.2. Código Completo
python
Copy code
import os
from PIL import Image

# Caminhos das pastas
pasta_imagem = r'C:\ia\logotipo\Imagem'
pasta_logotipo = r'C:\ia\logotipo'
pasta_salvar = r'C:\ia\logotipo\Imagem\imglogo'

# Criar a pasta de salvamento se não existir
os.makedirs(pasta_salvar, exist_ok=True)

# Encontrar o primeiro arquivo de imagem na pasta
imagem_arquivo = next((f for f in os.listdir(pasta_imagem) if f.endswith(('.jpg', '.jpeg', '.png'))), None)
logotipo_arquivo = next((f for f in os.listdir(pasta_logotipo) if f.endswith(('.jpg', '.jpeg', '.png'))), None)

if imagem_arquivo and logotipo_arquivo:
    caminho_imagem = os.path.join(pasta_imagem, imagem_arquivo)
    caminho_logotipo = os.path.join(pasta_logotipo, logotipo_arquivo)
    caminho_salvar = os.path.join(pasta_salvar, f"imagem_com_logotipo_{imagem_arquivo}")

    # Abrir imagem e logotipo
    imagem = Image.open(caminho_imagem)
    logotipo = Image.open(caminho_logotipo)

    # Redimensionar logotipo, se necessário
    largura_logotipo, altura_logotipo = logotipo.size
    proporcao = 0.1  # Logotipo ocupará 10% da largura da imagem
    largura_nova = int(imagem.width * proporcao)
    altura_nova = int((largura_nova / largura_logotipo) * altura_logotipo)
    logotipo = logotipo.resize((largura_nova, altura_nova), Image.Resampling.LANCZOS)

    # Posição para colocar o logotipo (canto inferior direito)
    posicao = (imagem.width - logotipo.width, imagem.height - logotipo.height)

    # Adicionar o logotipo à imagem
    imagem.paste(logotipo, posicao, logotipo)

    # Salvar a imagem com o logotipo
    imagem.save(caminho_salvar)

    print("Imagem salva com sucesso em:", caminho_salvar)
else:
    print("Arquivo de imagem ou logotipo não encontrado.")
5. Como Executar o Programa
Prepare as Imagens:

Coloque a imagem que deseja editar na pasta C:\ia\logotipo\Imagem.
Coloque o logotipo que deseja adicionar na pasta C:\ia\logotipo.
Execute o Programa:

Abra um terminal (PowerShell, CMD ou terminal integrado do seu editor).
Navegue até a pasta C:\ia\logotipo.
Execute o programa com o comando:
bash
Copy code
python app.py
Resultado:

A imagem processada será salva na pasta C:\ia\logotipo\Imagem\imglogo com o nome imagem_com_logotipo_<nome_do_arquivo_original>.jpg.
6. Personalizações
Proporção do Logotipo: O código redimensiona o logotipo para ocupar 10% da largura da imagem. Você pode ajustar essa proporção modificando a variável proporcao.

Posição do Logotipo: O logotipo é colocado no canto inferior direito. Para alterar a posição, modifique a variável posicao.

7. Erros Comuns
Imagem ou Logotipo Não Encontrado: Verifique se os arquivos estão nas pastas corretas e com extensões de imagem suportadas (.jpg, .jpeg, .png).
Permissões de Arquivo: Verifique se você tem permissões adequadas para acessar e salvar arquivos nos diretórios especificados.
8. Conclusão
Este programa é uma ferramenta útil para adicionar logotipos a imagens automaticamente. Ele é flexível e pode ser facilmente adaptado para diferentes necessidades de redimensionamento e posicionamento do logotipo.

