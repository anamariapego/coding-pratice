# pip install streamlit
# import streamlit as st
# from infrastructure.data_loader import dataset
# import plotly.express as px

# https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn/data
# streamlit run app.py

# st.title("Análise sobre Churn de Clientes Bancários 🏦")
# st.markdown("---")
# st.write("""
#     A evasão de clientes é uma questão crítica para os bancos, pois reter clientes existentes é muito menos custoso do que adquirir novos. 
#     Ao entender os fatores que influenciam o churn, os bancos podem desenvolver programas de fidelidade e estratégias de retenção direcionadas 
#     para reduzir a rotatividade de clientes. Este conjunto de dados, obtido no [Kaggle](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn/data), contém informações sobre clientes bancários e seu 
#     comportamento, que utilizaremos para construir uma análise exploratória sobre o comportamento de churn.
# """)
# st.markdown("---")

# # Primeiras 5 linhas do dataset
# st.subheader("Primeiras 5 linhas do dataset")
# st.dataframe(dataset.head())

# st.markdown(f"O conjunto de dados contém {dataset.shape[0]} linhas e {dataset.shape[1]} colunas.")

# st.subheader("Análise estatística do conjunto de dados")
# st.dataframe(dataset.describe(include="all"))


# st.subheader("Distribuição de Tipos de Produtos Comprados")
# chart_products = dataset["NumOfProducts"].value_counts().reset_index()
# chart_products.columns = ['NumOfProducts', 'Count']

# fig = px.bar(chart_products, 
#              x='NumOfProducts', 
#              y='Count',
#              text='Count',
#              color_discrete_sequence=['#72a9cf'])

# fig.update_layout(
#     showlegend=False,
#     yaxis_visible=False,
#     yaxis_showticklabels=False,
#     xaxis_title="",
#     margin=dict(l=20, r=20, t=20, b=20)
# )

# fig.update_traces(textposition='outside')
# st.plotly_chart(fig, use_container_width=True)


# st.subheader("Distribuição de Gênero")
# chart_gender = dataset["Gender"].value_counts().reset_index()
# chart_gender.columns = ['Gender', 'Count']

# fig_gender = px.pie(chart_gender, 
#                     values='Count', 
#                     names='Gender',
#                     color_discrete_sequence=['#72a9cf'])

# fig_gender.update_layout(
#     showlegend=True,
# )

# st.plotly_chart(fig_gender, use_container_width=True)


# st.subheader("Distribuição de Idade")
# chart_age = dataset["Age"].value_counts().reset_index()
# chart_age.columns = ['Age', 'Count']

# fig_age = px.bar(chart_age, 
#                  x='Age', 
#                  y='Count',
#                  color_discrete_sequence=['#72a9cf'])

# fig_age.update_layout(
#     showlegend=False,
# )

# st.plotly_chart(fig_age, use_container_width=True)


# st.subheader("Distribuição de Produtos Comprados")
# chart_products= dataset["NumOfProducts"].value_counts().reset_index()
# chart_products.columns = ['NumOfProducts', 'Count']

# fig_products = px.pie(chart_products, 
#                     values='Count', 
#                     names='NumOfProducts',
#                     color_discrete_sequence=['#72a9cf'])

# fig_products.update_layout(
#     showlegend=True,
# )

# st.plotly_chart(fig_products, use_container_width=True)

# st.subheader("Cliente que possuem cartão de crédito")
# chart_has_card = dataset["HasCrCard"].value_counts().reset_index()
# chart_has_card.columns = ['HasCrCard', 'Count']

# fig_has_card = px.pie(chart_has_card, 
#                     values='Count', 
#                     names='HasCrCard',
#                     color_discrete_sequence=['#72a9cf'])

# fig_has_card.update_layout(
#     showlegend=True,
# )

# st.plotly_chart(fig_has_card, use_container_width=True)

# st.subheader("Satifção com o serviço")
# chart_satisfaction = dataset["Satisfaction Score"].value_counts().reset_index()
# chart_satisfaction.columns = ['Satisfaction Score', 'Count']

