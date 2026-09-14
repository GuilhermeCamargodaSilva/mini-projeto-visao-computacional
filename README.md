# Mini-Projeto - Visão Computacional

## Informações Acadêmicas

**Curso:** Machine Learning e Visão Computacional  
**Módulo:** Módulo 2  
**Projeto:** Mini-Projeto Avaliativo  
**Aluno:** Guilherme Camargo da Silva

---

##  Descrição

Este projeto foi desenvolvido como parte do Mini-Projeto Avaliativo do módulo de Machine Learning e Visão Computacional.

O projeto simula uma etapa de pré-processamento de imagens aplicada a um cenário de inspeção visual industrial.

A partir do dataset **Casting Product Image Data for Quality Inspection**, são utilizadas técnicas de Visão Computacional com Python e OpenCV para preparar as imagens para uma futura aplicação de Machine Learning.

O projeto realiza diferentes etapas de processamento, como conversão para escala de cinza, redução de ruído, aplicação de threshold, operações morfológicas, detecção de bordas, redimensionamento e salvamento das imagens processadas.

> **Importante:** o projeto tem como foco o pré-processamento das imagens e não realiza a classificação automática das peças.

---

##  Contextualização

Em ambientes industriais, a inspeção visual pode ser utilizada para verificar a qualidade de peças produzidas.

Antes de utilizar imagens em um modelo de Machine Learning, é necessário realizar etapas de pré-processamento para reduzir ruídos, destacar características importantes e padronizar os dados.

Neste projeto, as imagens de peças metálicas são processadas utilizando técnicas de Visão Computacional, preparando-as para uma possível utilização em uma etapa futura de classificação.

---

##  Objetivo

Desenvolver um pipeline de processamento de imagens capaz de:

- Carregar imagens em lote;
- Converter imagens coloridas para escala de cinza;
- Reduzir ruídos;
- Aplicar threshold utilizando o método de Otsu;
- Realizar operações morfológicas;
- Detectar bordas utilizando Canny;
- Redimensionar as imagens para 256x256 pixels;
- Salvar as imagens processadas de forma organizada.

---

##  Funcionalidades

O sistema realiza automaticamente as seguintes etapas:

### 1. Carregamento das imagens

As imagens são carregadas em lote a partir das pastas:

