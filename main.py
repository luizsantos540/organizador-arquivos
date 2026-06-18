import shutil
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

ignorar = {
    "main.py",
    "README.md",
    ".gitignore"
}

caminho = input("Digite o caminho da pasta que deseja organizar: ")

pasta = Path(caminho)

if not pasta.exists():
    print("\nA pasta informada não existe.")
    exit()

print("\nOrganizando arquivos...\n")

for arquivo in pasta.iterdir():

    if not arquivo.is_file():
        continue

    if arquivo.name in ignorar:
        continue

    categoria = categorias.get(
        arquivo.suffix.lower(),
        "Outros"
    )

    pasta_destino = pasta / categoria

    pasta_destino.mkdir(exist_ok=True)

    destino = pasta_destino / arquivo.name

    shutil.move(str(arquivo), str(destino))

    print(f"{arquivo.name} movido para {destino}")

print("\nOrganização concluída!")