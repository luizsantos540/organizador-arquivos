from pathlib import Path

categorias = {
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",

    ".pdf": "Documentos",
    ".txt": "Documentos",
    ".docx": "Documentos",

    ".mp4": "Vídeos",
    ".avi": "Vídeos",

    ".mp3": "Áudios"
}

pasta = Path(".")

print("Arquivos encontrados:\n")

for arquivo in pasta.iterdir():
    if arquivo.is_file():

        categoria = categorias.get(
            arquivo.suffix.lower(),
            "Outros"
        )

        pasta_destino = Path(categoria)

        destino = pasta_destino / arquivo.name

        print(f"{arquivo.name} -> seria movido para {destino}")