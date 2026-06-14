from pathlib import Path

pasta = Path(".")

print("Arquivos encontrados:")

for arquivo in pasta.iterdir():
    if arquivo.is_file():
        print(arquivo.name)