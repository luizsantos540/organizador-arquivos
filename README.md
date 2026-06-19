 Organizador de Arquivos

 Descrição

O Organizador de Arquivos é uma ferramenta desenvolvida em Python que organiza automaticamente arquivos em pastas com base em suas extensões.

O usuário informa o caminho da pasta que deseja organizar, e o programa cria automaticamente categorias como Imagens, Documentos, Áudios e Vídeos, movendo cada arquivo para sua respectiva pasta.

 Funcionalidades

* Organização automática de arquivos.
* Criação automática de pastas por categoria.
* Escolha da pasta a ser organizada pelo usuário.
* Validação da existência da pasta informada.
* Contador de arquivos organizados.
* Suporte a múltiplas extensões de arquivos.

 Tecnologias utilizadas

* Python 3
* Git
* GitHub
* Biblioteca `pathlib`
* Biblioteca `shutil`

Extensões suportadas

Imagens

  .jpg`
  .jpeg`
  .png`

Documentos

.pdf`
.txt`
.docx`

Vídeos

.mp4`
.avi`

Áudios

.mp3`

Como executar o projeto

1. Clone o repositório:

bash

git clone https://github.com/luizsantos540/organizador-arquivos.git


2. Acesse a pasta do projeto:

bash

cd organizador-arquivos


3. Execute o programa
bash
python main.py


4. Informe o caminho da pasta que deseja organizar quando solicitado.

 Exemplo de uso

Antes:

text
Downloads/
├── foto.jpg
├── musica.mp3
├── trabalho.pdf


Depois:


Downloads/
├── Imagens/
│   └── foto.jpg
│
├── Áudios/
│   └── musica.mp3
│
├── Documentos/
│   └── trabalho.pdf


Autor

Desenvolvido por Luiz Manoel Ramalho Santos.
