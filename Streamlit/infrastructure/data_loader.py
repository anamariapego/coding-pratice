# Gerenciamento
import os

# Carregamento e processamento de dados
import pandas as pd

# Dataset
dataset = pd.read_csv(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "data",
        "Customer-Churn-Records.csv",
    )
)