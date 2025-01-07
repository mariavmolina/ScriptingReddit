# Scripting Traducción y Generación de Imágenes

Este script traduce automáticamente publicaciones de Reddit al español y genera imágenes estilizadas con el texto traducido, ideal para contenido en redes sociales.

## Tecnologías y Bibliotecas Usadas

- **Python 3.10+**
- **PRAW**: Para acceder al contenido de Reddit.
- **Googletrans**: Traducción automática (compatible con `googletrans==4.0.0rc1`).
- **Pillow**: Generación de imágenes.
- **Textwrap**: Ajuste dinámico del texto en las imágenes.

## Requisitos

1. Python 3.10 o superior.
2. Instalar las dependencias:
   ```bash
   pip install praw googletrans==4.0.0rc1 pillow
3. Descargar la fuente Roboto desde Google Fonts y guardarla en la carpeta del proyecto.
Uso
Clona este repositorio:

```bash
git clone https://github.com/tuusuario/ScriptingTraduccion.git
cd ScriptingTraduccion
```
Ejecuta el script:
```bash
python3 main.py
```
Ingresa el enlace de una publicación de Reddit.
El script traducirá el contenido y generará una imagen con el texto traducido, guardada como output.png.

