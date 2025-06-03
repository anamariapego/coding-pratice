# Projeto de Análise de Dados com Streamlit

Este projeto utiliza Streamlit para criar uma aplicação web interativa para análise de dados.

## Estrutura do Projeto

```
project_streamlit/
├── app.py                 # Arquivo principal da aplicação
├── README.md             # Este arquivo
├── requirements.txt      # Dependências do projeto
├── data/                 # Diretório para armazenar os datasets
│   └── dataset.csv      # Dataset principal
└── infrastructure/       # Diretório com módulos de suporte
    ├── data_loader.py   # Funções para carregar e tratar dados
    └── analysis.py      # Funções para análise exploratória
```

## Instalação

1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando a Aplicação

Para executar a aplicação, use o comando:
```bash
streamlit run app.py
```

## Funcionalidades

- Carregamento e tratamento automático de dados
- Análise exploratória com visualizações interativas
- Estatísticas descritivas
- Análise de valores nulos
