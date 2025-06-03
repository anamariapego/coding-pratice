"""Módulo responsável por fazer a análise exploratória e vizualização dos dados """

from utils.logger import log_message
import plotly.express as px
import streamlit as st

import plotly.graph_objects as go
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class ChurnPlots:
    """
    Classe responsável por gerar gráficos e visualizações para análise de churn de clientes bancários.
    Utiliza Plotly Express para criar gráficos interativos e Streamlit para exibição na web.
    """

    def __init__(self):
        self.color_palette = px.colors.qualitative.Pastel
        self.color_palette_exited = {"0": "#2ECC71", "1": "#E74C3C"} 
    
    def _format_exited(self, df):

        df['Exited'] = df['Exited'].astype(str)
        df['Exited'] = pd.Categorical(df['Exited'], categories=["0", "1"], ordered=True)
        return df


    # Análise qualitativa
    def graf_qualitative(self, df, column):
        try:    
            df = self._format_exited(df)
            col1, col2 = st.columns(2)

            with col1:
                freq = df[column].value_counts().reset_index()
                freq.columns = [column, 'Contagem']
                fig_pizza = px.pie(freq, names=column, values='Contagem', 
                                color_discrete_sequence=self.color_palette,
                                title=f"Distribuição geral de {column}")
                st.plotly_chart(fig_pizza, use_container_width=True)

            with col2:
                grouped = df.groupby([column, 'Exited']).size().reset_index(name='Contagem')
                grouped = self._format_exited(grouped)
                fig_bar = px.bar(grouped, x=column, y='Contagem', color='Exited',
                                barmode='group', text='Contagem',
                                color_discrete_map=self.color_palette_exited,
                                title=f"{column} por Churn")
                fig_bar.update_traces(textposition='outside')
                st.plotly_chart(fig_bar, use_container_width=True)
        except Exception as e:
                log_message("ERR", f"Erro ao gerar gráfico graf_qualitative(): {str(e)}", {"err": str(e)}, exc=e)

    def graf_numerical(self, df, column):
        try:
            df = self._format_exited(df)
            fig_hist = px.histogram(
                df, 
                x=column, 
                color='Exited',
                barmode='overlay', 
                nbins=30,
                opacity=0.7,
                color_discrete_map=self.color_palette_exited,
                title=f"Distribuição de {column} por Churn"
            )
            st.plotly_chart(fig_hist, use_container_width=True)
        except Exception as e:
                log_message("ERR", f"Erro ao gerar gráfico graf_numerical(): {str(e)}", {"err": str(e)}, exc=e)

    def churn_por_geo(self, df_grouped):
        try:
            df_grouped = self._format_exited(df_grouped)
            fig = px.bar(
                df_grouped,
                x="Geography",
                y="Count",
                color="Exited",
                text="Count",
                color_discrete_map=self.color_palette_exited
            )

            fig.update_layout(
                barmode='group',
                title="Distribuição de Churn por Geografia",
                xaxis_title="",
                yaxis_visible=False,
                legend_title="Churn"
            )

            fig.update_traces(textposition='outside')
            return fig

        except Exception as e:
            log_message("ERR", f"Erro ao gerar gráfico churn_por_geografia(): {str(e)}", {"err": str(e)}, exc=e)
            return None

    def churn_financial(self, df, financial_feature):
        try:
            df = self._format_exited(df)
            fig = px.box(
                df,
                x="Exited",
                y=financial_feature,
                color="Exited",
                color_discrete_map=self.color_palette_exited,
                points="all"
            )
            fig.update_layout(
                title=f"{financial_feature} por Churn",
                xaxis_title="Churn",
                yaxis_title=financial_feature,
                showlegend=False
            )
            return fig
        except Exception as e:
            log_message("ERR", f"Erro ao gerar gráfico churn_financial(): {str(e)}", {"err": str(e)}, exc=e)
            return None

    def products(self, df):
        try:
            df = self._format_exited(df)
            fig = px.histogram(
                data_frame=df,
                x='NumOfProducts',
                color='Exited',
                barmode="group",
                color_discrete_map=self.color_palette_exited,
                title="Distribuição de Churn por Produtos",
                labels={'NumOfProducts': 'Quantidade de Produtos', 'Exited': 'Churn'}
            )
            return fig
        except Exception as e:
            log_message("ERR", f"Erro ao gerar gráfico fig_products(): {str(e)}", {"err": str(e)}, exc=e)
            return None

    def behavior(self, df):
        try:
            df = self._format_exited(df)
            fig = px.scatter(
                df,
                x='Age',
                y='EstimatedSalary',
                color='Exited',
                facet_col='Exited',
                color_discrete_map=self.color_palette_exited,
                title="Idade vs Salário Estimado Separado por Churn",
                labels={'Exited': 'Churn', 'Age': 'Idade', 'EstimatedSalary': 'Salário Estimado'}
            )
            fig.update_layout(showlegend=False)
            return fig
        except Exception as e:
            log_message("ERR", f"Erro ao gerar gráfico behavior(): {str(e)}", {"err": str(e)}, exc=e)
            return None

    def graf_funil(self, df):
        try:
            df["Exited"] = df["Exited"].astype(int)
            funnel_df = pd.DataFrame({
                "Etapa": ["Tem Cartão de Crédito", "Cliente Ativo", "Fez Reclamação", "Saiu (Churn)"],
                "Quantidade": [
                    df['HasCrCard'].sum(),
                    df['IsActiveMember'].sum(),
                    df['Complain'].sum(),
                    df['Exited'].sum()
                ]
            })

            fig_funnel = px.funnel(funnel_df, 
                                   x='Quantidade', 
                                   y='Etapa', 
                                   title="Funil de Retenção", 
                                   color_discrete_sequence=self.color_palette
                                )
            fig_funnel.update_layout(
                yaxis_title="",
                showlegend=False
            )
            return fig_funnel
        except Exception as e:
            log_message("ERR", f"Erro ao gerar gráfico graf_funil(): {str(e)}", {"err": str(e)}, exc=e)
            return None

    def graf_importance_variable(self, df):
        try:
            numerical_cols = [
                'CreditScore', 'Age', 'Tenure', 'Balance', 
                'NumOfProducts', 'EstimatedSalary', 'PointEarned', 
                'SatisfactionScore'
            ]
            X = df[numerical_cols].fillna(df[numerical_cols].mean())
            y = df['Exited']

            model = RandomForestClassifier(random_state=42)
            model.fit(X, y)
            importances = model.feature_importances_

            imp_df = pd.DataFrame({
                "Feature": numerical_cols, 
                "Importance": importances
            }).sort_values(by="Importance", ascending=False)

            fig_imp = px.bar(
                imp_df, 
                x='Importance', 
                y='Feature', 
                orientation='h', 
                title="Importância das Features",
                color_discrete_sequence=self.color_palette
            )
            return fig_imp
        except Exception as e:
            log_message("ERR", f"Erro ao gerar gráfico graf_importance_variable(): {str(e)}", {"err": str(e)}, exc=e)
            return None
        
    # 📊 Customer Lifetime Value Estimado (Balance * SatisfactionScore)
    def graf_customer_lifetime_value(self, df):
        try:
            df = self._format_exited(df)
            df['CLV'] = df['Balance'] * df['SatisfactionScore']
            fig = px.box(df, x='Exited', y='CLV', color='Exited', color_discrete_map=self.color_palette_exited,
                         title='Customer Lifetime Value por Churn')
            return fig
        except Exception as e:
            log_message("ERR", f"Erro ao gerar gráfico CLV: {str(e)}", {"err": str(e)}, exc=e)
            return None
