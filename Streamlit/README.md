# 📊 Projeto de Análise de Dados com Streamlit

Este projeto é uma aplicação web interativa desenvolvida com [Streamlit](https://streamlit.io/) para análise e visualização de dados. A aplicação permite aos usuários explorar, analisar e visualizar dados de forma dinâmica e intuitiva.

## 🎯 Sobre o Projeto

O projeto foi desenvolvido para facilitar a análise exploratória de dados, oferecendo uma interface amigável e interativa. Ele permite que usuários, mesmo sem conhecimento técnico avançado, possam realizar análises complexas através de uma interface web intuitiva.

## 📁 Estrutura do Projeto

```
project_streamlit/
├── app.py                       # Arquivo principal da aplicação
├── README.md                    # Documentação
├── requirements.txt             # Dependências do projeto
├── infrastructure/              # Diretório com módulos de suporte
│   ├── __init__.py          
│   ├── analysis.py              # Funções para análise de visualiação
│   ├── data_loader_process.py   # Processamento de dados
│   └── metrics.py               # Métricas e cálculos estatísticos
└── utils/                       # Utilitários e configurações
    ├── __init__.py          
    ├── style.py                 # Configurações de estilo da aplicação
    └── logger.py                # Configuração de logs
```

## 🚀 Como Executar a Aplicação

1. Clone o repositório:
   ```bash
   git clone [URL_DO_REPOSITÓRIO]
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd project_streamlit
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```bash
   streamlit run app.py
   ```

📍 Acesse no navegador: [http://localhost:8501](http://localhost:8501)

## ⚙️Funcionalidades Principais

- **Carregamento de Dados**
  - Carregamento e tratamento automático de dados faltantes
  - Validação de dados

- **Análise Exploratória**
  - Visualizações interativas
  - Métricas financeiras e comportamentais

- **Recursos Interativos**
  - Filtros por variáveis categóricas ou numéricas
  - Seleção de atributos para visualização
 
## 🌐 Demonstração da Aplicação

![Demonstração em execução](./streamlit.gif)




