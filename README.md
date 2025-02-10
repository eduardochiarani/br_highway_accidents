
---

## 📋 Sobre o Projeto

> Este projeto tem como objetivo analisar dados abertos da PRF, referentes
> aos acidentes nos anos de 2021 à 2024, aplicando técnicas de analise de
> dados e ciência de dados para gerar insights a partir desses dados.  
> Uma das análises realizadas, foi a de acidentes com vítimas devido a
> ingestão de álcool, verificando o comportamento do fenômeno durante
> os dias da semana e períodos do dia. Como resultados iniciais,
> observa-se a alta frequência deste tipo de acidente entre sábado e
> domingo, e durante a noite e madrugada.

---

## 🚀 Funcionalidades

- Análise exploratória de dados e Engenharia de atributos
- Geração de gráficos
- Comportamento geográfico com Mapas de Localização e Calor
- Apresentação visual dos dados usando Streamlit

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Gerenciadores de Dependências:** `pip`, `venv`
- **Ferramentas:** 
  - Streamlit, Pandas, Matplotlib, Plotly, Folium

---
## Configurando o ambiente

- Docker 🚧 em desenvolvimento 🚧
- Configuração virtual environment:

1. Instale o Python > 3.12
    - [Guia para instalação](https://medium.com/@nara.guimaraes/guia-de-instala%C3%A7%C3%A3o-do-python-em-diferentes-plataformas-10ea027c1869) (Win, Linux e MacOS)

    - No terminal, verfique a instalação digitando 
    ```bash
    python --version
    ```

2. Instalação de ambiente virtual e dependências do projeto:
    - Navegue até o diretório do projeto ou de sua escolha
    ```
    cd <caminho-do-diretorio-de-sua-escolha>
    ```
    - Crie o ambiente virtual
    ```
    python -m venv venv
    ```
    - Ative o ambiente virtual
    ```
    source venv/scripts/activate
    ```
    - E instale as dependências usando o arquivo requirements do projeto
    ```
    pipenv install -r requirements.txt
    ```

---
## Obtendo a base de dados
    
A fonte de dados utilizada:

- [Dados Abertos da PRF](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf)
- Os dados considerados foram os documentos em CSV de acidentes agrupados por ocorrência, dos anos 2021 a 2024.

---
## Processo de limpeza

1. Na pasta data, execute o script
    ```
    data_cleaning.py
    ```
2. Verifique se o arquivo ``\data\processed\df_concat.csv`` foi criado

---

## Acessando Streamlit

1. Para visualização dos resultados no Streamlit, no diretório do projeto e com o ambiente virtual venv ativo , digite:
    ```
    streamlit run src/Inicio.py
    ```

---

## 📂 Estrutura do Projeto

```plaintext

br_highway_accidents/ 
├── src/                   
│   ├── Inicio.py          # Arquivo de inicialização do Streamlit
│   └── pages/             
│       ├── 1_             # Página de revisão do dataset
│       ├── 2_             # Análise de acidentes com vítimas e ingestão de álcool
│       └── 3_             # Mapas com localização da ocorrência e densidade dos acidentes
│
├── data/                  # Dados utilizados pela aplicação
│   ├── raw/               # Dados brutos
│   ├── processed/         # Dados processados
│   └── data_cleaning.py   # Limpeza dos dados
│
├── requirements.txt       # Dependências do projeto
├── Dockerfile             # Arquivo Docker para containerização
└── README.md              # Documentação do projeto

```