```text
raw_images/
├── ok_front/
└── def_front/

O programa percorre as categorias e processa cada imagem encontrada.

2. Conversão para escala de cinza

As imagens são convertidas de BGR para escala de cinza utilizando o OpenCV.

cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

Essa etapa reduz as informações de cor da imagem e facilita o processamento posterior.

3. Redução de ruído

É utilizado o filtro Gaussian Blur para suavizar as imagens e reduzir pequenos ruídos.

cv2.GaussianBlur(imagem, (5, 5), 0)
4. Threshold

É aplicado o método de Otsu para realizar a segmentação da imagem.

cv2.threshold(
    imagem,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
5. Operações morfológicas

São realizadas operações de erosão e dilatação utilizando um kernel retangular.

Essas operações ajudam no tratamento da estrutura da imagem após a aplicação do threshold.

6. Detecção de bordas

As bordas das peças são detectadas utilizando o algoritmo Canny.

cv2.Canny(imagem, 100, 200)

Essa etapa permite destacar os contornos presentes nas imagens.

7. Redimensionamento

Após o processamento, as imagens são redimensionadas para:

256 x 256 pixels

Essa padronização permite que todas as imagens tenham as mesmas dimensões para uma possível utilização futura em Machine Learning.

8. Salvamento das imagens

As imagens processadas são salvas automaticamente na pasta:

processed_images/
├── ok_front/
└── def_front/

A organização das categorias originais é mantida nos arquivos processados.

 Pipeline de Processamento

O processamento segue a seguinte sequência:

Imagem original
      ↓
Conversão para escala de cinza
      ↓
Redução de ruído
      ↓
Threshold com Otsu
      ↓
Erosão
      ↓
Dilatação
      ↓
Detecção de bordas com Canny
      ↓
Redimensionamento para 256x256
      ↓
Salvamento da imagem processada
 Organização do Código

O projeto utiliza Programação Orientada a Objetos (POO) para organizar as etapas do processamento.

A classe principal do projeto é:

ProcessadorImagens

Cada etapa do processamento foi organizada em um método específico:

converter_cinza()
reduzir_ruido()
aplicar_threshold()
aplicar_morfologia()
detectar_bordas()
redimensionar_imagem()
salvar_imagem()
carregar_imagens()

Essa organização facilita a leitura, manutenção e evolução do código.

 Tecnologias e Bibliotecas
Python

Linguagem utilizada para desenvolvimento do projeto.

OpenCV

Biblioteca utilizada para as operações de processamento de imagens.

Entre os recursos utilizados estão:

Conversão de imagens;
Gaussian Blur;
Threshold;
Operações morfológicas;
Canny;
Resize;
Salvamento de imagens.
OS

Biblioteca nativa do Python utilizada para manipulação de diretórios e caminhos de arquivos.

 Dataset

O projeto utiliza o dataset Casting Product Image Data for Quality Inspection.

As imagens são organizadas nas categorias:

ok_front/
def_front/
Download do dataset

O dataset utilizado neste projeto pode ser obtido através do seguinte link:

**[Download do Dataset - Google Drive](https://drive.google.com/file/d/1K5gNxQ7RXA-nb4boNzPYQTJlRvJyYBD1/view?usp=sharing)**
Após realizar o download e extrair os arquivos, organize as imagens da seguinte maneira:

raw_images/
├── ok_front/
└── def_front/

Importante: as imagens do dataset não são enviadas para o GitHub. As pastas raw_images/ e processed_images/ estão configuradas no .gitignore.

 Pré-requisitos

Para executar o projeto, é necessário possuir:

Python 3;
Git;
Visual Studio Code (recomendado).

Para verificar a instalação do Python:

python --version

ou:

py --version
 Estrutura do Projeto
mini-projeto-visao-computacional/
│
├── .venv/
│
├── raw_images/
│   ├── ok_front/
│   └── def_front/
│
├── processed_images/
│   ├── ok_front/
│   └── def_front/
│
├── .gitignore
├── main.py
└── requirements.txt
Descrição dos arquivos

.venv/

Ambiente virtual utilizado para isolar as dependências do projeto.

raw_images/

Contém as imagens originais utilizadas como entrada.

processed_images/

Contém as imagens após o processamento.

main.py

Arquivo principal responsável pela execução do pipeline.

requirements.txt

Contém as dependências utilizadas no projeto.

.gitignore

Impede que arquivos e pastas que não devem ser enviados ao GitHub sejam versionados.

🚀 Instalação
1. Clonar o repositório
git clone https://github.com/GuilhermeCamargodaSilva/mini-projeto-visao-computacional.git

Entre na pasta do projeto:

cd mini-projeto-visao-computacional
2. Criar o ambiente virtual
python -m venv .venv
3. Ativar o ambiente virtual

No Windows PowerShell:

.venv\Scripts\Activate.ps1

No Windows CMD:

.venv\Scripts\activate

Após a ativação, o terminal deverá apresentar:

(.venv)
4. Instalar as dependências

Com o ambiente virtual ativado:

pip install -r requirements.txt
 Execução

Após configurar o ambiente e organizar o dataset, execute:

python main.py

O programa irá percorrer as imagens presentes em raw_images, realizar todas as etapas de processamento e salvar os resultados em processed_images.

Durante a execução, o terminal apresenta informações sobre as etapas realizadas.

Exemplo:

Imagem em cinza: (512, 512)
Ruído reduzido: (512, 512)
Threshold aplicado: (512, 512)
Morfologia aplicada: (512, 512)
Bordas detectadas: (512, 512)
Imagem redimensionada: (256, 256)
Imagem salva: processed_images/ok_front/cast_ok_0_35.jpeg
 Resultado Esperado

Ao final da execução, as imagens processadas estarão organizadas por categoria:

processed_images/
├── ok_front/
│   ├── cast_ok_0_35.jpeg
│   ├── cast_ok_0_37.jpeg
│   └── ...
│
└── def_front/
    ├── cast_def_0_0.jpeg
    ├── cast_def_0_2.jpeg
    └── ...

Todas as imagens processadas possuem tamanho padronizado de:

256 x 256 pixels

O processamento destaca principalmente os contornos e bordas das peças, preparando as imagens para uma possível utilização futura em modelos de Machine Learning.

 Etapas do Desenvolvimento

O desenvolvimento do projeto foi realizado de forma incremental, seguindo as etapas propostas para o mini-projeto:

Configuração do repositório Git;
Criação do ambiente virtual;
Instalação das dependências;
Organização do dataset;
Implementação do carregamento das imagens em lote;
Conversão para escala de cinza;
Redução de ruído;
Aplicação de threshold;
Operações morfológicas;
Detecção de bordas;
Redimensionamento das imagens;
Salvamento das imagens processadas;
Documentação do projeto.
 Git e Branches

O controle de versão do projeto foi realizado utilizando Git.

Durante o desenvolvimento, foi utilizada a branch:

development

As alterações foram registradas através de commits incrementais.

Entre os commits realizados estão:

chore: configuracao estrutura inicial do projeto
chore: registra dependencias do projeto
feat: adiciona carregamento de imagens em lote
feat: adiciona processamento de imagens
feat: adiciona operacoes morfologicas
feat: adiciona deteccao de bordas
feat: adiciona redimensionamento das imagens
feat: adiciona salvamento das imagens processadas
 Possíveis Melhorias Futuras

Como continuidade do projeto, algumas melhorias poderiam ser implementadas:

Criar uma interface para visualizar as etapas do processamento;
Comparar automaticamente imagens originais e processadas;
Testar diferentes parâmetros de threshold;
Avaliar outros métodos de detecção de bordas;
Utilizar outras operações morfológicas;
Desenvolver uma etapa de classificação utilizando Machine Learning;
Avaliar métricas de desempenho do modelo.
🎥 Vídeo de Apresentação

O vídeo de apresentação do projeto está disponível no Google Drive:

**[Assistir ao vídeo de apresentação](https://drive.google.com/file/d/1uv8sF3bdVIZXOg-nxvO6WozwSX1NJ7OR/view?usp=sharing)**
 Autor

Guilherme Camargo da Silva