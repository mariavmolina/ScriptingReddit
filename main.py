import praw
from googletrans import Translator
from PIL import Image,ImageDraw,ImageFont
import textwrap

reddit = praw.Reddit(
    client_id= '20HHqqNzoYym856YhM0WbA',
    client_secret='Av3lbfpB3UtKDtTLPOMaDm3IN9A-gw',
    user_agent='TraducciónScript/1.0'
)

def get_reddit_post(url):
    post= reddit.submission(url=url)
    return post.title, post.selftext

def translate_text(text,target_lenguage='es'):
    translator=Translator()
    traslation=translator.translate(text,dest=target_lenguage)
    return traslation.text


def generate_dynamic_image(title, content, output_path="output.png"):
    # Configuración inicial
    img_width = 800  # Ancho fijo de la imagen
    background_color = (0, 0, 0)  # Fondo negro
    text_color = (255, 255, 255)  # Texto blanco
    margin = 40  # Margen alrededor del texto
    max_font_title = 42  # Tamaño máximo del título
    max_font_content = 36  # Tamaño máximo del contenido

    # Cargar fuentes
    try:
        font_title = ImageFont.truetype("Roboto-Bold.ttf", max_font_title)
        font_content = ImageFont.truetype("Roboto-Regular.ttf", max_font_content)
    except IOError:
        print("Fuente no encontrada. Usa fuentes predeterminadas.")
        font_title = font_content = ImageFont.load_default()

    # Función para ajustar texto según el ancho
    def wrap_text(text, font, max_width):
        lines = []
        words = text.split()
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()
            text_width = font.getbbox(test_line)[2] - font.getbbox(test_line)[0]

            if text_width <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return lines

    # Ajustar las líneas del título y contenido
    title_lines = wrap_text(title, font_title, img_width - 2 * margin)
    content_lines = wrap_text(content, font_content, img_width - 2 * margin)

    # Calcular altura dinámica de la imagen
    title_height = sum(font_title.getbbox(line)[3] - font_title.getbbox(line)[1] for line in title_lines) + (len(title_lines) - 1) * 10
    content_height = sum(font_content.getbbox(line)[3] - font_content.getbbox(line)[1] for line in content_lines) + (len(content_lines) - 1) * 10
    img_height = margin * 2 + title_height + 30 + content_height

    # Crear la imagen
    img = Image.new("RGB", (img_width, img_height), background_color)
    draw = ImageDraw.Draw(img)

    # Dibujar el título
    y = margin
    for line in title_lines:
        draw.text((margin, y), line, fill=text_color, font=font_title)
        y += font_title.getbbox(line)[3] - font_title.getbbox(line)[1] + 10

    # Espaciado entre título y contenido
    y += 20

    # Dibujar el contenido
    for line in content_lines:
        draw.text((margin, y), line, fill=text_color, font=font_content)
        y += font_content.getbbox(line)[3] - font_content.getbbox(line)[1] + 10

    # Guardar la imagen
    img.save(output_path)
    print(f"Imagen generada: {output_path}")



if __name__=="__main__":
    reddit_url=input("Ingresa el enlace del post de Reddit: ")
    title,content=get_reddit_post(reddit_url)

    translated_title = translate_text(title)
    translated_content = translate_text(content)

    print("\nTítulo original: ", title)
    print("Título traducido: ", translated_title)
    print("\nContenido original: ", content)
    print("Contenido traducido: ", translated_content)

    generate_dynamic_image(translated_title, translated_content)

