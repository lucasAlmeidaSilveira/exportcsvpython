import cloudinary
import cloudinary.api

# Configurar as credenciais do Cloudinary
cloudinary.config(
    cloud_name='de9nzomvv',
    api_key='952772444116636',
    api_secret='octTeoYlz-47kE9HJK5kJi2hr0k'
)

# Definir o número máximo de resultados por página
max_results = 500  # Defina o valor desejado ou use -1 para recuperar todas as imagens

# Pasta específica no Cloudinary (caminho completo)
folder_path = 'Imagens NuvemShop'  # Substitua pelo caminho completo da pasta desejada

# Variável para armazenar todas as imagens que contêm "Ambientes" na URL
images_with_ambientes = []

# Função para recuperar imagens de uma pasta e suas subpastas
def get_images_in_folder(folder_path):
    result = cloudinary.api.resources(max_results=max_results, folder=folder_path)
    if 'resources' in result:
        for resource in result['resources']:
            if 'Ambientes' in resource['url']:
                images_with_ambientes.append(resource)
        next_cursor = result.get('next_cursor')
        while next_cursor:
            result = cloudinary.api.resources(max_results=max_results, next_cursor=next_cursor, folder=folder_path)
            if 'resources' in result:
                for resource in result['resources']:
                    if 'Ambientes' in resource['url']:
                        images_with_ambientes.append(resource)
                next_cursor = result.get('next_cursor')
            else:
                break

# Recuperar imagens da pasta específica e suas subpastas
get_images_in_folder(folder_path)

# Verificar se foram encontradas imagens com "Ambientes"
if images_with_ambientes:
    # Caminho do arquivo JavaScript
    js_filename = r'C:/Users/Administrador/OneDrive - Arte Propria/Documentos/Arte Própria/Programação/api-nuvemshop/src/db/image_urls_ambients.js'

    # Abrir o arquivo JavaScript em modo de escrita (substituir arquivo existente)
    with open(js_filename, 'w', encoding='utf-8') as jsfile:
        # Escrever o início do objeto no arquivo
        jsfile.write("export const urlImages = {\n")

        # Escrever as informações de cada imagem no arquivo JavaScript
        for image in images_with_ambientes:
            nome = image['public_id'].replace('/', '_')  # Substitua '/' por '_' para evitar problemas no nome da variável
            url = image['url']

            # Escrever a linha no arquivo JavaScript
            jsfile.write(f'    "{nome}": "{url}",\n')

        # Escrever o final do objeto no arquivo
        jsfile.write("};\n")

    print(f'O arquivo JavaScript "{js_filename}" foi gerado com sucesso!')
else:
    print('Nenhuma imagem contendo "Ambientes" foi encontrada no Cloudinary.')
