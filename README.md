# 🚧🚧🚧 em desenvolvimento 🚧🚧🚧

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

- Análise exploratória de dados
- Engenharia de atributos
- Geração de gráficos
- Comportamento geográfico com mapas de localização e calor
- Apresentação visual dos dados usando Streamlit

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Gerenciadores de Dependências:** `pip`, `venv`
- **Ferramentas:** 
  - Streamlit
  - Pandas, NumPy, Matplotlib, Plotly, Seaborn, Folium

---

## 📂 Estrutura do Projeto

```plaintext

br_highway_accidents/ 
├── src/                   # Código-fonte principal
│   ├── app.py             # Arquivo principal do Streamlit
│   ├── pages/             # Várias páginas da aplicação
│   │   ├── home.py        # Página inicial
│   │   ├── analysis.py    # Página de análise
│   │   ├── mapa.py        # Página com mapas
│   │   └── dashboard.py   # Página de dashboard
│   ├── components/        # Módulos e layouts reutilizáveis
│   │   ├── sidebar.py     # Configuração da barra lateral
│   │   └── charts.py      # Funções para geração de gráficos
│   ├── utils/             # Funções auxiliares e lógica do negócio
│   │   ├── data_loader.py # Funções para carregar dados
│   │   └── plot_utils.py  # Funções para criação de gráficos
│   └── config.py          # Configurações gerais da aplicação
├── data/                  # Dados utilizados pela aplicação
│   ├── raw/               # Dados brutos
│   ├── processed/         # Dados processados
│   └── sample.csv         # Exemplo de dados
├── assets/                # Arquivos estáticos (imagens, CSS, etc.)
│   ├── styles.css         # Estilos personalizados
│   └── logo.png           # Imagens ou logos
├── tests/                 # Testes automatizados
│   ├── test_app.py        # Testes para a aplicação principal
│   └── test_utils.py      # Testes para funções auxiliares
├── requirements.txt       # Dependências do projeto
├── setup.sh               # Script de configuração inicial (opcional)
├── Dockerfile             # Arquivo Docker para containerização
├── .env.example           # Arquivo de exemplo para variáveis de ambiente
└── README.md              # Documentação do projeto

```

---
## Configurando o ambiente

1. Instale o Python 3.x
    - [Guia para instalação](https://medium.com/@nara.guimaraes/guia-de-instala%C3%A7%C3%A3o-do-python-em-diferentes-plataformas-10ea027c1869) (Win, Linux e MacOS)

    - Verfique a instalação 
        ```bash
        python --version
        ```

2. Gerênciador de ambientes virtuais
    - Recomendamos o uso de venv ou conda para isolar as dependências do projeto.

---
## Obtendo a base de dados
    
A fonte de dados utilizada:

- [Dados Abertos da PRF](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf)
- Os dados considerados foram os documentos em CSV de acidentes agrupados por ocorrência, dos anos 2021 a 2024.

---
## Processo de limpeza

1. Na pasta data, execute o script ``data_cleaning.py``
2. Verifique se o arquivo ``\data\processed\df_concat.csv`` foi criado
