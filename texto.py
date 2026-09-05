import requests
from bs4 import BeautifulSoup
import pandas as pd
# Guardar el script completo en un archivo .py local
script_code = """import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://libreriamorelos.mx/novedades/index.html"
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")
libros = soup.find_all("div", class_="product-footer")

datos = []

for libro in libros:
    enlace = libro.find("a")
    titulo = enlace.text.strip()

    autor_tag = libro.find("a", class_="author")
    autor = autor_tag.text.strip() if autor_tag else "Sin autor"

    precio_tag = libro.find("div", class_="mt-2 price theme-color link text-center")
    precio_texto = precio_tag.text.strip() if precio_tag else "0"
    precio = float(precio_texto.replace("$", "").replace(",", ""))

    datos.append({
        "titulo": titulo,
        "autor": autor,
        "precio_mxn": precio
    })

df = pd.DataFrame(datos)
df.to_csv("catalogo_libros_LibreriaMorelos.csv", index=False)
print("Scraping exitoso y archivo catalogo_libros.csv creado.")
"""

with open("texto.py", "w", encoding="utf-8") as f:
    f.write(script_code)
