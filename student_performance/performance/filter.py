import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder


def filter_dataframe(file_path):

    df = pd.read_csv(file_path , sep=';')

    df.columns = df.columns.str.strip().str.lower()

    main_df = df[['g1', 'g2', 'failures', 'absences','studytime','g3']].copy()
    main_df = main_df.dropna()

    return main_df