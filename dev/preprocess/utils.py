import pandas as pd
import numpy as np


def _class_ocup(x: int):
    x = str(x)
    if len(x) != 6:
        return 0
    elif x == '999991':  # Estudante
        return 11
    elif x == '999992':  # Dona de casa
        return 12
    else:
        return int(x[:1])


def classify (df: pd.DataFrame) -> pd.DataFrame:
    map = {
        1: 1,
        2: 2,
        4: 2
    }

    df['RACACOR'] = df['RACACOR'].map(map)

    df['CODOCUPMAE'] = df['CODOCUPMAE'].apply(_class_ocup)

    return df


def remove_outliers (df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR

    upper_array = df.loc[df[column] > upper].index
    lower_array = df.loc[df[column] < lower].index

    df.drop(index=upper_array, inplace=True)
    df.drop(index=lower_array, inplace=True)

    return df