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
