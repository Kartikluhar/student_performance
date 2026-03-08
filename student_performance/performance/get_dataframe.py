import pandas as pd
import numpy as np

def get_dataframe(file_path):

    df = pd.read_csv(file_path , sep=';')
    df = df.dropna()

    return df