import cloudinary
import cloudinary.api
import csv

# Configurar as credenciais do Cloudinary
cloudinary.config(
  cloud_name= 'dkhqk9bz2', 
  api_key= '766563287624973', 
  api_secret= 'vxveqxIg-ZigtalWZWpPi7n7GBo' 
)

# Definir o número máximo de resultados por página
max_results = 500  # Defina o valor desejado ou use -1 para recuperar todas as imagens

# Pasta específica no Cloudinary (caminho completo)
folder_path = 'Artes Outlet dos Quadros'  # Substitua pelo caminho completo da pasta desejada

# Variável para armazenar todas as imagens
all_images = []

# Função para recuperar imagens de uma pasta e suas subpastas
def get_images_in_folder(folder_path):
    result = cloudinary.api.resources(max_results=max_results, folder=folder_path)
    if 'resources' in result:
        all_images.extend(result['resources'])
        next_cursor = result.get('next_cursor')
        while next_cursor:
            result = cloudinary.api.resources(max_results=max_results, next_cursor=next_cursor, folder=folder_path)
            if 'resources' in result:
                all_images.extend(result['resources'])
                next_cursor = result.get('next_cursor')
            else:
                break

# Recuperar imagens da pasta específica e suas subpastas
get_images_in_folder(folder_path)

# Verificar se foram encontradas imagens
if all_images:
    # Caminho do arquivo CSV
    csv_filename = r'C:/Users/Administrador/OneDrive - Arte Propria/SISTEMA/ARTE PRÓPRIA/Nuvemshop/DownloadsURLImagens.csv'

    # Abrir o arquivo CSV em modo de escrita (substituir arquivo existente)
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        # Cabeçalho do CSV
        fieldnames = ['Nome', 'URL']

        # Criar o objeto de escrita CSV
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Escrever o cabeçalho no arquivo CSV
        writer.writeheader()

        # Escrever as informações de cada imagem no arquivo CSV
        for image in all_images:
            nome = image['public_id']
            url = image['url']

            # Escrever a linha no arquivo CSV
            writer.writerow({'Nome': nome, 'URL': url})

    print(f'O arquivo CSV "{csv_filename}" foi gerado com sucesso!')
else:
    print('Nenhuma imagem encontrada no Cloudinary.')
