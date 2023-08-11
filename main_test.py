# import cloudinary
# import cloudinary.api
# import csv

# # Configurar as credenciais do Cloudinary
# cloudinary.config(
#   cloud_name='de9nzomvv',
#   api_key='952772444116636',
#   api_secret='octTeoYlz-47kE9HJK5kJi2hr0k'
# )

# # Definir o número máximo de resultados por página
# max_results = 500  # Defina o valor desejado ou use -1 para recuperar todas as imagens

# # Variável para armazenar todas as imagens
# all_images = []

# # Primeira chamada para recuperar as imagens
# result = cloudinary.api.resources(max_results=max_results)

# # Verificar se as imagens foram encontradas
# if 'resources' in result:
#   all_images.extend(result['resources'])
#   next_cursor = result.get('next_cursor')

#   # Continuar recuperando imagens enquanto houver um próximo cursor
#   while next_cursor:
#     result = cloudinary.api.resources(max_results=max_results, next_cursor=next_cursor)

#     if 'resources' in result:
#       all_images.extend(result['resources'])
#       next_cursor = result.get('next_cursor')
#     else:
#       break

# # Verificar se foram encontradas imagens
# if all_images:
#   # Caminho do arquivo CSV
#   csv_filename = r'C:/Users/Administrador/OneDrive - Arte Propria/SISTEMA/DROPSHIPPING/URLImages.csv'

#   # Abrir o arquivo CSV em modo de escrita (substituir arquivo existente)
#   with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
#     # Cabeçalho do CSV
#     fieldnames = ['Nome', 'URL']

#     # Criar o objeto de escrita CSV
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     # Escrever o cabeçalho no arquivo CSV
#     writer.writeheader()

#     # Escrever as informações de cada imagem no arquivo CSV
#     for image in all_images:
#       nome = image['public_id']
#       url = image['url']

#       # Escrever a linha no arquivo CSV
#       writer.writerow({'Nome': nome, 'URL': url})

#   print(f'O arquivo CSV "{csv_filename}" foi gerado com sucesso!')
# else:
#   print('Nenhuma imagem encontrada no Cloudinary.')