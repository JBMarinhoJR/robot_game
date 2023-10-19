import os
import base64

def image_to_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            # Lê a imagem como bytes
            image_bytes = image_file.read()
            # Converte os bytes em base64
            base64_image = base64.b64encode(image_bytes).decode('utf-8')
            return base64_image
    except Exception as e:
        print(f"Erro: {e}")
        return None

def save_base64_image(base64_image, output_path):
    try:
        with open(output_path, "w") as output_file:
            output_file.write(base64_image)
        print(f'Imagem base64 salva com sucesso em: {output_path}')
    except Exception as e:
        print(f"Erro ao salvar a imagem base64: {e}")

if __name__ == "__main__":
    # Obtém o caminho do diretório onde o script está localizado
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Caminho da imagem chamada "seta.png" na mesma pasta do script
    image_path = os.path.join(script_directory, 'imagemteste.png')

    # Converte a imagem em base64
    base64_image = image_to_base64(image_path)

    if base64_image:
        # Caminho para salvar o arquivo base64 na mesma pasta do script
        output_path = os.path.join(script_directory, 'base64_image_imagemteste.txt')
        # Salva a imagem base64 no arquivo
        save_base64_image(base64_image, output_path)
    else:
        print('Falha ao converter a imagem em base64.')
