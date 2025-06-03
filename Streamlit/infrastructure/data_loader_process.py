"""Módulo responsável por carregar e processar os dados do dataset de Churn."""

import os
import sys
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.logger import log_message

def load_process():
    """
    Função para carregar e processar os dados para deixá-los prontos para
    análise exploratória e visualização.

    Return:
        pd.DataFrame: dataframe processado pronto para análise
    """
    try:
        dataset = pd.read_csv("data/Customer-Churn-Records.csv")
        dataset["Exited"] = dataset["Exited"].astype(str)
        dataset.drop(["RowNumber", "Surname"], axis=1, inplace=True)
        dataset.columns = dataset.columns.str.replace(" ", "")

        return dataset
    except (pd.errors.EmptyDataError, FileNotFoundError, pd.errors.ParserError, KeyError) as e:
        log_message("ERR", "load_process(): erro ao carregar e processar o dataset", {"err": str(e)}, exc=e)
        return None
