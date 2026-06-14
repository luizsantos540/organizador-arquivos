from pathlib import Path

pasta = Path(".")

print ("arquivos encontrados:")
for arquivo in pasta.iterdir():
    if arquivo.is_file():
        print (item.name)