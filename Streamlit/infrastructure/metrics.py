"""Módulo responsável por fazer as métricas dos dados."""

from utils.logger import log_message

# Usa @staticmethod já que nenhuma das funções usa self
class ChurnMetrics:
    """
    A classe ChurnMetrics contém métodos estáticos para calcular métricas relacionadas ao churn de clientes.
    Cada método recebe um DataFrame e retorna uma métrica específica, como o total de clientes, taxa de churn, etc.
    """
    @staticmethod
    def total_customer(df):
        """
        Retorna o número de clientes distintos.

        Args:
            df (DataFrame): DataFrame com os dados dos clientes

        Returns:
            int: Número total de clientes únicos
        """
        try:
            return df["CustomerId"].nunique()
        except Exception as e:
            log_message("ERR", "Erro ao calcular total_customer()", {"err": str(e)}, exc=e)
            return None

    @staticmethod
    def total_customer_churn(df):
        """
        Retorna o número total de clientes que deram churn (saíram).

        Args:
            df (DataFrame): DataFrame com os dados dos clientes

        Returns:
            int: Número de clientes que saíram
        """
        try:
            return df[df["Exited"] == "1"]["CustomerId"].nunique()
        except Exception as e:
            log_message("ERR", "Erro ao calcular total_customer_churn()", {"err": str(e)}, exc=e)
            return None

    @staticmethod
    def rate_churn(df):
        """
        Calcula a taxa de churn (clientes que saíram).

        Args:
            df (DataFrame): DataFrame com os dados dos clientes

        Returns:
            str: Taxa de churn formatada como porcentagem
        """
        try:
            churned = df[df['Exited'] == "1"]["CustomerId"].nunique()
            total = df["CustomerId"].nunique()
            return f"{churned / total:.2%}"
        except Exception as e:
            log_message("ERR", "Erro ao calcular rate_churn()", {"err": str(e)}, exc=e)
            return None

    @staticmethod
    def customer_retained(df):
        """
        Calcula a taxa de clientes retidos (que não deram churn).

        Args:
            df (DataFrame): DataFrame com os dados dos clientes

        Returns:
            str: Taxa de retenção formatada como porcentagem
        """
        try:
            retained = df[df['Exited'] == "0"]["CustomerId"].nunique()
            total = df["CustomerId"].nunique()
            return f"{retained / total:.2%}"
        except Exception as e:
            log_message("ERR", "Erro ao calcular customer_retained()", {"err": str(e)}, exc=e)
            return None
    
    @staticmethod
    def avg_satisfaction(df):
        """
        Calcula a pontuação média de satisfação dos clientes.
        Args:
            df (DataFrame): DataFrame com os dados dos clientes
        Returns:
            str: Pontuação média formatada com duas casas decimais
        """
        try:
            avg = df["SatisfactionScore"].mean()
            return f"{avg:.2f}"
        except Exception as e:
            log_message("ERR", "Erro ao calcular avg_satisfaction()", {"err": str(e)}, exc=e)
            return None
    
    @staticmethod
    def mean_balance(df):
        """
        Calcula o saldo médio dos clientes.

        Args:
            df (DataFrame): DataFrame com os dados dos clientes

        Returns:
            str: Saldo médio formatado com duas casas decimais
        """
        try:
            avg = df["Balance"].mean()
            return f"{avg:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        except Exception as e:
            log_message("ERR", "Erro ao calcular mean_balance()", {"err": str(e)}, exc=e)
            return None
