from pathlib import Path

pasta = Path(".")

print("Arquivos encontrados:\n")

for arquivo in pasta.iterdir():
    if arquivo.is_file():
        print(f"{arquivo.name} -> {arquivo.suffix}")