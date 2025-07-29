import requests
from bs4 import BeautifulSoup

def extraer_datos_web(url):
    """Descarga una página web y extrae título, encabezados y párrafos."""

    # Encabezado para evitar bloqueo por bots
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Descargar la página
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanza error si falla
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al acceder a la URL: {e}")
        return

    # Analizar el HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extraer título de la página
    titulo = soup.title.string.strip() if soup.title else "Sin título"
    print(f"\n📄 Título de la página: {titulo}")

    # Extraer encabezados h1
    print("\n📰 Encabezados (h1):")
    for h1 in soup.find_all("h1"):
        print(f" - {h1.get_text(strip=True)}")

    # Extraer párrafos
    print("\n📑 Párrafos:")
    for p in soup.find_all("p"):
        texto = p.get_text(strip=True)
        if texto:
            print(f" - {texto}")

# ---------- USO ----------
if __name__ == "__main__":
    url = input("🔗 Introduce la URL a analizar: ").strip()
    extraer_datos_web(url)