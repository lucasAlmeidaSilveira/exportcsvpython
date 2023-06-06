import cloudinary
import cloudinary.api
import csv
import os

# Configurar as credenciais do Cloudinary
cloudinary.config(
  cloud_name='de9nzomvv',
  api_key='952772444116636',
  api_secret='octTeoYlz-47kE9HJK5kJi2hr0k'
)

# Recuperar as informações das imagens do Cloudinary
images = cloudinary.api.resources()

# Verificar se as imagens foram encontradas
if 'resources' in images:
  # Caminho do arquivo CSV
  csv_filename = r'Z:/compartilhada/E-commerce Arte Própria/URLImagens.csv'

  # Verificar se o diretório pai do arquivo CSV existe, caso contrário, criar
  os.makedirs(os.path.dirname(csv_filename), exist_ok=True)

  # Abrir o arquivo CSV em modo de escrita
  with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    # Cabeçalho do CSV
    fieldnames = ['URL']

    # Criar o objeto de escrita CSV
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Escrever o cabeçalho no arquivo CSV
    writer.writeheader()

    # Escrever as URLs de cada imagem no arquivo CSV
    for image in images['resources']:
      url = image['url']

      # Escrever a linha no arquivo CSV
      writer.writerow({'URL': url})

  print(f'O arquivo CSV "{csv_filename}" foi gerado com sucesso!')
else:
  print('Nenhuma imagem encontrada no Cloudinary.')
