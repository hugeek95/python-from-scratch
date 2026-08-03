import os
from PIL import Image
from pillow_heif import register_heif_opener

# Permite que Pillow pueda abrir imágenes HEIC
register_heif_opener()

def convertir_heic_a_jpeg(carpeta_entrada, carpeta_salida):
    os.makedirs(carpeta_salida, exist_ok=True)

    for archivo in os.listdir(carpeta_entrada):
        if archivo.lower().endswith(".heic"):
            ruta_entrada = os.path.join(carpeta_entrada, archivo)

            nombre_sin_extension = os.path.splitext(archivo)[0]
            ruta_salida = os.path.join(carpeta_salida, nombre_sin_extension + ".jpg")

            try:
                imagen = Image.open(ruta_entrada)

                # Convertir a RGB para evitar problemas con transparencia o perfiles
                imagen = imagen.convert("RGB")

                imagen.save(ruta_salida, "JPEG", quality=95)

                print(f"Convertido: {archivo} -> {nombre_sin_extension}.jpg")

            except Exception as e:
                print(f"Error al convertir {archivo}: {e}")


if __name__ == "__main__":
    carpeta_entrada = "C:/Users/hugui/OneDrive/Documents/Hugeek/Hugeek"
    carpeta_salida = "C:/Users/hugui/OneDrive/Documents/Hugeek/Salida"

    convertir_heic_a_jpeg(carpeta_entrada, carpeta_salida)