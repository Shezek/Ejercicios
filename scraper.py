import requests
from bs4 import BeautifulSoup
import csv

def extraer_datos_web(url):
    """Scrapea una URL y guarda título, encabezados y párrafos en un CSV."""
    headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f" Error al acceder a la URL: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Preparar datos
    titulo = soup.title.string.strip() if soup.title else "Sin título"
    encabezados = [h1.get_text(strip=True) for h1 in soup.find_all("h1")]
    parrafos = [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]

    # Guardar en CSV
    with open("datos_web.csv", mode="w", newline="", encoding="utf-8") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["Tipo", "Contenido"])  # Cabecera

        writer.writerow(["Título", titulo])
        for h in encabezados:
            writer.writerow(["Encabezado", h])
        for p in parrafos:
            writer.writerow(["Párrafo", p])

    print("\n Datos guardados en 'datos_web.csv'.")

# ---------- USO ----------
if __name__ == "__main__":
    url = input(" Introduce la URL a analizar: ").strip()
    extraer_datos_web(url)


