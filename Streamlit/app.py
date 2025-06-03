"""Aplicação Streamlit para análise de dados de Churn."""

import streamlit as st
from utils.style import inject_custom_css
from infrastructure.data_loader_process import load_process
from infrastructure.metrics import ChurnMetrics
from infrastructure.analysis import ChurnPlots

st.set_page_config(
        page_title="Análise Churn",
        page_icon="🏦",
        layout="wide"
    )

inject_custom_css()

# Instancia as classes
plots = ChurnPlots()
metrics = ChurnMetrics()

def main():
    """Função principal que configura e executa a aplicação Streamlit."""

    st.title("Análise sobre Churn de Clientes Bancários 🏦")

    st.write("""
    A retenção de clientes é um dos maiores desafios enfrentados pelas instituições financeiras. 
    Identificar os fatores que levam um cliente a encerrar seu relacionamento com o banco — o chamado *churn* — 
    é essencial para o desenvolvimento de estratégias eficazes de fidelização e mitigação de perdas.

    Nesta aplicação, realizaremos uma análise exploratória de dados com base em um conjunto de informações de clientes bancários, disponível no 
    [Kaggle](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn/data). 
    Nosso objetivo é compreender o perfil dos clientes que tendem a sair, detectar padrões de comportamento e avaliar quais variáveis mais influenciam a decisão de churn.
                 
    """)
    st.markdown("---")

    # Carregando os dados
    data_churn = load_process()
    if data_churn is None:
        st.error("Erro ao carregar os dados. Por favor, verifique o arquivo de dados.")
        return

    # 01. Visão Geral
    st.markdown("## Visão Geral de Indicadores", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total de clientes", metrics.total_customer(data_churn))
    col2.metric("Clientes Retidos", metrics.customer_retained(data_churn))
    col3.metric("Taxa de churn", metrics.rate_churn(data_churn))
    col4.metric("Pontuação média de satisfação", metrics.avg_satisfaction(data_churn))
    col5.metric("Saldo médio no banco", metrics.mean_balance(data_churn))

    # 02. Análise de Variáveis Categóricos
    st.markdown("## Análise de Variáveis Categóricos", unsafe_allow_html=True)

    columns_category = st.selectbox(
        "Selecione uma variável categórica para análise:",
        options=['Geography', 'Gender', 'HasCrCard', 'IsActiveMember', 'Complain', 'CardType'],
        index=0 
    )

    if columns_category:
        st.subheader(f"Distribuição de Clientes por {columns_category}")
        plots.graf_qualitative(data_churn, columns_category)

    # 03. Análise de Variáveis Numéricas
    st.markdown(" ## Análise de Variáveis Numéricas", unsafe_allow_html=True)

    columns_numerical = st.selectbox(
        "Selecione uma variável numérica para análise:",
        options=['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 
                 'EstimatedSalary', 'PointEarned', 'SatisfactionScore'],
        index=0 
    )

    if columns_numerical:
        st.subheader(f"Distribuição de Clientes por {columns_numerical}")
        plots.graf_numerical(data_churn, columns_numerical)

    # 04. Análise Demográfica
    st.markdown("## Análise Demográfica", unsafe_allow_html=True)
    gender = st.selectbox(
        "Selecione o gênero para análise: ",
        options = ["Todos"] + data_churn["Gender"].unique().tolist()
    )

    if gender != "Todos":
        data_churn_filtered = data_churn[data_churn["Gender"] == gender]
    else:
        data_churn_filtered = data_churn.copy()

    churn_geo = data_churn_filtered.groupby(["Exited", "Geography"]).size().reset_index(name='Count')
    fig_churn_geo = plots.churn_por_geo(churn_geo)
    if fig_churn_geo:
        st.plotly_chart(fig_churn_geo, use_container_width=True)

    # Análise Financeira
    st.markdown("## Churn por Perfil Financeiro", unsafe_allow_html=True)
    financial_feature = st.selectbox("Selecione uma característica financeira:", ['CreditScore', 'Balance', 'EstimatedSalary'])

    fig_churn_financial = plots.churn_financial(data_churn, financial_feature)
    if fig_churn_financial:
        st.plotly_chart(fig_churn_financial, use_container_width=True)

    # Engajamento com Produtos
    st.markdown("## Engajamento com Produtos", unsafe_allow_html=True)
    fig_products = plots.products(data_churn)
    if fig_products:
        st.plotly_chart(fig_products, use_container_width=True)

    # Análise de Comportamento
    st.markdown("## Churn e Comportamento do Cliente", unsafe_allow_html=True)
    fig_behavior = plots.behavior(data_churn)
    if fig_behavior:
        st.plotly_chart(fig_behavior, use_container_width=True)

    # Funil de Conversão
    st.markdown("## Funil de Conversão", unsafe_allow_html=True)
    fig_funnel = plots.graf_funil(data_churn)
    if fig_funnel:
        st.plotly_chart(fig_funnel, use_container_width=True)

    # Importancia das Variáveis
    st.markdown("## Importância das Variáveis", unsafe_allow_html=True)
    fig_importance = plots.graf_importance_variable(data_churn)
    if fig_importance:
        st.plotly_chart(fig_importance, use_container_width=True)
    
if __name__ == "__main__":
    main()
