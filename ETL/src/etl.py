# =======================================
#             Bibliotecas
# =======================================
import os
import pandas as pd
import numpy as np

# ==============================================
# Pastas e subpastas do projeto
# ==============================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'landing')

# ==============================================
# Extração e validação dos dados
# ==============================================
def read_csv(filename:str,parse_dates:list):
    '''Leitura do arquivo'''
    df = pd.read_csv(os.path.join(DATA_DIR,filename), parse_dates=parse_dates)
    return df

def validation(df,date:str,id_item:str):
    '''Validando os tipos de dados'''
    if df.dtypes[[date]].item() == np.object:
        raise TypeError('O tipo de dado deve ser datetime64[ns].')
    elif df[[id_item]].isnull().values.any():
        raise TypeError('A coluna não pode conter valores nulos.')
    else:
        return df