# fig_satisfaction = px.bar(chart_satisfaction, 
#                     x='Satisfaction Score', 
#                     y='Count',
#                     color_discrete_sequence=['#72a9cf'])    

# fig_satisfaction.update_layout(
#     showlegend=False,
# )

# st.plotly_chart(fig_satisfaction, use_container_width=True)

# st.subheader("Clientes ativos")
# chart_active = dataset["IsActiveMember"].value_counts().reset_index()
# chart_active.columns = ['IsActiveMember', 'Count']

# fig_active = px.pie(chart_active, 
#                     values='Count',
#                     names='IsActiveMember',
#                     color_discrete_sequence=['#72a9cf'])

# fig_active.update_layout(
#     showlegend=True,
# )

# st.plotly_chart(fig_active, use_container_width=True)


# criar um select de colunas categoricas para desenhar os graficos
# criar um select de colunas numericas para desenhar os graficos
# Criar outro select para fazer cruzamento de dados

# E ter uma opção de gerar um relatório detalhada das informações que por padrão será todos os graficos e tabelas e ter a 
# opção de escolher quais informações e graficos mostrar no relatório.

# https://www.kaggle.com/code/aliaagamal/bank-customer-churn-analysis-and-prediction


# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
from infrastructure.data_loader import dataset



# # Identificar colunas por tipo
# cat_cols = dataset.select_dtypes(include='object').columns.tolist()
# num_cols = dataset.select_dtypes(include='number').columns.tolist()

# st.sidebar.title("Configurações de Gráficos")

# # Seleções
# cat_col = st.sidebar.selectbox("Selecionar coluna categórica", cat_cols)
# num_col = st.sidebar.selectbox("Selecionar coluna numérica", num_cols)
# cross_col = st.sidebar.selectbox("Selecionar coluna para cruzamento", cat_cols + num_cols)

# # Opções de relatório
# st.sidebar.markdown("### Selecione elementos para o relatório")
# show_table = st.sidebar.checkbox("Mostrar Tabela", value=True)
# show_cat_plot = st.sidebar.checkbox("Gráfico categórico", value=True)
# show_num_plot = st.sidebar.checkbox("Gráfico numérico", value=True)
# show_cross_plot = st.sidebar.checkbox("Cruzamento de dados", value=True)

# st.title("Análise Interativa de Dados")

# # Mostra tabela
# if show_table:
#     st.subheader("Visualização da Tabela")
#     st.dataframe(dataset)

# # Gráfico categórico
# if show_cat_plot and cat_col:
#     st.subheader(f"Distribuição da variável: {cat_col}")
#     fig, ax = plt.subplots()
#     dataset[cat_col].value_counts().plot(kind='bar', ax=ax)
#     st.pyplot(fig)

# # Gráfico numérico
# if show_num_plot and num_col:
#     st.subheader(f"Distribuição da variável numérica: {num_col}")
#     fig, ax = plt.subplots()
#     sns.histplot(dataset[num_col], kde=True, ax=ax)
#     st.pyplot(fig)

# # Gráfico de cruzamento
# if show_cross_plot and cross_col:
#     st.subheader(f"Cruzamento entre {cat_col} e {cross_col}")
#     fig, ax = plt.subplots()
#     sns.boxplot(x=dataset[cat_col], y=dataset[cross_col], ax=ax)
#     st.pyplot(fig)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados (exemplo)

# Criar abas
aba_dados, aba_graficos = st.tabs(["📄 Dados", "📊 Gráficos"])

# Aba de dados
with aba_dados:
    st.subheader("Visualização dos Dados")
    st.dataframe(dataset)

# Aba de gráficos
with aba_graficos:
    st.subheader("Gráfico de Distribuição")
    coluna_num = st.selectbox("Selecione uma coluna numérica", dataset.select_dtypes(include='number').columns)

    fig, ax = plt.subplots()
    sns.histplot(dataset[coluna_num], kde=True, ax=ax)
    st.pyplot(fig)
